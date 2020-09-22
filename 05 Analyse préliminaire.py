# -*- coding: utf8 -*-

import pdb
import re
import os
import html
import csv

with open('PageInd/s228316.txt','r',encoding='utf8') as output:
            content = output.read()

content = html.unescape(content)

d = 300

identifiant = content[874-d:874+d]
doctorant = content[1030-d:1030+d]
titre = content[1065-d:1065+d]
domaine = content[26664-d:26664+d]
directeur = content[26912-d:26912+d]
université = content[27157-d:27157+d]

pdb.set_trace()


'''
for x in ['entreprise','marché']:
    for y in ['0','10','20','30','40','50','60','70','80','90']:     
        with open('pagescollectees/finance_'+x+'_page'+y+'.txt','r',encoding='utf8') as output:
            content = output.read()

        pattern = '<div class="informations">\n\n<h2>\n\n<a href=/(.+?(?=>))'
        result = re.findall(pattern,content)
        if result==[]:
            print("problème d\'extraction à :",x,y)
        else:
            print('les identifiants sont :',result)

            for k in result:
                url='http://www.theses.fr/'+k
                my_code={'User-Agent':"((Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6" }

                i=0
                while i<5:
                    j=0
                    while j<5:
                        try:
                            req=requests.get(url,headers=my_code,timeout=10)
                            j=1000
                        except:
                            time.sleep(1)
                            j=j+1

                    if j==1000:
                        if req.status_code==200:
                            print('succès à l\'extraction : ',x,y)
                            content2=req.text
                            with open('PageInd/'+x+'_'+k+'.txt','w',encoding='utf8') as output: 
                                output.write(content2)

                            i=1000
                        else:
                            i=i+1
                            time.sleep(1)

                if i==1000:
                    print("code source de la page ",x,k," est collecté")
                else:
                    if j==1000:
                        print("problème au niveau de l\'extraction de la page : ",x,k)
                    else:
                        print("problème au niveau du timeout lors de l\'extraction de la page : ",x,k)

print("les 200 pages ont été collectés avec succès")
'''



