from CheckSegmentInline import *
from GetSingleChar import *
import cv2
import numpy as np
#from matplotlib import pyplot as plt
def Detect(imgFileName,outputFileName):
	img = cv2.imread(imgFileName)
	b,g,r = cv2.split(img)
	ret,g = cv2.threshold(g,180,255,cv2.THRESH_BINARY_INV)
	cv2.imwrite(outputFileName,g)
	return g
#blur = b
#b = cv2.blur(b,(3,3))
#ret,b = cv2.threshold(b,180,255,cv2.THRESH_BINARY)

#blur = cv2.bilateralFilter(blur,9,75,75)
#ret,b = cv2.threshold(b,180,255,cv2.THRESH_BINARY)
	
#ret,r = cv2.threshold(r,180,255,cv2.THRESH_BINARY)
#cv2.imwrite('b_output.jpg',b)

#cv2.imwrite('r_output.jpg',r)
#cv2.imwrite('blur_output.jpg',blur)
#img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#ret,img2 = cv2.threshold(img,180,255,cv2.THRESH_BINARY)
#print type(img2)
#img = cv2.medianBlur(img,3)

#ret,img1 = cv2.threshold(img,150,255,cv2.THRESH_BINARY)
#cv2.imwrite('output1.jpg',img1)
#img2 = blur = cv2.GaussianBlur(img2,(3,3),0)
#img2 = blur = cv2.GaussianBlur(img2,(3,3),0)
#ret,img2 = cv2.threshold(img2,100,255,cv2.THRESH_BINARY_INV)
#cv2.imwrite('output2.jpg',img2)
#cv2.imwrite('output3.jpg',img)
#print img2.shape
#print img2.shape[1]
#print type(img2.shape[1])
#print SplitToSingle(g)
#firstSt = CharStart(img2,60,20)
#firstEn = FirstCharEnd(img2,60,20)
#width = firstEn - firstSt + 1
#img4 = img2[0:20,firstSt:(firstEn+1)]
#horiSt = HoriCharStart(img4,width,20)
#horiEn = HoriCharEnd(img4,width,20)
#print width
#print firstSt
#print firstEn
#print horiSt
#print horiEn
#img4 = img4[horiSt:(horiEn+1),0:width]
#cv2.imwrite('output4.jpg',img4)
if __name__ == '__main__':
	Detect('output.jpg','g.jpg')
