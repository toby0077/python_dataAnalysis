# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 16:33:09 2020

呆瓜半小时入门python数据分析：http://dwz.date/b62x
@author:231469242@qq.com
微信公众号：pythonEducation
lambda 匿名函数
"""
#单一参数，多参数lambda

#数学函数应用
#写一个函数计算 3X+1
#传统函数
def f(x):
    return 3*x+1
    
f(2)

#lambda
g=lambda x: 3*x+1

#一元二次函数
def build_quadratic_function(a,b,c):
    """returns the function f(x)=a*x^2+b*x+c"""
    return lambda x: a*x**2+b*x+c

f=build_quadratic_function(2,3,-5)
f(0)
f(1)
f(2)

#evaluated for x=2,不太常用
f=build_quadratic_function(3,0,1)(2)

#几何平均数
f=lambda x,y:(x*y)**0.5
#harmonic mean
f=lambda x,y,z: 3/(1/x+1/y+1/z) 

#多参数lambda
#邮件字符串输入规范函数
#str2 = "   Runoob      ";   # 去除首尾空格
#print str2.strip();
#title() 方法返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写
full_name=lambda firstName,lastName: firstName.strip().title()+" "+lastName.strip().title()
full_name("  toby","Green")  

#lambda 在sort排序，filter函数里使用非常流行
#sorting a list of tuples using lambda
list1=[('egg',5.25),('honey',9),('carrots',1.1),('peaches',2.45)]
list1.sort(key=lambda x: x[0])
list1.sort(key=lambda x: x[1])

#lambda可以实现复杂排序功能
#字符串最后一个字母排序，前提去除前后空格，然后小写，
scifi_authors=["Isaac Asimov"," Ray Bradbury ","Robert Heinlein"]
scifi_authors.sort(key=lambda name: name.strip(" ")[-1].lower())
'''
输出
['Robert Heinlein', 'Isaac Asimov', 'Ray Bradbury']
'''

#sorting a list of dictionaries using lambda
import pprint as pp
list1=[{'make':'Ford','model':'Focus','year':2013},{'make':'Tesla','model':'X','year':1998},
       {'make':'Mercedes','model':'C350E','year':2008}]
list2=sorted(list1,key=lambda x:x['year'])

pp.pprint(list2)

# lambda 在filter应用
list1=[1,2,3,4,5,6]
#筛选偶数
list2=list(filter(lambda x:x%2==0,list1))
list3=list(filter(lambda x:x%2==1,list1))
print(list2)
print(list3)

#筛选奇数
even=lambda x:x%2==0
list1=[1,2,3,4,5,6]
list2=list(filter(even,list1))

#筛选奇数,更规范写法
odds=lambda x:x%2==1
list1=[1,2,3,4,5,6]
list2=list(filter(odds,list1))



#lambda 常常和map函数连用
#python's map function applies the lambda to every element in the list
list1=[1,2,3,4,5,6]
square=lambda x:x**2
list2=list(map(square,list1))
'''
 [1, 4, 9, 16, 25, 36]
'''

#lambda常常和if语句连用 conditionals条件判断
# lambda args: a if boolean_expression else b
starts_with_j=lambda x: True if x.startswith("J") else False
print(starts_with_j('Joey'))

#lambda on DataTime objects
import datetime
now=datetime.datetime.now()
print(now)
year=lambda x:x.year
month=lambda x:x.month
day=lambda x:x.day
print(year(now))
month(now)
day(now)





