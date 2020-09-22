# -*- coding: utf8 -*-

import requests
import pdb
import time


url="http://www.theses.fr/fr/?q=finance%20entreprise&start=0"
request_headers={'User-Agent': "(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6" }
req=requests.get(url,headers=request_headers,timeout=10)
content=req.text

with open('pagescollectees/codepage.txt','w',encoding='utf8') as output:
    output.write(content)
    
pdb.set_trace()
