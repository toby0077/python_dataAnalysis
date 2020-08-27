# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 11:30:16 2019

呆瓜半小时入门python数据分析：http://dwz.date/b62x
@author:231469242@qq.com
微信公众号：pythonEducation
"""

import pandas as pd
import numpy as np
from numpy import nan as NaN

df=pd.DataFrame([[1,2,3],[NaN,NaN,2],[NaN,NaN,NaN],[8,8,NaN]])

#用100填充空缺值，但df不会真是改变，因此替换后结果保存为df1
df1=df.fillna("")

#直接在df上替换空值
df.fillna("",inplace=True)



