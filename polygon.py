# Written by: Nick Gerend, @dataoutsider
# Viz: "Windows to the Soul", enjoy!

import numpy as np 
import cv2
import os

#region prepare
# load image 
img2 = cv2.imread(os.path.dirname(__file__) + '/polygon.jpg', cv2.IMREAD_COLOR) 
   
# duplicate to gray scale
img = cv2.imread(os.path.dirname(__file__) + '/polygon.jpg', cv2.IMREAD_GRAYSCALE) 
   
# image to black and white 
_,threshold = cv2.threshold(img, 75, 255, cv2.THRESH_BINARY) 
   
# detect shapes 
contours,_ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#endregion

#region polygon algorithm
# find polygons within regions
cx = []
cy = []
poly = []
ellipse = []
for cnt in contours : 
    area = cv2.contourArea(cnt) 
   
    # filter regions based on there area
    if area >= 100 and area <= 100000:  
        polygon = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True) 
   
        # check if the number of sides 
        if(len(polygon) >= 4)and(len(polygon) <= 100):  
            cv2.drawContours(img2, [polygon], 0, (0, 0, 255), 5)
            #M = cv2.moments(cnt)
            M = cv2.moments(polygon)
            cx.append(M['m10']/M['m00'])
            cy.append(M['m01']/M['m00'])
            poly.append(polygon)
            e = cv2.fitEllipse(cnt)
            ellipse.append(e)
   
# # Showing the image along with outlined arrow. 
# img2 = cv2.resize(img2, (900, 900))
# cv2.imshow('image2', img2)  
   
# # Exiting the window if 'q' is pressed on the keyboard. 
# if cv2.waitKey(0) & 0xFF == ord('q'):  
#     cv2.destroyAllWindows()
#endregion

#region ellipse algorithm
path = 1
it = 1
import csv
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.path import Path
from matplotlib.patches import PathPatch
# with open(os.path.dirname(__file__) + '/ellipse.csv', 'w',) as csvfile:
#     writer = csv.writer(csvfile, lineterminator = '\n')
#     writer.writerow(['x', 'y', 'path', 'item'])
#     for e in ellipse:
#         xc = e[0][0]
#         yc = e[0][1]
#         w = e[1][0]
#         h = e[1][1]
#         angle = e[2]
#         a = w/2.
#         b = h/2.
#         theta = angle * np.pi/180.

#         # Create the base ellipse
#         ellipse = Ellipse((xc, yc), width=w*0.5, height=h*0.5, angle=angle)
#         pathe = ellipse.get_path()
#         vertices = pathe.vertices.copy()
#         vertices = ellipse.get_patch_transform().transform(vertices)

#         for i in range(len(vertices)):
#             writer.writerow([vertices[i][0],vertices[i][1],path,it])
#             path += 1

#         path = 1
#         it += 1
#endregion

#region output
it = 1
with open(os.path.dirname(__file__) + '/polygons.csv', 'w',) as csvfile:
    writer = csv.writer(csvfile, lineterminator = '\n')
    writer.writerow(['x', 'y', 'path', 'item'])
    for polygon in poly:
        for j in polygon:
            writer.writerow([j[0][0],j[0][1],path,it])
            path += 1
        path = 1
        it += 1
it = 1
with open(os.path.dirname(__file__) + '/centroids.csv', 'w',) as csvfile:
    writer = csv.writer(csvfile, lineterminator = '\n')
    writer.writerow(['x', 'y', 'item'])
    for i in range(len(cx)):
        writer.writerow([cx[i],cy[i],it])
        it += 1
#endregion

print('finish')