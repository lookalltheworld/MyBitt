import xlwt

#设置表格样式
def set_style(name,height,bold=False):
    style=xlwt.XFStyle()
    font= xlwt.Font()
    font.name=name
    font.bold=bold
    font.color_index=4
    font.height=height
    style.font=font
    return style

#写Excel
def write_excel():
    f=xlwt.Workbook()
    sheet1=f.add_sheet('学生',cell_overwrite_ok=True)
    row0=['姓名','年龄','出生日期','爱好']
    colum0=["张三","李四","恋习Python","小明","小红","无名"]
    #写第一行
    for i in range(0,len(row0)):
        sheet1.write(0,i,row0[i],set_style('Time New Roman',220,True))
    #写第一列
    for i in range(0,len(colum0)):
        sheet1.write(i+1,0,colum0[i])
    sheet1.write(1, 3, '2006/12/12')
    sheet1.write_merge(6, 6, 1, 3, '未知')  # 合并行单元格
    sheet1.write_merge(1, 2, 3, 3, '打游戏')  # 合并列单元格
    sheet1.write_merge(4, 5, 3, 3, '打篮球')
    f.save('test4.xlsx')
import xlrd
from datetime import date,datetime



def read_excel(file):

    #wb=xlrd.open_workbook(filename=file)#打开文件
    #print(wb.sheet_names())#获取所有表
    #sheet1=wb.sheet_by_index(0)#通过索引获取表格
    #sheet2=wb.sheet_by_name('年级')#通过名字获取表格
    #print(sheet1,sheet2)
    #print(sheet1.name,sheet1.nrows,sheet1.ncols)
    #rows=sheet1.row_values(2)  #获取行内容
    #cols=sheet1.col_values(3)#获取列内容
    #print(rows)
    #print(cols)
    #print(sheet1.cell(1,0).value)#获取表格里的内容，三种方式
    #print(sheet1.cell_value(1,0))
    #print(sheet1.row(1)[0].value)
    f=xlrd.open_workbook(file)
    sheet1=f.sheet_by_index(0)
    dict_1={}
    for i in range(sheet1.nrows):
        row=sheet1.row_values(i)
        #print(row)
        if row[0]=='' or row[0][0]=='#':
            continue
        key=row[0]
        value=row[1]
        dict_1[key]=value
    return dict_1
def read_excel_list(file):

    #wb=xlrd.open_workbook(filename=file)#打开文件
    #print(wb.sheet_names())#获取所有表
    #sheet1=wb.sheet_by_index(0)#通过索引获取表格
    #sheet2=wb.sheet_by_name('年级')#通过名字获取表格
    #print(sheet1,sheet2)
    #print(sheet1.name,sheet1.nrows,sheet1.ncols)
    #rows=sheet1.row_values(2)  #获取行内容
    #cols=sheet1.col_values(3)#获取列内容
    #print(rows)
    #print(cols)
    #print(sheet1.cell(1,0).value)#获取表格里的内容，三种方式
    #print(sheet1.cell_value(1,0))
    #print(sheet1.row(1)[0].value)
    f=xlrd.open_workbook(file)
    sheet1=f.sheet_by_index(0)
    list1=[]
    for i in range(sheet1.nrows):
        row=sheet1.row_values(i)
        if row[0]=='' : #or row[0][0]=='#':
           continue
        list1.append(row)



    return list1



if __name__ == '__main__':
    #write_excel()
    #d=read_excel('../test_data/element.xlsx')
    #print(d)
    e = read_excel_list('../test_data/createWallet.xlsx')
    print(e)
