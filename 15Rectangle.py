import cv2

img = cv2.imread("BTTH_10.png")
cv2.rectangle(img, (1000,1000), (100,100), (255,0,0), 2)
cv2.imwrite("output(0).png", img)