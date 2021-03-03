# 将文件读取出来后，按照45行一个文件进行拆分

import os
import pandas as pd

def splitExcel(file_path):

    data = pd.read_excel(file_path)

    data_header = data.head(3)

    num = 0
    body_num = len(data)
    if body_num%45:
        num = body_num/45+1
    else:
        num = body_num/45
    first = 3
    last = first+45

    for i in range(0, int(num)):

        last = last if last< body_num else body_num+1

        df = data.iloc[first:last]

        df = pd.concat([data_header, df], ignore_index=False)

        path = './result%s'%i+'.xlsx'
        fd = open(path, mode="w", encoding="utf-8")
        fd.close()

        df.to_excel(path,index=False)

        first = first + 45
        last = first+45


splitExcel("./data3.xls")

