#!/usr/bin/env python
# coding: utf-8


import requests
import json
import pandas as pd



id = 420100
type = 'move_out'



url = 'http://huiyan.baidu.com/migration/historycurve.jsonp?dt=city&id={id}&type={type}'.format(id = id,type=type)



#get response
file = requests.get(url)


#read data from file 
data = json.loads(file.text.split('(')[1][:-1])
dict = data['data']['list']

#change dictionary to panda DataFrame
col = str(id) + '_' + type + '_index'
df = pd.DataFrame(dict,index=[0])

df_2019 = df.iloc[:,0:61]
df_2020 = df.iloc[:,61:]

#save the two year data
out_2019 = col + '_2019.csv'
out_2020 = col + '_2020.csv'
df_2019.to_csv(out_2019)
df_2020.to_csv(out_2020)







