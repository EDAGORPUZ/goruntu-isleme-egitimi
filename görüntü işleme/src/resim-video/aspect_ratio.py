import cv2 # type: ignore

def resizewithAspectRatio(img, width = None , height = None, inter = cv2.INTER_AREA): #prmtre1= tutulan değişken adı Pprmtre4=çakışmaları önlemek için

    dimension = None
    (h,w) = img.shape[:2]  #boy ve en için tuple oluşturduk ve shape ile boyutları atadık.
    
    if width is None and height is None:  #en ve boy girilmediyse orijinal rsmi döndürür
        return img
    
    if width is None:    #en girilmediyse boyut için tanımlanan işlem yapılsın.
        r = height / float(h)  
        dimension = (int(w*r), height)
    
    else:  
        r = width / float(w)
        dimension = (width, int(h*r))
        
    return cv2.resize(img, dimension, interpolation = inter)
    
img = cv2.imread("resim okuma.png")
img1 = resizewithAspectRatio(img, width = None , height = 600, inter = cv2.INTER_AREA)

cv2.imshow('original: ', img)
cv2.imshow('resized: ', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
