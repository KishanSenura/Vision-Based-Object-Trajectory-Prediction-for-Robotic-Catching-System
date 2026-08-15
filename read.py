import cv2 as cv

img = cv.imread(r'C:\Users\Senura\Desktop\Open CV\kk1-1.jpg',-1)
img = cv.resize(img,(1000,1000))


cv.imshow('Image',img)

cv.waitKey(0) #time delay in miliseconds
cv.destroyAllWindows()




