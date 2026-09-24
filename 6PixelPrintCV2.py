import cv2

img = cv2.imread("BTTH_10.png")

img[100,200] = [0,255,0]
cv2.imwrite("output(0).png", img)