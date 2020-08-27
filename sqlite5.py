# -*- coding: utf-8 -*-
'''
呆瓜半小时入门python数据分析：http://dwz.date/b62x
@author:231469242@qq.com
微信公众号：pythonEducation
delete and update data
'''
import sqlite3
import time,datetime,random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')
#创建连接
#注意格式
#con=sqlite3.connect('c:/Users/Administrator/Desktop/python SQL/demo.db')
conn=sqlite3.connect('demo1.db')
print(conn)
#创建游标对象
c=conn.cursor()
#删除表格
def delete_table(table_name):
    sql='''drop table if exists '''
    sql+=table_name
    c.execute(sql)

#创建表格
def create_table():
    sql='''CREATE TABLE IF NOT EXISTS table1(
                            unix REAl,
                            datestamp TEXT,
                            keyword TEXT,
                            value REAL)'''
    c.execute(sql)
    
#输入数据
def data_entry():
    sql='''INSERT INTO table1 VALUES(123456,'2016-01-01','python',5)'''
    sql1='''INSERT INTO table1 VALUES(123457,'2016-01-01','python',9)'''
    c.execute(sql)
    c.execute(sql1)
    conn.commit()

    
def dynamic_data_entry():
    unix=time.time()
    #Y年M月d日H小时M分钟S秒钟
    date=str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword='python'
    value=random.randrange(0,10)
    c.execute("INSERT INTO table1(unix,datestamp,keyword,value) VALUES(?,?,?,?)",
              (unix,date,keyword,value))
    conn.commit()
    
def read_from_db():
    sql='select * from table1;'
    sql1='select * from table1 where value=4;'
    sql2="select * from table1 where value=4 and keyword='python';"
    sql3="select datestamp,keyword,value from table1 where value=4 and keyword='python';"
    #c.execute(sql)
    c.execute(sql3)
    data=c.fetchall()
    print(data)
    return data

def graph_data():
    c.execute('select unix,value from table1;')
    data=c.fetchall()
    dates=[]
    values=[]
    for row in data:
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])
    #绘制时间，数据的函数plot_date
    plt.plot_date(dates,values,'-')
    plt.show()

#更新数据
def update():
    c.execute('select * from table1;')
    c.execute('update table1 set value=22 where value=2')
    conn.commit()

#删除数据
def delete():
    c.execute('delete from table1 where value=8;')
    conn.commit()
    
    
#删除表格
#delete_table("table1")
#创建表格
#create_table()
#输入多条数据
#for i in range(10):
#    dynamic_data_entry()
#    time.sleep(1)

#data=read_from_db()
update()   
#delete() 
c.close()
conn.close()













