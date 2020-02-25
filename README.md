# corona2019 
Get the data from the web and analyze the infected number of people.

Data source:
1. migration data: http://qianxi.baidu.com/

2. infected data: https://news.sina.cn/zt_d/yiqing0121

How to import data from a website:
1. On a website, go to more tools>Developer tools>Network>JS, get the url for api.
  For example, the history curve which gives the migration index on http://qianxi.baidu.com/ is 'http://huiyan.baidu.com/migration/historycurve.jsonp?dt=city&id=420100&type=move_out'.
 
 
2. request the url and save the data as a format you want



What is included in the code:
1. city_id.csv, state_id.csv: give the ids for different provinces and cities used in other codes. For example, 420100 is the city_id for wuhan(武汉).

2. curve.ipynb/curve.py : get the migration index of this year and the previous year at the same lunar calendar day for a two-month period moving in or out a city. You can change the id and type in the script. There are two kinds of 'type', one is 'move_in' and another one is 'move_out'. And id is explained in the previous code city_id.csv and state_id.csv.

3. percent.ipynb/percent.py: get the migration top 100 cities/provinces moving in or out a city per day. You can change the rank, id and type to collect different kinds of data.

4. infect.ipynb/infect.py: get the infected number of people in cities ,provinces in China or countries around the world.

5. data_analysis.ipynb/data_analysis.py: analyze the relationship between migration and infection. The script analyzes the province migration data.



