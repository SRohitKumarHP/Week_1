import cv2

img = cv2.imread("BTTH_10.png")

resized = cv2.resize(img, (200, 200))