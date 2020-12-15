import xlrd
import xlsxwriter
import os
import pandas as pd
# import DataFrame

# paths = os.listdir("/Users/will/Desktop/归档/test")


#打开一个excel文件
# def open_xls(file):
#     if path.endswith(".xlsx"):
#         f = xlrd.open_workbook(file)
#         return f
#     else:
#         return None



#获取excel中所有的sheet表
def getsheet(f):
    return f.sheets()


#获取sheet表的行数
def get_Allrows(f,sheet):
    table=f.sheets()[sheet]
    return table.nrows


#读取文件内容并返回行内容
def getFile(file):
    print("开始读取%s"%file)
    df = pd.read_excel(file)  # 这个会直接默认读取到这个Excel的第一个表单
    data2 = df.drop(index=[0],axis=0)
    return data2


#获取sheet表的个数
def getshnum(f):
    x=0
    sh=getsheet(f)
    for sheet in sh:
        x+=1
    return x

#读取各sheet,合并成一个sheet

def combile_sheet():

    import time
    ticks = time.time()
    print("当前时间戳为:", ticks)
    ex = pd.ExcelFile("/Users/will/Desktop/华住各平台全员名单导出.xlsx")
    sheet_names = ex.sheet_names

    df = None
    for sheet_name in sheet_names:
        if df is None:
            df = pd.read_excel("/Users/will/Desktop/华住各平台全员名单导出.xlsx",sheet_name=sheet_name)
            df = df.drop(index=[0], axis=0)
            continue
        else:
            temp = pd.read_excel("/Users/will/Desktop/华住各平台全员名单导出.xlsx",sheet_name=sheet_name)
            temp2 = temp.drop(index=[0], axis=0)
            print("sheet多少行df%s"%len(temp2))
            df = df.append(temp2, ignore_index=True)

    df.to_excel("/Users/will/Desktop/result.xlsx")
    print(df)


    print("总共多少行df%s"%len(df))
    ticks2 = time.time()
    print("当前时间戳为:", ticks2-ticks)



def combile_sheet2():

    file_path = "/Users/will/Desktop/result_test.xlsx"
    nan_excle = pd.DataFrame()

    nan_excle.to_excel(file_path)
    # 打开excel
    writer = pd.ExcelWriter(file_path)

    import time
    ticks = time.time()
    ex = pd.ExcelFile("/Users/will/Desktop/华住各平台全员名单导出.xlsx")
    sheet_names = ex.sheet_names

    for sheet in sheet_names:
        print(sheet)
        df = pd.read_excel("/Users/will/Desktop/华住各平台全员名单导出.xlsx", sheet_name=sheet)
        df.to_excel(writer, sheet_name="总和")

    writer.save()

    ticks2 = time.time()
    print("总共时间为:", ticks2-ticks)

combile_sheet2()
#
# paths = os.listdir("/Users/will/Desktop/test1")
# #
# line = 0
# #
# df3 = pd.read_excel("/Users/will/Desktop/城家.xlsx")
#
# for fl in paths:
#     if fl == ".DS_Store":continue
#
#     path = os.path.join("/Users/will/Desktop/test1", fl)
#     print("开始读取。。。。%s"%path)
#     data = pd.read_excel(path)  # 这个会直接默认读取到这个Excel的第一个表单
#     data2 = data.drop(index=[0], axis=0)
#
#     df3 = pd.concat([df3,data2],ignore_index=False)
#     print("result有多少行呢%s"%len(df3))
#     line = line + len(data)
#     # df2.to_excel("/Users/will/Desktop/归档/test.xlsx")
#
# df3.to_excel("/Users/will/Desktop/test1.xlsx")
# df4 = pd.read_excel("/Users/will/Desktop/test1.xlsx")
# print(df4)
#
# print("总共多少行df%s"%len(df3))
# print("总共多少行%s"%line)
    # return
#
#     if f :
#         x=getshnum(f)
#         for shnum in range(x):
#             print("正在读取文件："+str(path)+"的第"+str(shnum)+"个sheet表的内容...")
#             getFile(path, shnum)
#             datavalue.extend(getFile(path, shnum))
# #定义最终合并后生成的新文件
# endfile='/Users/will/Desktop/归档/endFile.xlsx'
# wb= xlsxwriter.Workbook(endfile)
# #创建一个sheet工作对象
# ws=wb.add_worksheet()
# i = 1
# for a in range(len(datavalue)):
#     i = i + 1
#     for b in range(len(datavalue[a])):
#         c=datavalue[a][b]
#         if c and len(c)>0:
#             ws.write(a,b,c)
#
# wb.close()
#
# print("文件合并完成，总共%s行"%i)
#
# def read_excel(file_path):
#     wb = xlrd.open_workbook(file_path)# 打开Excel文件
#     sheet = wb.sheet_by_index(0)#通过excel表格名称(rank)获取工作表
#     dat = []  #创建空list
#     for a in range(sheet.nrows):  #循环读取表格内容（每次读取一行数据）
#         if a == 0 or a == 1:continue
#         cells = sheet.row_values(a)  # 每行数据赋值给cells
#         # data=cells[0]#因为表内可能存在多列数据，0代表第一列数据，1代表第二列，以此类推
#         dat.append(cells) #把每次循环读取的数据插入到list
#     return dat


# # paths = os.listdir("/Users/will/Desktop/归档/")
# # data = []
# # for file in paths:
# #     path = os.path.join("/Users/will/Desktop/归档/", file)
# #     file_data = read_excel(path)
# #     data.append(file_data)
#
# data = read_excel("/Users/will/Desktop/归档/test2.xlsx")
# writebook = xlwt.Workbook()#打开一个excel
# sheet = writebook.add_sheet('test')#在打开的excel中添加一个sheet
#
# for a in range(len(rvalue)):
#     for b in range(len(rvalue[a])):
#         c = rvalue[a][b]
#         ws.write(a, b, c)
#
#
# writebook.save('answer.xlsx')

#
# df3 = pd.read_excel("/Users/will/Desktop/test1/test2/城家.csv")
# df2 = pd.read_excel("/Users/will/Desktop/test1/test2/城家的副本.xlsx")
# df3 = pd.concat([df3, df2], ignore_index=True)
#
# print(df3)


