import xlrd
import xlsxwriter
import os



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
def getFile(file,shnum):
    f=open_xls(file)
    table=f.sheets()[shnum]
    num=table.nrows
    filecontent=[]
    for row in range(num):
        if row == 0 or row ==1:continue

        rdata=table.row_values(row)
        filecontent.append(rdata)
    return filecontent


#获取sheet表的个数
def getshnum(f):
    x=0
    sh=getsheet(f)
    for sheet in sh:
        x+=1
    return x


paths = os.listdir("/Users/will/Desktop/归档/")
datavalue=[]
for fl in paths:
    path = os.path.join("/Users/will/Desktop/归档/", fl)
    f=open_xls(path)
    if f :
        x=getshnum(f)
        for shnum in range(x):
            print("正在读取文件："+str(path)+"的第"+str(shnum)+"个sheet表的内容...")
            datavalue.extend(getFile(path, shnum))
#定义最终合并后生成的新文件
endfile='/Users/will/Desktop/归档/endFile.xlsx'
wb= xlsxwriter.Workbook(endfile)
#创建一个sheet工作对象
ws=wb.add_worksheet()
i = 1
for a in range(len(datavalue)):
    i = i + 1
    for b in range(len(datavalue[a])):
        c=datavalue[a][b]
        if c and len(c)>0:
            ws.write(a,b,c)

wb.close()

print("文件合并完成，总共%s行"%i)

def read_excel(file_path):
    wb = xlrd.open_workbook(file_path)# 打开Excel文件
    sheet = wb.sheet_by_index(0)#通过excel表格名称(rank)获取工作表
    dat = []  #创建空list
    for a in range(sheet.nrows):  #循环读取表格内容（每次读取一行数据）
        if a == 0 or a == 1:continue
        cells = sheet.row_values(a)  # 每行数据赋值给cells
        # data=cells[0]#因为表内可能存在多列数据，0代表第一列数据，1代表第二列，以此类推
        dat.append(cells) #把每次循环读取的数据插入到list
    return dat


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





