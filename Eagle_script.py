## Program Name:    Eagle script
## Program Author:  Ahmed Samir Oraby
## Email:           ahmed.oraby@gizasystems.com
## Date: 	    3/1/2018
##

import numpy as np
import cv2

 

im = cv2.imread('a2.png')



imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
siza= im.shape



ret,mask=cv2.threshold(imgray,50,255,cv2.THRESH_BINARY)
con,h=cv2.findContours(mask,1,2)

for i in con:
    (x,y,w,h)=cv2.boundingRect(i)
    # 20 is the diameter of the circle
    cv2.circle(im,((x + w/2),(y + h/2)), 10, (255,0,0), -1)

for s in range(0,siza[0]):
    for ss in range(0,siza[1]):
        pix=im[s][ss]
        if pix[0]>200:
            im[s][ss]=(0,0,0)
        else:
            im[s][ss]=(255,255,255)

#the output image 
cv2.imwrite('new.png',im)

cv2.waitKey(0)
cv2.destroyAllWindows()
