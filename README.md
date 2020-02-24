# corona2019 
Get the data from the web and analyze the infected number of people.

Data source:
1. migration data: http://qianxi.baidu.com/

2. infected data: https://news.qq.com

How to import data from a website:
1. On a website, go to more tools>Developer tools>Network>JS, get the url for api.
  For example, the history curve which gives the migration index on http://qianxi.baidu.com/ is 'http://huiyan.baidu.com/migration/historycurve.jsonp?dt=city&id=420100&type=move_out'.
 'http://view.inews.qq.com/g2/getOnsInfo?name=disease_h5' is url for the infected number from https://news.qq.com
  
2. request the url and save the data as a format you want



What is included in the code:
1. curve.ipynb/curve.py : get the migration index of this year and the previous year for a city with city id and migration type, you can change the id and type in the script. Type has two kinds, one is 'move_in' and another one is 'move_out'. And id is explained in the later text.

2. : get the migration percentage for a city with city id or province id and type.

3. : get the infected number of people in diffent cities and provinces


How to map city/province id with city/province names:

