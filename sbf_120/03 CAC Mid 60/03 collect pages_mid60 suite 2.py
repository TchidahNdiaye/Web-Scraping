# -*- coding: utf8 -*-

import requests
import pdb
import time
import re
import pickle
import os
import html
import csv

# Extraction des pages de chaque action
for k in ['ipsos','societe-bic','nexans','akka-technologies','m6-metropole','gtt',
          'tarkett','sopra-group','trigano','dassault-avia','virbac','robertet']:
    url='https://fr.investing.com/equities/'+k
    request_headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' + ' (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

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
                with open('pages_mid60/'+k+'.txt','w',encoding='utf8') as output:
                    output.write(content)

                i=1000
            else:
                i=i+1
                time.sleep(1)

    if i==1000:
        print("code source de la page",k,"est collecté")
    else:
        if j==1000:
            print("probléme au niveau de la collecte de la page ",k)
        else:
            print("problème au niveau du timeout",k)

pdb.set_trace()

'''
'eurazeo?cid=25448',
'korian?cid=23514',

Après plusieurs téléchargement, mon User-agent a été
réfusé et j'avais la réponse 406 à req.status_code
ce qui m'amène à changer de user agent. et la
collecte a parfaitement réussi avec ce nouveau code.
'''
