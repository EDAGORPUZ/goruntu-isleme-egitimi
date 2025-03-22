#SMOOTHİNG İMAGE = RESİM YUMUŞATMA
import cv2
import numpy as np

img_filter = cv2.imread("filter.png")
img_median = cv2.imread("median.png")
img_bilateral = cv2.imread("bilateral.png")

blur = cv2.blur(img_filter, (7,7))  #p2= yumuşama oranı(sadece tek sayılar girilebilr.)
g_blur = cv2.GaussianBlur(img_filter, (5,5), cv2.BORDER_DEFAULT)
#p3= sınır değerler(varsayılan seçili)

m_blur = cv2.medianBlur(img_median, 5)


cv2.imshow('original', img_filter)
cv2.imshow('blur', blur)
cv2.imshow('g_blur', g_blur)
cv2.imshow('m_blur', m_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
