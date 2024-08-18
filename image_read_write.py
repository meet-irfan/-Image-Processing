import cv2 

img = cv2.imread("D:\Pictures\\irfan.jpg",1)
cv2.imshow("orginal", img)
img = cv2.resize(img, (1450,800))
print("Colorful picture",img)



# gray picture show 
img1 = cv2.imread("D:\Pictures\\irfan.jpg",0)
img1 = cv2.resize(img1, (1450,800))
print(" Gray pic ==\n",img1)
cv2.imshow("gray Picture ", img1)

# Unchanged Picture show 
img2 = cv2.imread("D:\Pictures\\irfan.jpg",-1)
img2 = cv2.resize(img2, (1450,800))
print(" Unchanged Picture  ==\n",img2)
cv2.imshow("unchanged Picture ", img2)



cv2.waitKey()
cv2.destroyAllWindows()
