#!/usr/bin/env python
# coding: utf-8


import requests
import json
import pandas as pd

rank = 'cityrank'   #['provincerank','cityrank']
id = 420100
type = 'move_out'   #['move_out','move_in']


#get data from 20200101-20200124
for i in range(1,25):
    date=20200100+i
    url = 'http://huiyan.baidu.com/migration/{rank}.jsonp?dt=city&id={id}&type={type}&date={date}'.format(id=id,rank=rank,type=type,date=date)
    #get response as string 
    file = requests.get(url)
    #read data from file 
    data = json.loads(file.text.split('(')[1][:-1])
    dict = data['data']['list']
    df_ = pd.DataFrame(dict)
    if 'city' in rank:
        df_['city_name']=df_['city_name'] + df_['province_name']
        df_.drop('province_name',axis=1,inplace=True)
    df_.columns=['rank',date]
    df_[date] = df_[date].apply(lambda num : num / 100)
    if i > 1:
        df = pd.merge(df,df_, how = 'outer', on = 'rank')
    else:
        df = df_
   

df.head()

out = rank + '_' + type +'.csv'
df.to_csv(out)






