
# Excel文件加载
# # python2.7
# pip install xlrd  
# pip install xlwt
# # python 3.*
# pip3 install xlrd
# pip3 install xlwt

import os
from pathlib import Path
import csv

import xlrd
import xlwt

import numpy as np

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def read_excel( fileName, winderId ):
    """
    获取风机数据
        fileName Excel文件名
        winderId 风机号
    """
    
    # 判断文件是否存在
    if os.path.exists(fileName):
        pass
    else:
        return None, None, None, None
    

    # 打开execl
    #print(fileName)
    workbook = xlrd.open_workbook(fileName)

    # 输出Excel文件中所有sheet的名字
    sheetNames = workbook.sheet_names()
    #print(sheetNames)

    #if winderId not in sheetNames:
    #    return None, None

    # 根据sheet索引或者名称获取sheet内容
    #Data_sheet = workbook.sheet_by_name( winderId )  # 通过名称获取
    Data_sheet = workbook.sheet_by_index( 0 ) #通过索引

    #print(Data_sheet.name)  # 获取sheet名称
    rowNum = Data_sheet.nrows  # sheet行数
    colNum = Data_sheet.ncols  # sheet列数

    # 获取所有单元格的内容
    rowCountentList = []
    rowBaddataList = []

    labelList = Data_sheet.row_values(0)

    for i in range(1, rowNum):
        #rowlist = []
        #for j in range(colNum):
        #    rowlist.append(Data_sheet.cell_value(i, j))
        rowlist = Data_sheet.row_values(i)

        if float(rowlist[23]) < 0.0001:
            rowBaddataList.append( rowlist )
        else :
            rowCountentList.append(rowlist)

    return rowCountentList, rowBaddataList, labelList, colNum

def show_figure( xArr, xLabel, yArr, yLabel ):
    """
    绘制图形
    """

    '''
    plt.subplot(311)
    plt.plot( xArr[:10000], yArr[:10000],  'ro')

    plt.subplot(312)
    plt.plot( xArr[10000:20000], yArr[10000:20000], 'go')

    plt.subplot(313)
    plt.plot( xArr[20000:30000], yArr[20000:30000], 'bo' )
    '''
    
    #plt.plot( xArr[:10000], yArr[:10000],  'r-', xArr[10000:20000], yArr[10000:20000], 'g-' , xArr[20000:30000], yArr[20000:30000], 'b-' )

    plt.plot(xArr, yArr, 'bo')
    plt.xlabel( xLabel )
    plt.ylabel( yLabel )

    plt.show()

def descript_label():
    '''
    00:'系统时间'
    01:'NCC300温度[°C]'
    02:'NCC320温度[°C]'
    03:'机侧电感温度[°C]'
    04:'网侧电感温度[°C]'
    05:'机侧半导体温度[°C]'
    06:'网侧半导体温度[°C]'
    07:'驱动链摆动幅度[%]'
    08:'环境温度[°C]'
    09:'最大故障电流[A]'
    10:'滤波板温度[°C]'
    11:'齿轮箱轴承温度[°C]'
    12:'齿轮箱油温[°C]'
    13:'驱动方向发电机轴承温度[°C]'
    14:'非驱动方向发电机轴承温度[°C]'
    15:'最大发电机绕组温度[°C]'
    16:'变浆电机1温度[°C]'
    17:'变浆电机2温度[°C]'
    18:'变浆电机3温度[°C]'
    19:'变浆电机1扭矩[Nm]'
    20:'变浆电机2扭矩[Nm]'
    21:'变浆电机3扭矩[Nm]'
    22:'机舱内温度[°C]'
    23:'有功功率[kW]'
    24:'无功功率[kVAr]'
    25:'机舱电池温度[°C]'
    26:'驱动方向塔筒摆动幅度[%]'
    27:'非驱动方向塔筒摆动幅度[%]'
    28:'1秒平均风速[m/s]'
    29:'最大偏航功率[kW]'
    30:'叶片1角度[°]'
    31:'叶片1最大角度[°]'
    32:'发电机平均转速[rpm]'
    33:'发电机最小转速[rpm]'
    34:'发电机最大转速[rpm]'
    35:'控制用发电机平均转速[rpm]'
    36:'控制用发电机最小转速[rpm]'
    37:'控制用发电机最大转速[rpm]'
    38:''
    '''
    #labelList = np.array( labels )  

def test_one_excel():
    winderId = "2"
    fileName = "/Users/wangyujie/Temp/七里嘎2.xls"

    rowCountentList, rowBaddataList, labels, colNum = read_excel( fileName, winderId )

    #labels
    labelList = np.array( labels ) 

    #data
    system_times = []
    dataList = []  #不含time

    for row in rowCountentList:
        system_times.append( row[0] )
        dataList.append( row[1:] )
    
    dataList = np.array( dataList )
    

    # 取某列 3列
    ncc300 = dataList[:, 0]
    ncc320 = dataList[:, 1]

    dataColList = []
    for i in range(colNum-1) :
        cols = dataList[:, i]
        dataColList.append( cols )

    #dataListT = np.mat(dataList).T
    xArr = dataColList[27]  #风速
    yArr = dataColList[22]  #有功功率

    xLabel = labelList[27+1]
    yLabel = labelList[22+1]

    show_figure( xArr, xLabel, yArr, yLabel )

    print("ok")



if __name__ == "__main__":

    test_one_excel()
    