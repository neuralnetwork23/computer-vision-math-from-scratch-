# Compressing the size of image so that it affect positive in the image

import cv2

image = cv2.imread("cat.png")
# .jpg, .png uses the file extension i am interested to save
# image is the variable in memory i want to save
# 10 decide the quality of image[[ 100 - good quality, 70 - bit blurry, 10 - very blur]]
cv2.imwrite("compressed.jpg",
                               image,
                               [cv2.IMWRITE_JPEG_QUALITY, 10])
## read helps to load the file
compressed_image = cv2.imread("compressed.jpg")

print("The matrix of the original image", image)
print("The matrix of the new compressed image", compressed_image)

# visualizing and creating the difference between the images

# for original image
cv2.imshow("original", image)
cv2.moveWindow("original", 100, 100)

# for compresssed image
cv2.imshow("mac",compressed_image)
cv2.moveWindow("mac", 400, 400)
cv2.waitKey(0)
cv2.destroyAllWindows()



