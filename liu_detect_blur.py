import cv2

##imagePath="image_010.png" #307.45
##imagePath="./pureWhite2.png" #4964.61
##imagePath="./xie.jpg"#1281.71
##imagePath="./demo.png"#163.92
##imagePath="./6.jpg"#82.32
##imagePath="./pureWhite.png"#0.0

imagePath="./v1.png" #1633.18
#imagePath="./v2.png" #1.59
#imagePath="./v3.png" #2.31

def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image,cv2.CV_16S,ksize=1).var()

image = cv2.imread(imagePath)
cv2.imshow("Image", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
fm = variance_of_laplacian(gray)
text=""

# show the image
cv2.putText(image, "{} {:.2f}".format(text, fm), (0, 30),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.6, (0, 0, 255),2)
cv2.imshow("Image", image)

#cv2.imshow("gray", cv2.Laplacian(gray, cv2.CV_64F))
key = cv2.waitKey(2)
print(fm)
