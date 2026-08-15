import numpy as np
import cv2 as cv



cap = cv.VideoCapture(0)

# Load template only once
template_original = cv.imread(
    r'C:\Users\Senura\Desktop\Open CV\Project\4444.jpg',
    0
)

method = cv.TM_SQDIFF_NORMED

while True:

    ret, frame = cap.read()

    if not ret:
        break


    img2 = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    best_value = 1
    best_location = None
    best_w = 0
    best_h = 0
    best_scale = 0

    for scale in np.linspace(0.5, 2.0, 20):

        template = cv.resize(template_original, (0,0), fx=scale, fy=scale)

        h, w = template.shape

        if h > img2.shape[0] or w > img2.shape[1]: # check temp biger than frame
            continue

        result = cv.matchTemplate(img2, template, method)

        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

        if min_val < best_value:

            best_value = min_val
            best_location = min_loc
            best_w = w
            best_h = h
            best_scale = scale


    if best_location is not None and best_value < 0.3:  # to avoid unnessary drawing when no good match is found

        x = best_location[0]
        y = best_location[1]

        bottom_right = (x + best_w, y + best_h)

        cv.rectangle(frame, best_location, bottom_right, (0, 0, 255), 1)

        
        center_x = x + best_w // 2 # center of object
        center_y = y + best_h // 2

        
        cv.circle(frame, (center_x, center_y), 5, (0, 255, 0), -1)

        cv.putText(frame, f"Scale: {best_scale:.2f}", (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        cv.putText(frame, f"X:{center_x} Y:{center_y}", (20, 40), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    cv.imshow('Match', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv.destroyAllWindows()