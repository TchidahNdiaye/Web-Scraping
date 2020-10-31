# -*- coding: utf8 -*-
import requests
import pdb

# 1. Page teleperformance
url1='https://www.investing.com/equities/teleperformance'

request_headers={'User-Agent': "(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6" }

req=requests.get(url1,headers=request_headers,timeout=10)
content=req.text

with open('teleperformance.txt','w',encoding='utf8') as output:
    output.write(content)
    

# 1. Ratios teleperformance
url2='https://www.investing.com/equities/teleperformance-ratios'

request_headers={'User-Agent': "(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6" }

req=requests.get(url2,headers=request_headers,timeout=10)
content=req.text

with open('teleperformance-ratios.txt','w',encoding='utf8') as output:
    output.write(content)


pdb.set_trace()
