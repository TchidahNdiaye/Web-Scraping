# -*- coding: utf8 -*-
import requests
import pdb


url='https://www.investing.com/indices/sbf-120-components'

request_headers={'User-Agent': "(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6" }

req=requests.get(url,headers=request_headers,timeout=10)
contenudelapage=req.text

with open('sbf_120/sbf-120-components.txt','w',encoding='utf8') as output:
    output.write(contenudelapage)

pdb.set_trace()
