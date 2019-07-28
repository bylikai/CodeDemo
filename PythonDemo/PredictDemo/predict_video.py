# 1. Required Packages
import csv
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model

# flash_episode_number,flash_us_viewers,arrow_episode_number,arrow_us_viewers
# 1,    4.83,   1,  2.84
# 2,    4.27,   2,  2.32
# 3,    3.59,   3,  2.55
# 4,    3.53,   4,  2.49
# 5,    3.46,   5,  2.73
# 6,    3.73,   6,  2.6
# 7,    3.47,   7,  2.64
# 8,    4.34,   8,  3.92
# 9,    4.66,   9,  3.06

# 2. Function to get data
def get_data(file_name):
    data = pd.read_csv(file_name)
    flash_x_parameter = []
    flash_y_parameter = []
    arrow_x_parameter = []
    arrow_y_parameter = []
    for x1, y1, x2, y2 in zip(
        data['flash_episode_number'], 
        data['flash_us_viewers'], 
        data['arrow_episode_number'], 
        data['arrow_us_viewers'] ):

        flash_x_parameter.append([float(x1)])
        flash_y_parameter.append(float(y1))
        arrow_x_parameter.append([float(x2)])
        arrow_y_parameter.append(float(y2))

    return flash_x_parameter, flash_y_parameter, arrow_x_parameter, arrow_y_parameter

# 3. Function to know which Tv show will have more viewers
def more_viewers(x1, y1, x2, y2):
    regr1 = linear_model.LinearRegression()
    regr1.fit(x1, y1)
    predicted_value1 = regr1.predict(9)
    print(predicted_value1)

    regr2 = linear_model.LinearRegression()
    regr2.fit(x2, y2)
    predicted_value2 = regr2.predict(9)
    print(predicted_value2)

    if predicted_value1 > predicted_value2:
        print("The Flash Tv Show will have more viewers for next week")
    else:
        print("Arrow Tv Show will have more viewers for next week")


def main():
    x1, y1, x2, y2 = get_data('video_data.csv')
    # print x1,y1,x2,y2
    more_viewers(x1, y1, x2, y2)

if __name__ == '__main__':
    main()

