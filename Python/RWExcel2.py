# 将文件夹下所有文件读取出来汇总成一个文件，并增加备注从哪个文件来的


import os
import pandas as pd

import openpyxl

from openpyxl import load_workbook
import xlwings as xw
import time
def combile_excels(aim_path, result_path):

    '''
    组合文件夹下，多个Excel到同一个文件

    :param aim_path:
    :return:
    '''
    # fd = open(result_path, mode="w", encoding="utf-8")
    # fd.close()
    #
    # df3 = pd.DataFrame()
    # df3.to_excel(result_path)

    book = load_workbook(result_path)
    writer = pd.ExcelWriter(result_path, engine='openpyxl')
    writer.book = book
    writer.sheets = dict((ws.title, ws) for ws in book.worksheets)

    line = 0

    paths = os.listdir(aim_path)
    for fl in paths:
        if fl == ".DS_Store":continue

        print(time.time())
        path = os.path.join(aim_path, fl)
        print("开始读取。。。。%s"%path)

        data = pd.read_excel(path)

        data["备注"] = fl.split('-')[0]


        print(time.time())
        print("开始读取。。。。%s行"%len(data))
        # if line == 0:
        #     data.to_excel(result_path,index=False);
        #     data["备注"] = fl
        #     line = line + len(data)
        #     print("第一个成功",)
        # else:

        data.to_excel(writer, sheet_name="Sheet1", startrow=line + 1, index=False, header=False)

        line = line + len(data)

    writer.save()
    # df3.to_excel(result_path)
    df4 = pd.read_excel(result_path)
    print(df4)

# aim_path = "/Users/will/Desktop/华住-员工综合学习情况"
aim_path = "/Users/will/Desktop/华住-员工综合学习情况"
result_path = "/Users/will/Desktop/result1.xlsx"
combile_excels(aim_path, result_path)


