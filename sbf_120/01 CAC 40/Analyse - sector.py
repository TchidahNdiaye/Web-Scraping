# -*- coding: utf8 -*-
import pdb
import re
import os
import pickle
import html
import csv
 
L=os.listdir('pagescollectees')
Base=[['firme','sector']]
for k in L:
        with open('pagescollectees/'+k,'r',encoding='utf8') as output:
                    content = output.read()
        content = html.unescape(content)
        pattern1 = '<h1 class="float_lang_base_1 relativeAttr"\n\tdir="ltr" itemprop="name">(.+?(?=\t</h1>))'
        firme = re.findall(pattern1,content)
                
        pattern2 = '<div>Secteur<a href="/stock-screener/.{45,68}">(.+?(?=</a></div>))'
        sector = re.findall(pattern2,content)
                
        if len(firme)==1 and len(sector)==1:
                print("100% - Extraction réaliser avec succès", firme, sector)
        else:
                if len(firme) !=1:
                        pattern1 ='class="float_lang_base_1 relativeAttr"\n\tdir="ltr" >(.+?(?=\t</h1>))'
                        firme = re.findall(pattern1,content)
                if len(sector) !=1:
                        pattern2 ='<div>Sector<a href="/stock-screener/.{45,70}">(.+?(?=</a>))'
                        sector = re.findall(pattern2,content)
                print("Après correction, on a :", firme, sector)
        
        firme = firme[0]
        sector = sector[0]

        Result = [firme,sector]
        Base.append(Result)

with open("cac40_sector.csv", "w",encoding='utf8') as outfile:
        data=csv.writer(outfile,delimiter=',',lineterminator='\n')
        for b in Base:
                data.writerow(b)
