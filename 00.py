import cv2

img = cv2.imread("BTTH_10.png")
print(img.shape)
grey = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.show()
cv2.waitKey(0)