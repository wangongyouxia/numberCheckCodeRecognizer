import cv2
from FileNum import *

def AddTemp(fileNum):
	fileNumStr = str(fileNum)	
	getFirstCharOfLogFP = open('recoLong','r')
	for i in range(1,5):
		iStr = str(i)
		log = getFirstCharOfLogFP.readline()
		numStr = log[0]
		imgStr = 'char'+iStr+'.jpg'
		img = cv2.imread(imgStr)
#		cv2.imshow('image',img)
#		cv2.waitKey(0)
#		cv2.destroyAllWindows()
		writePathStr = numStr+r'/'+'template'+fileNumStr+'.jpg'
		cv2.imwrite(writePathStr,img)
	getFirstCharOfLogFP.close()
	return 0

def ReplaceTemp():
	getFirstCharOfLogFP = open('recoLong','r')
	for i in range(1,5):
		iStr = str(i)
		log = getFirstCharOfLogFP.readline()
		imgStr = 'char'+iStr+'.jpg'
		img = cv2.imread(imgStr)
		cv2.imwrite(log,img)
	getFirstCharOfLogFP.close()

def Learn(learnNum = 200):
	fileNum = learnNum
	for i in range(1,10):
		dirStr = str(i)
		fileN = GetFileNum(r'./'+dirStr+r'/')
#		print ('第'+str(i)+'个字符现在有'+str(fileN)+'张图片')
		if fileN<fileNum:
			fileNum = fileN
	print ('现在在学习第'+str(fileNum)+'张图！')
	if fileNum<learnNum:
		AddTemp(fileNum)
	else:
		ReplaceTemp()

if __name__ == '__main__':
	Learn()
