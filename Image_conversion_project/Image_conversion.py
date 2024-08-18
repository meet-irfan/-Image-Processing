import cv2

#Image conversion project colored image into grayscale.

path = input("Enter the Path and name of an image===")
print("You Enter this===",path)

#Now read image 
img1 = cv2.imread(path,0) #convert image into grayscale
img1 = cv2.resize(img1,(560,700))
img1 = cv2.flip(img1,1)#it accept 3 parameters 0,-1,1
cv2.imshow("converted image==",img1)

cv2.waitKey()
cv2.destroyAllWindows()