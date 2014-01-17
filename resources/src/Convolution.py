import cv2
import numpy as np
import Image

class ImageConvolution():
	"""docstring for ImageConvolution"""
	__image_origianl=""
	__new_img=""
	__kernel=""
	__img_output=""
	__array_filter=[[1,1,1],[1,1,1],[1,1,1]]

	def __init__(self, img):		
		self.image_origianl=img
		self.__image_origianl = cv2.imread(img)
		self.image_new=img

	def __convolve2d(self,array_filter):
		self.__kernel=np.array(array_filter,np.float32)   # kernel should be floating point type.
		self.__new_img = cv2.filter2D(self.__image_origianl,-1,self.__kernel)        # ddepth = -1, means destination image has depth same as input image.

	def setImage(self,img):
		img = cv2.imread(img)
		self.image_origianl=img
		self.image_new=img		

	def setFilter(self,array_filter):
		self.__array_filter=array_filter

	def getImage(self,array_filter):
		if not array_filter:
			array_filter = self.__array_filter
		self.__convolve2d(array_filter)		
		self.__img_output = Image.fromarray(self.__new_img, 'RGB')
		return self.__img_output
			

	def saveImageAs(self,path,array_filter=None):
		if not array_filter.any():
			array_filter = self.__array_filter
		self.__convolve2d(array_filter)		
		self.__img_output = Image.fromarray(self.__new_img, 'RGB')
		self.__img_output.save(path)









"""
img = cv2.imread('lena.jpg')

kernel = np.array([ [0,1,0],
                    [1,-4,1],
                    [0,1,0] ],np.float32)   # kernel should be floating point type.

new_img = cv2.filter2D(img,-1,kernel)        # ddepth = -1, means destination image has depth same as input image.

print new_img
img = Image.fromarray(new_img, 'RGB')
img.save('my.jpg')
#cv2.imwrite("image_processed.png", new_img)"""

