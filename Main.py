#!/usr/bin/env python
# -*- coding:utf-8 -*-
from PIL import Image
from random import Random
import cv2

from GetSingleChar import *
from Detect import *
from Recognize import *
from TranPic import *
from MachineLearn import *

learnNum = 20
g = Detect('output.jpg','g.jpg')
if SplitToSingle(g) != 4:
	print ('不是四个字符！')
	exit(-1)
CheckCode = RecognizeCheckCode(4,learnNum)
print (CheckCode)
