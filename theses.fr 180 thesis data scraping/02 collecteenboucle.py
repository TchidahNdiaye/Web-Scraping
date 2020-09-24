# -*- coding: utf8 -*-
import requests
import pdb
import time

for x in ['entreprise','marché']:
    for y in ['0','10','20','30','40','50','60','70','80','90']:
        url='http://www.theses.fr/fr/?q=finance%20'+x+'&start='+y
        request_headers={'User-Agent': "(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6" }

        i=0
        while i<5:
            j=0
            while j<5:
                try:
                    req=requests.get(url,headers=request_headers,timeout=10)
                    j=1000
                except:
                    time.sleep(1)
                    j=j+1

            if j==1000:
                if req.status_code==200:
                    content=req.text
                    with open('pagescollectees/finance_'+x+'_page'+y+'.txt','w',encoding='utf8') as output:
                        output.write(content)

                    i=1000
                else:
                    i=i+1
                    time.sleep(1)

        if i==1000:
            print("code source de la page",x,y,"est collecté")
        else:
            if j==1000:
                print('problème au niveau du code status',x,y)
            else:
                print('problème au niveau du timeout',x,y)

pdb.set_trace()
