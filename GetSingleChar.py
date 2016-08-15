from CheckSegmentInline import *
import cv2
import numpy as np

def SplitToSingle(img,num = 0):
	width = img.shape[1]
	heigth = img.shape[0]
	firstSt = CharStart(img,width,heigth)
	firstEn = FirstCharEnd(img,width,heigth)
	charWidth = firstEn - firstSt + 1
	if charWidth>1:
		num = num + 1
	else:
		return num
	charPicWithHoriBlack = img[0:heigth,firstSt:(firstEn+1)]
	horiSt = HoriCharStart(charPicWithHoriBlack,charWidth,heigth)
	horiEn = HoriCharEnd(charPicWithHoriBlack,charWidth,heigth)
	charPic = img[horiSt:(horiEn+1),firstSt:(firstEn+1)]
	strOfNum = str(num)
	cv2.imwrite(('char'+strOfNum+'.jpg'),charPic)
	theRestPic = img[0:heigth,(firstEn+1):width]
	return SplitToSingle(theRestPic,num)
