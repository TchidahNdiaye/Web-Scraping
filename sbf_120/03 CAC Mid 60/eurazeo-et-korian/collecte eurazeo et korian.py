# -*- coding: utf8 -*-
import requests
import pdb

# 1. eurazeo
url1='https://www.investing.com/equities/eurazeo'

request_headers={'User-Agent': "(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6" }

req=requests.get(url1,headers=request_headers,timeout=10)
content=req.text

with open('maison_mere/eurazeo.txt','w',encoding='utf8') as output:
    output.write(content)
    


url2='https://www.investing.com/equities/eurazeo-ratios'

request_headers={'User-Agent': "(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6" }

req=requests.get(url2,headers=request_headers,timeout=10)
content=req.text

with open('maison_mere/eurazeo-ratios.txt','w',encoding='utf8') as output:
    output.write(content)
    


####################################################################




# 2. korian
url3='https://www.investing.com/equities/korian'

request_headers={'User-Agent': "(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6" }

req=requests.get(url3,headers=request_headers,timeout=10)
content=req.text

with open('maison_mere/korian.txt','w',encoding='utf8') as output:
    output.write(content)
    



url4='https://www.investing.com/equities/korian-ratios'

request_headers={'User-Agent': "(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6" }

req=requests.get(url4,headers=request_headers,timeout=10)
content=req.text

with open('maison_mere/korian-ratios.txt','w',encoding='utf8') as output:
    output.write(content)


pdb.set_trace()

#les deux pages ont été téléchargé avec succès.
