import os

def GetFileNum(path):
	count = sum([len(x) for _, _, x in os.walk(os.path.dirname(path))])
	return (count)               #输出结果
if __name__ == '__main__':
	print (GetFileNum('./1/'))

