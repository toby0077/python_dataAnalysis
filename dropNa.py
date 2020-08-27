# -*- coding: utf-8 -*-
"""
呆瓜半小时入门python数据分析：http://dwz.date/b62x
@author:231469242@qq.com
微信公众号：pythonEducation
"""
import pandas as pd
import numpy as np

df = pd.DataFrame({"name": ['Alfred', 'Batman', 'Catwoman'],
                   "toy": [np.nan, 'Batmobile', 'Bullwhip'],
                 "born": [pd.NaT, pd.Timestamp("1940-04-25"),
                           pd.NaT]})

#Drop the rows where at least one element is missing.
#至少有一个空缺值的行都会被删除
df.dropna()

#Drop the columns where at least one element is missing.
##至少有一个空缺值的列都会被删除
df.dropna(axis='columns')

#Drop the rows where all elements are missing.
#删除所有变量全为空的行
df.dropna(how='all')

#Keep only the rows with at least 2 non-NA values.
#删除至少有2个空缺值的行
df.dropna(thresh=2)

#Define in which columns to look for missing values.
#定义指定某列需要删除空缺值的行
df.dropna(subset=['born'])
#定义指定多列需要删除空缺值的行
df.dropna(subset=['name', 'born'])

df1=df.dropna(subset=['born'])