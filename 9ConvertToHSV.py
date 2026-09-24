import cv2

img = cv2.imread("BTTH_10.png")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print(hsv)