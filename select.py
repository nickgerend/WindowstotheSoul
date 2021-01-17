# Written by: Nick Gerend, @dataoutsider
# Viz: "Windows to the Soul", enjoy!

import pandas as pd
import os

#region selection layer (combine charts)
df_lines = pd.read_csv(os.path.dirname(__file__) + '/dilines.csv')
df_points = pd.read_csv(os.path.dirname(__file__) + '/centroids.csv')

lines_x_min = -7.
lines_x_max = 7.
lines_y_min = -9.5
lines_y_max = 4.5
df_lines['x'] = (df_lines['x']-(lines_x_min))/(lines_x_max-lines_x_min)
df_lines['y'] = (df_lines['y']-(lines_y_min))/(lines_y_max-lines_y_min)

points_x_min = 0.
points_x_max = 1864.
points_y_min = 0.
points_y_max = 1867.
df_points['x'] = (df_points['x']-(points_x_min))/(points_x_max-points_x_min)
df_points['y'] = 1.-(df_points['y']-(points_y_min))/(points_y_max-points_y_min)


df_lines['type'] = 'lines'
df_points['type'] = 'points'

dfs = [df_lines, df_points]
df_combined = pd.concat(dfs)
print(df_combined)
#endregion

df_combined.to_csv(os.path.dirname(__file__) + '/select.csv', encoding='utf-8', index=False)