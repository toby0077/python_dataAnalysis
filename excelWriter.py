# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 13:24:28 2019

呆瓜半小时入门python数据分析：http://dwz.date/b62x
@author:231469242@qq.com
微信公众号：pythonEducation
官网
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_excel.html
"""
import numpy as np
import pandas as pd

df1 = pd.DataFrame({"name": ['Alfred', 'Batman', 'Catwoman'],
                   "toy": [np.nan, 'Batmobile', 'Bullwhip'],
                 "born": [pd.NaT, pd.Timestamp("1940-04-25"),
                           pd.NaT]})

df2 = pd.DataFrame({"name": ['Alfred', 'Jim', 'Catwoman'],
                   "toy": [np.nan, 'Batmobile', 'Bullwhip'],
                 "born": ['Greens',pd.Timestamp("1940-04-25"),
                           pd.NaT]})

with pd.ExcelWriter('result1.xlsx') as writer:
    df1.to_excel(writer, sheet_name='sheet1')
    df2.to_excel(writer, sheet_name='sheet2')
    
    
#仅存单个excel表格就用to_excel更简单
df1.to_excel("result.xlsx")