# -*- coding: utf8 -*-
import pdb
import re
import os
import pickle
import html
import csv
 
L=os.listdir('ratios_next20')
Base=[['firme','return_on_equity']]
for k in L:
        with open('ratios_next20/'+k,'r',encoding='utf8') as output:
                    content = output.read()

        content = html.unescape(content)

        pattern1 = '<h1 class="float_lang_base_1 relativeAttr"\n\tdir="ltr" itemprop="name">(.+?(?=\t</h1>))'
        firme = re.findall(pattern1,content)

        pattern2 = 'Rentabilité des capitaux propres <i class="lighterGrayFont arial_11">TTM</i></span></td>\n                                <td>(.+?(?=</td>))'
        return_on_equity = re.findall(pattern2,content)

        if len(firme)==1 and len(return_on_equity)==1:
                print("Extraction réalisé avec succès", k)
        else:
                if len(return_on_equity)!=1:
                        pattern2 = 'Return on Equity <i class="lighterGrayFont arial_11">TTM</i></span></td>\n                                <td>(.+?(?=</td>))'
                        return_on_equity = re.findall(pattern2,content)
                        print("le ROE est :", firme, return_on_equity)

        firme = firme[0]
        return_on_equity = return_on_equity[0]

        Result = [firme,return_on_equity]
        Base.append(Result)
        

with open("cac_next20_roe.csv", "w",encoding='utf8') as outfile:
        data=csv.writer(outfile,delimiter=',',lineterminator='\n')
        for b in Base:
                data.writerow(b)
