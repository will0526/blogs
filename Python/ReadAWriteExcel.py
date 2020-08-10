import xlrd
import xlsxwriter
import os
import pandas as pd
# import DataFrame


#打开一个excel文件
def open_xls(file):
    if path.endswith(".xlsx"):
        f = xlrd.open_workbook(file)
        return f
    else:
        return None



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


paths = os.listdir("/Users/will/Desktop/归档/test")

line = 0

df3 = pd.read_excel("/Users/will/Desktop/归档/test.xlsx")
for fl in paths:
    if fl == ".DS_Store":continue

    path = os.path.join("/Users/will/Desktop/归档/test", fl)
    print("开始读取。。。。%s"%path)
    data = pd.read_excel(path)  # 这个会直接默认读取到这个Excel的第一个表单
    data2 = data.drop(index=[0], axis=0)

    df3 = df3.append(data,ignore_index=True)
    print("result有多少行呢%s"%len(df3))
    line = line + len(data)
    # df2.to_excel("/Users/will/Desktop/归档/test.xlsx")

df3.to_excel("/Users/will/Desktop/归档/test1.xlsx")
df3 = pd.read_excel("/Users/will/Desktop/归档/test1.xlsx")

print("总共多少行df%s"%len(df3))
print("总共多少行%s"%line)
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





