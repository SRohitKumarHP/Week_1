import cv2

img = cv2.imread("BTTH_10.png")

rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(rgb)