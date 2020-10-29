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
        if firme==[]:
            print("Problème d\'extraction du nom de la firme : ",k)
        else:
            print(firme)
            print('le nom de la société est:',firme)

        pattern2 = 'Rentabilité des capitaux propres <i class="lighterGrayFont arial_11">TTM</i></span></td>\n                                <td>(.+?(?=</td>))'
        return_on_equity = re.findall(pattern2,content)
        if return_on_equity==[]:
            print("Problème d\'extraction du g de l'action: ",k)
        else:
            print(return_on_equity)
            print("la rentabilité des capitaux propres est:",return_on_equity)
        

        firme = firme[0]
        return_on_equity = return_on_equity[0]

        Result = [firme,return_on_equity]
        Base.append(Result)
        

with open("cac_next20_roe.csv", "w",encoding='utf8') as outfile:
        data=csv.writer(outfile,delimiter=',',lineterminator='\n')
        for b in Base:
                data.writerow(b)
