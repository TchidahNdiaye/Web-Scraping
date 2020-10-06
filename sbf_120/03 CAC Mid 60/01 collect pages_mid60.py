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
for k in ['natixis','ses-global','cgg-veritas','air-france---klm','bollore-s.a.',
          'eutelsat-comm','elis-services-sa','mercialys','rexel','cnp-assurances',
          'genfit-sa','rubis','lagardere-s.c.a.','elior','casino','fonc-des-regions',
          'spie-promesses','la-francaise-des-jeux-sa','tf1','soitec','aperam',
          'jcdeceaux','coface','dbv-technologies-sa','aeroports-paris','icade',
          'euronext','biomerieux','neoen','amundi-sa','ipsen','alten','remy-cointreau',
          'plastic-omnium','imerys','maisons-du-monde-sas','groupe-fnac','ald-international-sa',
          'nexity','wendel','iliad','stedim','eramet','albioma','vallourec','seb','ipsos',
          'societe-bic','nexans','akka-technologies','m6-metropole','tarkett','gtt',
          'sopra-group','trigano','dassault-avia','virbac','robertet']:
    url='https://fr.investing.com/equities/'+k
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
'''
