import cv2

img = cv2.imread("BTTH_10.png")

crop = img[100:400, 200:500]
print(crop)