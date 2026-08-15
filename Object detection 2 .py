import cv2 as cv

cap = cv.VideoCapture(0)

# Background subtractor
back_sub = cv.createBackgroundSubtractorMOG2(history=250, varThreshold=15, detectShadows=False)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Create foreground mask
    mask = back_sub.apply(frame)

    # Remove small noise
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))

    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)

    mask = cv.dilate(mask, kernel, iterations=2)

    # Find moving regions
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for contour in contours:

        area = cv.contourArea(contour)

        # Ignore very small movements/noise
        if area < 800 or area > 3000:  # Adjust the threshold as needed
            continue

        x, y, w, h = cv.boundingRect(contour)

        # Draw bounding box
        cv.rectangle(frame,(x, y),(x + w, y + h),(0, 255, 0),2)

        # Center of moving object
        center_x = x + w // 2
        center_y = y + h // 2

        cv.circle(frame,(center_x, center_y),5,(0, 0, 255),-1) 

        cv.putText(frame,f"({center_x}, {center_y})",(x, y - 10),cv.FONT_HERSHEY_SIMPLEX, 0.6,(255, 0, 0), 2)

    cv.imshow("Moving Objects", frame)
    cv.imshow("Motion Mask", mask)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv.destroyAllWindows()