# Written by: Nick Gerend, @dataoutsider
# Viz: "Windows to the Soul", enjoy!

from math import pi, sin, cos
#import matplotlib.pyplot as plt

#region algorithm
x_o = 0.0
y_o = 0.0
count = 5000 
offset = 0.001 
golden_ratio = (1+5**0.5)/2.0 # golden_ratio approx = 1.618033989
angle_i = (2-golden_ratio)*2*pi + offset
angle = 0
k = 3.0
scale = 1e-10
x = []
y = []
for j in range(1,count+1):
    r = scale*j**k
    angle += angle_i
    x.append(x_o + r*cos(angle))
    y.append(y_o + r*sin(angle))
for j in range(1,count+1):
    r = scale*j**k
    angle += angle_i
    x.append(x_o + r*cos(-angle))
    y.append(y_o + r*sin(-angle))

path_list=[]
s=100./34.
item_list = []
color_list = []
path = 0
color = 0
for j in range(count*2):
    item_list.append((j%34.)*s)
    if item_list[j] == 0:
        path += 1
    path_list.append(path)
    color_list.append(color)
    if j == count-1:
        color = 1

# plt.scatter(x, y)
# plt.show()

#endregion

import csv
import os
with open(os.path.dirname(__file__) + '/dilines.csv', 'w',) as csvfile:
    writer = csv.writer(csvfile, lineterminator = '\n')
    writer.writerow(['x', 'y', 'path', 'item', 'color'])
    for i in range(len(x)):
        writer.writerow([x[i],y[i],path_list[i],item_list[i],color_list[i]])
print('finish')