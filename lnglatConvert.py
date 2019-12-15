# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 09:30:46 2019

@author: zx6186
"""

import os
import csv
import coordTransform_utils
import pandas as pd
f_orig = open('lnglat.csv', 'r', encoding='gbk')

da = pd.read_csv(f_orig)
f_new = 'Wgslnglat.csv'
with open(f_new, 'w', newline='') as f:
    # writer=csv.writer(f)与下面一行等价，delimiter默认是逗号
    writer = csv.writer(f, delimiter=',')

    # for row in img:
    #   writer.writerow(row)
    print(f_orig)
    for eachline in f_orig:
        try:
            # print("I am here")
            eachline = eachline.split(',')
            print(eachline)
            # 需要改一下经纬度顺序 和转换的坐标系
            result = coordTransform_utils.bd09_to_wgs84(float(eachline[0]), float(eachline[1]))

        # result.extend(eachline.split(',')[0],eachline.split(',')[1],eachline.split(',')[2])
        except BaseException:
            result = [0, 0]
            print("There is BaseException")

        writer.writerow(eachline + result)
