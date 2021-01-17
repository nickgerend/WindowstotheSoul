# Written by: Nick Gerend, @dataoutsider
# Viz: "Windows to the Soul", enjoy!

import numpy as np

eye_colors = ['brown', 'blue', 'hazel', 'amber', 'gray', 'green', 'red-violet', 'heterochromia']
probabilities = [0.745, 0.09, 0.05, 0.05, 0.03, 0.02, 0.009, 0.006]
sampling = np.random.choice(eye_colors, 1154, p=probabilities)

import csv
import os
with open(os.path.dirname(__file__) + '/eye_colors.csv', 'w',) as csvfile:
    writer = csv.writer(csvfile, lineterminator = '\n')
    writer.writerow(['item', 'color'])
    for i in range(len(sampling)):
        writer.writerow([i+1,sampling[i]])
print('finish')