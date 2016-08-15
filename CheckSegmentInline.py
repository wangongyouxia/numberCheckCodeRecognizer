import numpy as np

def HoriStartPoint( ary,width,horiNum):
	for i in  range(width):
#		print i
		if ary[horiNum][i] == 0:
			return i
	return -1

def ColumnStartPoint( ary,column,heigth):
	for i in  range(heigth):
		if ary[i][column] == 0:
			return i
	return -1

def EndPiont( ary):
	length = ary.length	
	for i in  range(length,0,-1):
		if ary[i] == 0:
			return i
	return -1

def SegmentNumInLine( ary):
	length = ary.length
	outSeg = True
	ret =0
	segLen = 0
	for i in range(length):
		if ary[i] == 0:
			if outSeg:
				ret = ret+1
				outSeg = False
		else:
			outSeg = True
	return ret

def CharStart(ary,width,heigth):
	for i in range(width):
		if ColumnStartPoint(ary,i,heigth) != -1:
			return i
	return -1

def HoriCharStart(ary,width,heigth):
	for i in range(heigth):
		if HoriStartPoint(ary,width,i) != -1:
			return i
	return -1

def FirstCharEnd(ary,width,heigth):
	startScan = CharStart(ary,width,heigth)+1
	inChar = False
	for i in range(startScan,width):
		if ColumnStartPoint(ary,i,heigth) == -1:
			if inChar == True:
				return i-1
		else:
			inChar = True
	return -1

def HoriCharEnd(ary,width,heigth):
	for i in range(heigth-1,-1,-1):
		if HoriStartPoint(ary,width,i) != -1:
			return i
	return -1

def CharWidth( ary,):
	if((CharStart!=-1)and(FirstCharEnd!=-1)):
		return FirstCharEnd(ary)-CharStart(ary)
