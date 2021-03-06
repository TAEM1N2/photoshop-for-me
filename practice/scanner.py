import cv2
import numpy as np 

win_name = "scan"

#original img
img = cv2.imread("paper.jpg")
cv2.imshow("original", img)
cv2.waitKey(0)
draw = img.copy()

#grayScale / gaussianBlur / CannyEdge  
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3,3), 0)
edged = cv2.Canny(gray, 100,200)
cv2.imshow("win_name", edged)
cv2.waitKey(0)

cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(draw, cnts, -1, (0,255,0))

cv2.imshow(win_name, draw)
cv2.waitKey(0)



