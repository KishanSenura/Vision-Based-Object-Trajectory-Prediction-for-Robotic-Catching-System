import numpy as np
import cv2 as cv


img = cv.imread(r'C:\Users\Senura\Desktop\Open CV\WIN_20260809_01_55_35_Pro.jpg', 0) # need a gray scale image
template = cv.imread(r'C:\Users\Senura\Desktop\Open CV\1111.jpg', 0)


h, w = template.shape # two dimentional array because of gray

methods = [cv.TM_CCOEFF, cv.TM_CCOEFF_NORMED, cv.TM_CCORR, cv.TM_CCORR_NORMED, cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()

    result = cv.matchTemplate(img2, template, method) # (W - w + 1 , H - h + 1) array
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]: # these method use min_location
        location = min_loc
    else:
        location = max_loc
    bottom_right = (location[0] + w, location[1] + h)
    cv.rectangle(img2, location, bottom_right, 255, 5)
    cv.imshow('Match',img2)
    cv.waitKey(0)
    cv.destroyAllWindows()

    






