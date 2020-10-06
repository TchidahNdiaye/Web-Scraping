# -*- coding: utf8 -*-
import requests
import pdb

# 1. eurazeo
url1='https://www.investing.com/equities/eurazeo?cid=25448'

request_headers={'User-Agent': "(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6" }

req=requests.get(url1,headers=request_headers,timeout=10)
content=req.text

with open('pages_mid60/eurazeo.txt','w',encoding='utf8') as output:
    output.write(content)
    


url2='https://www.investing.com/equities/fmc-technologies-inc-ratios?cid=7006'

request_headers={'User-Agent': "(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6" }

req=requests.get(url2,headers=request_headers,timeout=10)
content=req.text

with open('ratios_mid60/eurazeo.txt','w',encoding='utf8') as output:
    output.write(content)
    


####################################################################




# 2. korian
url3='https://www.investing.com/equities/korian?cid=23514'

request_headers={'User-Agent': "(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6" }

req=requests.get(url3,headers=request_headers,timeout=10)
content=req.text

with open('pages_mid60/korian.txt','w',encoding='utf8') as output:
    output.write(content)
    



url4='https://www.investing.com/equities/korian-ratios?cid=23514'

request_headers={'User-Agent': "(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6" }

req=requests.get(url4,headers=request_headers,timeout=10)
content=req.text

with open('ratios_mid60/korian.txt','w',encoding='utf8') as output:
    output.write(content)


pdb.set_trace()

#les deux pages ont été téléchargé avec succès.
