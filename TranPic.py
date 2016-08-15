from PIL import Image                     
def ConvertToJpg(inputFileName,outputFileName):
	im = Image.open(inputFileName)   
	im = im.convert('RGB') 
	im.save(outputFileName,"jpeg")  

if __name__ == '__main__':
	ConvertToJpg('save_get.gif','output.jpg')
