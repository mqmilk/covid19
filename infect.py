#!/usr/bin/env python
# coding: utf-8


import requests
import json
import pandas as pd


url = 'https://gwpre.sina.cn/interface/fymap2020_data.json?1582592919476'


#get response as string
file = requests.get(url)
#read data from file 
data = json.loads(file.text)['data']


province = pd.DataFrame(data['list']).set_index('name')
province = province.drop(['city','adddaily','ename','hejian','susNum','deathNum','cureNum','conadd'],axis=1)
province['value'] = province['value'].apply(int)
province = province.sort_values(by='value',ascending=False)

world = pd.DataFrame(data['worldlist']).set_index('name')
world = world.drop(['citycode','susNum','deathNum','cureNum'],axis=1)
world['value'] = world['value'].apply(int)
world = world.sort_values(by='value',ascending=False)


list = []
for province_ in data['list']:
    for city in province_['city']:
        num = {'name':city['name'],'province':province_['name'],'value': int(city['conNum'])}
        list.append(num)

city = pd.DataFrame(list).set_index('name')
city = city.sort_values(by='value',ascending=False)


world.to_csv('world_infected.csv')
province.to_csv('province_infected.csv')
city.to_csv('city_infected.csv')


# In[109]:





# In[ ]:




