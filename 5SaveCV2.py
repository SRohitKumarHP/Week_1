import cv2

img = cv2.imread("BTTH_10.png")

cv2.imwrite("output.jpg", img)