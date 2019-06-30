
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


def read_excels( fileNames, winderId ):
    """
    读取文件列表fileNames，归档winderId数据
    """
    rowCountentList = []
    for fileName in fileNames:
        rowCountentOne = read_excel( fileName, winderId )
        if None != rowCountentOne:
            #for rowlist in rowCountentOne :
            #    rowCountentList.append(rowlist)
            rowCountentList.extend( rowCountentOne )

    return rowCountentList

def read_excel_row( fileName, winderId ):
    """
    获取风机数据
        fileName Excel文件名
        winderId 风机号
    """
    
    # 判断文件是否存在
    if os.path.exists(fileName):
        pass
    else:
        return None
    

    # 打开execl
    print(fileName)
    workbook = xlrd.open_workbook(fileName)

    # 输出Excel文件中所有sheet的名字
    sheetNames = workbook.sheet_names()
    print(sheetNames)

    if winderId not in sheetNames:
        return None

    # 根据sheet索引或者名称获取sheet内容
    Data_sheet = workbook.sheet_by_name( winderId )  # 通过名称获取

    #print(Data_sheet.name)  # 获取sheet名称
    rowNum = Data_sheet.nrows  # sheet行数
    #colNum = Data_sheet.ncols  # sheet列数

    # 获取所有单元格的内容
    rowCountentList = []

    for i in range(1, rowNum):
        row = Data_sheet.row_values(i)
        print(row)
        rowCountentList.append(row)

    return rowCountentList

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
        return None
    

    # 打开execl
    print(fileName)
    workbook = xlrd.open_workbook(fileName)

    # 输出Excel文件中所有sheet的名字
    sheetNames = workbook.sheet_names()
    print(sheetNames)

    if winderId not in sheetNames:
        return None

    # 根据sheet索引或者名称获取sheet内容
    Data_sheet = workbook.sheet_by_name( winderId )  # 通过名称获取

    #print(Data_sheet.name)  # 获取sheet名称
    rowNum = Data_sheet.nrows  # sheet行数
    colNum = Data_sheet.ncols  # sheet列数

    # 获取所有单元格的内容
    rowCountentList = []

    for i in range(1, rowNum):
        rowlist = []
        for j in range(colNum):
            rowlist.append(Data_sheet.cell_value(i, j))
        rowCountentList.append(rowlist)

    return rowCountentList


def write_excel(filename, winderId, rowCountentList ):
    """
    将内容写入文件
        filename:   要写入的文件名
        winderId:   风机号
        rowCountentList: 需要写入的内容
    """
    # 创建工作簿
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建sheet
    data_sheet = workbook.add_sheet(winderId)

    
    # 生成行与列
    try:
        for i in range( len(rowCountentList) ):
            rowlist = rowCountentList[i]
            for j in range(len(rowlist)):
                data_sheet.write(i, j, (rowlist[j]) )
    except:
        pass
    
    # 保存文件
    workbook.save(filename)

def write_csv(filename, winderId, rowCountentList ):
    """
    将内容写入文件
        filename:   要写入的文件名
        winderId:   风机号
        rowCountentList: 需要写入的内容
    """
    with open( filename, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        
        for i in range( len(rowCountentList) ):
            rowlist = rowCountentList[i]
            spamwriter.writerow( rowlist )


def file_names():
    """
    返回文件数组
    """
    winderId = "2"

    fileNames = []
    fileNames.append('/Users/wangyujie/Downloads/2017七里嘎1-12月份十分钟数据/七里嘎1月十分钟数据.xls')
    fileNames.append('/Users/wangyujie/Downloads/2017七里嘎1-12月份十分钟数据/七里嘎2月十分钟数据.xls')
    fileNames.append('/Users/wangyujie/Downloads/2017七里嘎1-12月份十分钟数据/七里嘎3月十分钟数据.xls')
    fileNames.append('/Users/wangyujie/Downloads/2017七里嘎1-12月份十分钟数据/七里嘎4月十分钟数据.xls')
    fileNames.append('/Users/wangyujie/Downloads/2017七里嘎1-12月份十分钟数据/七里嘎5月十分钟数据.xls')
    fileNames.append('/Users/wangyujie/Downloads/2017七里嘎1-12月份十分钟数据/七里嘎6月十分钟数据.xls')
    fileNames.append('/Users/wangyujie/Downloads/2017七里嘎1-12月份十分钟数据/七里嘎7月十分钟数据.xls')
    fileNames.append('/Users/wangyujie/Downloads/2017七里嘎1-12月份十分钟数据/七里嘎8月十分钟数据.xls')
    fileNames.append('/Users/wangyujie/Downloads/2017七里嘎1-12月份十分钟数据/七里嘎9月十分钟数据.xls')
    fileNames.append('/Users/wangyujie/Downloads/2017七里嘎1-12月份十分钟数据/七里嘎10月十分钟数据.xls')
    fileNames.append('/Users/wangyujie/Downloads/2017七里嘎1-12月份十分钟数据/七里嘎11月十分钟数据.xls')
    fileNames.append('/Users/wangyujie/Downloads/2017七里嘎1-12月份十分钟数据/七里嘎12月十分钟数据.xls')

    fileNames.append('/Users/wangyujie/Downloads/2018七里嘎十分钟数据/2018年1月七里嘎.xls')
    fileNames.append('/Users/wangyujie/Downloads/2018七里嘎十分钟数据/2018年2-3月七里嘎.xls')
    fileNames.append('/Users/wangyujie/Downloads/2018七里嘎十分钟数据/2018年4-5月七里嘎.xls')
    fileNames.append('/Users/wangyujie/Downloads/2018七里嘎十分钟数据/2018年6月份七里嘎.xls')
    fileNames.append('/Users/wangyujie/Downloads/2018七里嘎十分钟数据/七里嘎2018年7-8月十分钟数据.xls')
    fileNames.append('/Users/wangyujie/Downloads/2018七里嘎十分钟数据/七里嘎2018年9-10月十分钟数据.xls')
    fileNames.append('/Users/wangyujie/Downloads/2018七里嘎十分钟数据/七里嘎2018年11月十分钟数据.xls')
    fileNames.append('/Users/wangyujie/Downloads/2018七里嘎十分钟数据/七里嘎2018年12月十分钟数据.xls')
    

    return fileNames, winderId

def test_all_excel():
    fileNames, winderId = file_names()

    rowCountentList = read_excels( fileNames, winderId )

    destname = '/Users/wangyujie/Downloads/七里嘎'+winderId+".xls"
    write_excel( destname, winderId, rowCountentList)

    print("ok")


def test_one_excel():
    fileNames, winderId = file_names()

    rowCountentList = read_excel_row( fileNames[0], winderId )

    destname = '/Users/wangyujie/Downloads/七里嘎'+winderId+".xls"
    write_excel( destname, winderId, rowCountentList)

    print("ok")

def test_one_csv():
    fileNames, winderId = file_names()

    rowCountentList = read_excel_row( fileNames[0], winderId )

    destname = '/Users/wangyujie/Downloads/七里嘎'+winderId+".csv"
    write_csv( destname, winderId, rowCountentList)

    print("ok")

if __name__ == '__main__':
    test_all_excel()
    #test_one_excel()
    #test_one_csv()

    
    