# -*- coding: utf8 -*-
import requests
import pdb


url='https://www.investing.com/equities/fmc-technologies-inc'

request_headers={'User-Agent': "(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6" }

req=requests.get(url,headers=request_headers,timeout=10)
content=req.text

with open('fmc-tech/fmc-technologies-inc.txt','w',encoding='utf8') as output:
    output.write(content)




url1='https://www.investing.com/equities/fmc-technologies-inc-ratios'

request_headers={'User-Agent': "(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6" }

req=requests.get(url1,headers=request_headers,timeout=10)
content=req.text

with open('fmc-tech/fmc-technologies-inc-ratios.txt','w',encoding='utf8') as output:
    output.write(content)
    

pdb.set_trace()

#les deux pages ont été téléchargé avec succès.
