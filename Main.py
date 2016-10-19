#!/usr/bin/env python
# -*- coding:utf-8 -*-

from GetSingleChar import *
from Detect import *
from Recognize import *
from MachineLearn import *
def Test():
	learnNum = 20
	g = Detect('output.jpg','g.jpg')
	if SplitToSingle(g) != 4:
		print('不是四个字符！')
		exit(-1)
	CheckCode = RecognizeCheckCode(4,learnNum)
	if CheckCode == '-1':
		print('识别失败')
		exit(-1)
	Learn(learnNum)
	print (CheckCode)

if __name__ == '__main__':
	Test()
