import numpy as np
import cv2

img = cv2.imread(r'C:\Users\Senura\Desktop\Open CV\images.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


conners = cv2.goodFeaturesToTrack(gray, 10, 0.01, 10)
conners = conners.astype(np.int32)

for conner in conners:
    x, y = conner.ravel()
    cv2.circle(img, (x,y), 5, (255,0,0), -1)

for i in range(len(conners)):
    for j in range(i + 1, len(conners)):
        conner1 = tuple(conners[i][0])
        conner2 = tuple(conners[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0,255, size=3)))
        cv2.line(img, conner1, conner2, color, 1)


cv2.imshow('frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()






