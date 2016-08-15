import os
import cv2
import numpy as np

def SimilarRateWithSameShp(img1,img2):
	horiNum = img1.shape[0]
	coluNum = img1.shape[1]
	simiPoint = 0
	for i in range(coluNum):
		for j in range(horiNum):
			if img1[j][i] == img2[j][i]:
				simiPoint = simiPoint + 1
	return (1.0*simiPoint)/(horiNum*coluNum)

def CutOneColuAtLef(img):
	imgC = img[0:(img.shape[0]),1:(img.shape[1])]
	return imgC

def CutOneColuAtRig(img):
	imgC = img[0:(img.shape[0]),0:(img.shape[1]-1)]
	return imgC

def CutOneLineAtTop(img):
	imgC = img[1:(img.shape[0]),0:(img.shape[1])]
	return imgC

def CutOneLineAtBot(img):
	imgC = img[0:(img.shape[0]-1),0:(img.shape[1])]
	return imgC

def CutLefAndTop(img):
	imgC = CutOneLineAtTop(img)
	imgC = CutOneColuAtLef(imgC)
	return imgC

def CutLefAndBot(img):
	imgC = CutOneLineAtBot(img)
	imgC = CutOneColuAtLef(imgC)
	return imgC

def CutRigAndBot(img):
	imgC = CutOneLineAtBot(img)
	imgC = CutOneColuAtRig(imgC)
	return imgC

def CutRigAndTop(img):
	imgC = CutOneLineAtTop(img)
	imgC = CutOneColuAtRig(imgC)
	return imgC

def MaxSimilarRateWithSameShp(img1,img2):
	maxSR = SimilarRateWithSameShp(img1,img2)
	cmp1 = CutOneColuAtLef(img1)
	cmp2 = CutOneColuAtRig(img2)
	SR=SimilarRateWithSameShp(cmp1,cmp2)
	if (SR>maxSR):
		maxSR = SR
	cmp1 = CutOneColuAtLef(img2)
	cmp2 = CutOneColuAtRig(img1)
	SR=SimilarRateWithSameShp(cmp1,cmp2)
	if (SR>maxSR):
		maxSR = SR
	cmp1 = CutOneLineAtTop(img1)
	cmp2 = CutOneLineAtBot(img2)
	SR=SimilarRateWithSameShp(cmp1,cmp2)
	if (SR>maxSR):
		maxSR = SR
	cmp1 = CutOneLineAtTop(img2)
	cmp2 = CutOneLineAtBot(img1)
	SR=SimilarRateWithSameShp(cmp1,cmp2)
	if (SR>maxSR):
		maxSR = SR
	cmp1 = CutLefAndTop(img1)
	cmp2 = CutRigAndBot(img2)
	SR=SimilarRateWithSameShp(cmp1,cmp2)
	if (SR>maxSR):
		maxSR = SR
	cmp1 = CutLefAndBot(img1)
	cmp2 = CutRigAndTop(img2)
	SR=SimilarRateWithSameShp(cmp1,cmp2)
	if (SR>maxSR):
		maxSR = SR
	cmp1 = CutLefAndTop(img2)
	cmp2 = CutRigAndBot(img1)
	SR=SimilarRateWithSameShp(cmp1,cmp2)
	if (SR>maxSR):
		maxSR = SR
	cmp1 = CutLefAndBot(img2)
	cmp2 = CutRigAndTop(img1)
	SR=SimilarRateWithSameShp(cmp1,cmp2)
	if (SR>maxSR):
		maxSR = SR
	return maxSR


def MaxSimilarRateWithOneColuDif(img1,img2):
	if img2.shape[1]>img1.shape[1]:
		temp = img1
		img1 = img2
		img2 = temp
	cmp1 = CutOneColuAtLef(img1)
	maxSR = -1
	SR=MaxSimilarRateWithSameShp(cmp1,img2)
	if (SR>maxSR):
		maxSR = SR
	cmp1 = CutOneColuAtRig(img1)
	SR=MaxSimilarRateWithSameShp(cmp1,img2)
	if (SR>maxSR):
		maxSR = SR
	return maxSR

def MaxSimilarRateWithOneLineDif(img1,img2):
	if img2.shape[0]>img1.shape[0]:
		temp = img1
		img1 = img2
		img2 = temp
	cmp1 = CutOneLineAtTop(img1)
	maxSR = -1
	SR=MaxSimilarRateWithSameShp(cmp1,img2)
	if (SR>maxSR):
		maxSR = SR
	cmp1 = CutOneLineAtBot(img1)
	SR=MaxSimilarRateWithSameShp(cmp1,img2)
	if (SR>maxSR):
		maxSR = SR
	return maxSR

def SimilarRate(img1,img2):
	if img1.shape == img2.shape:
		return MaxSimilarRateWithSameShp(img1,img2)
	if ((abs(img1.shape[0]-img2.shape[0]) == 1)and(img1.shape[1] == img2.shape[1])):
		return MaxSimilarRateWithOneLineDif(img1,img2)
	elif abs(img1.shape[0]-img2.shape[0])>=2:
		return -1
	if ((abs(img1.shape[1]-img2.shape[1]) == 1)and(img1.shape[0] == img2.shape[0])):
		return MaxSimilarRateWithOneColuDif(img1,img2)
	elif abs(img1.shape[1]-img2.shape[1])>=3:
		return -1
	return -1
	

def PrtPicShape(img):
	print (img.shape)
	cv2.imshow('image',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def FindTheLowestSR(img,numChar,learnNum):
	miniSR = 100
	miniTempChar = '10'
	for i in range(learnNum):
		pathStr = numChar+r'/template'+str(i)+'.jpg'
		if os.path.exists(pathStr):
			temp = cv2.imread(pathStr) 
			temp = cv2.cvtColor(temp,cv2.COLOR_BGR2GRAY)
			ret,temp = cv2.threshold(temp,150,255,cv2.THRESH_BINARY)
			SR = SimilarRate(img,temp)                              
			if ((SR<miniSR)and(SR!=-1)):
#				print ('目前相似度最低的图片是:'+str(i))
				miniSR = SR              
				miniTempChar = str(i)
	return miniTempChar

def Recognize(img,learnNum):
	SimRat = -1
	numChar = '-1'
	for i in range(9):
		strOfNum = str(i+1)
		for j in range(learnNum):
			pathStr = strOfNum+r'/template'+str(j)+'.jpg'
			if os.path.exists(pathStr):
				temp = cv2.imread(pathStr)
				temp = cv2.cvtColor(temp,cv2.COLOR_BGR2GRAY)
				ret,temp = cv2.threshold(temp,150,255,cv2.THRESH_BINARY)
				SR = SimilarRate(img,temp)
				if SR>SimRat:
					SimRat = SR
					numChar = strOfNum
#				print ('in'+str(j))
			else:
				break
	miniCheckFile = open('Mini','w+')
	tempStr = ('template'+FindTheLowestSR(img,numChar,learnNum)+'.jpg')
	miniCheckFile.write(numChar+r'/'+tempStr)
	miniCheckFile.close()
#	print ("Recognize single char!")
	return numChar

def RecognizeCheckCode(num = 4,learnNum = 200):
	strStr = ''
	recoLogFP = open('recoLong','w+')
	for i in range(1,num+1):
		strCharFile = str(i)
		img = cv2.imread(r'char'+strCharFile+'.jpg')
		img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		ret,img = cv2.threshold(img,150,255,cv2.THRESH_BINARY)
		strChar = Recognize(img,learnNum)
		miniPathFP = open('Mini','r')
		miniStr = miniPathFP.readline()
		miniPathFP.close()
		recoLogFP.write(miniStr+'\n')
		if strChar == '-1':
			print ('Recognize error')
			print (i)
			recoLogFP.close()
			return '-1'
		strStr = strStr+strChar
	recoLogFP.close()
	return strStr
if __name__ == '__main__':
	print (RecognizeCheckCode())
