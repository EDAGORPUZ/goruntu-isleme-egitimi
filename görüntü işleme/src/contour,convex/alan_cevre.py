import cv2

img = cv2.imread('ucgen.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, ret = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


cnt = contours[0]
area = cv2.contourArea(cnt)
print(area)#contour kullanarak alan bulma


M = cv2.moments(cnt)
print(M['m00'])  #moments kullanarak alan bulma


perimeter = cv2.arcLength(cnt, True) #true= kapalı açık durumu için
print(perimeter)


cv2.imshow('orj', img)
cv2.imshow('gray', gray)
cv2.imshow('thresh', thresh)


cv2.waitKey(0)
cv2.destroyAllWindows()



