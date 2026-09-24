import cv2
img = cv2.imread("BTTH_10.png")
cv2.flip(img,1) #Horizontal Flip
cv2.flip(img,0) #Vertical Flip
cv2.flip(img,-1) #Both Flips