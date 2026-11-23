# rotating the image
import cv2
import math
import numpy as np
theta = math.radians(45)
cos_theta = math.cos(theta)
sin_theta = math.sin(theta)
image =  cv2.imread("cat.png")
#rotated_matrix = [
 #   [cos_theta, -sin_theta],
  #  [sin_theta, cos_theta]
#]
matrix = np.array([
    [cos_theta, -sin_theta, 0],
    [sin_theta, cos_theta, 0]
])
height = image.shape[0]
width = image.shape[1]

# rotated matrix create the same to same space/memory like original image

rotated_images = np.zeros_like(image)
for y in range(height): # height = rows = x
    for x in range(width): # width = columns = y
        point = np.array([x,y,1])
        new_point = matrix @ point
        new_x = round(new_point[0])
        new_y = round(new_point[1])
        if 0 <= new_x < width and 0<= new_y < height:
            rotated_images[new_y,new_x] = image[y,x]

#print(rotated_matrix)
cv2.imshow("mac", rotated_images)
#cv2.imshow("mac",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

