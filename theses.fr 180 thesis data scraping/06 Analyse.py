# -*- coding: utf8 -*-
import pdb
import re
import os
import pickle
import html
import csv
 
L=os.listdir('PageInd')
Base=[['identifiant','doctorant','titre','domaine','directeur','université']]
for k in L:
        with open('PageInd/'+k,'r',encoding='utf8') as output:
                    content = output.read()

        content = html.unescape(content)

        pattern1 = '<meta property="og:url" content="http://www.theses.fr/(.+?(?="/>))'
        identifiant = re.findall(pattern1,content)

        pattern2 = '<meta name="DC.creator" content="(.+?(?=" />))'
        doctorant = re.findall(pattern2,content)

        pattern3 = '<meta property="og:title" content="(.+?(?="/>))'
        titre = re.findall(pattern3,content)

        pattern4 = '<span property="dc:subject">(.+?(?=</span>))'
        domaine = re.findall(pattern4,content)

        pattern5 = '<meta name="DC.contributor" content="(.+?(?= "/>))'
        directeur = re.findall(pattern5,content)

        pattern6 = '<meta name="DC.publisher" content="(.+?(?=" />))'
        université = re.findall(pattern6,content)

        if len(identifiant)==1 and len(titre)==1 and len(directeur)==1 and len(université)==1:
            print("Extraction réaliser avec succès ",k)
        else:
                if len(identifiant)!=1:
                    pattern1 = '<link rel="alternate" href="http://www.theses.fr/(.+?(?=.rdf"))'
                    identifiant = re.findall(pattern1,content)
                if len(titre) !=1:
                    pattern3 = '<h1 property="dc:title" xml:lang="fr">(.+?(?=</h1>))'
                    titre = re.findall(pattern3,content)
                if len(directeur) !=1:
                    pattern5 ='<p>Sous la direction de \n\n<span rel="dcterms:contributor"><span typeof="foaf:Person" property="foaf:name">(.+?(?=</span></span>.\n\n</p>))'
                    directeur = re.findall(pattern5,content)
                if len(université) !=1:
                    pattern6 = 'Thèses en préparation à <a href=".{7,12}" rel="dcterms:contributor" resource="http://www.idref.fr/.{7,12}/id"><span property="foaf:name">(.+?(?=</span></a>))'
                    université = re.findall(pattern6,content)

        identifiant = identifiant[0]
        doctorant = doctorant[0]
        titre = titre[0]
        domaine = domaine[0]
        université = université[0]

        Result = [identifiant,doctorant,titre,domaine,directeur,université]
        Base.append(Result)

with open("TheseFinance_1.csv", "w",encoding='utf8') as outfile:
        data=csv.writer(outfile,delimiter=',',lineterminator='\n')
        for b in Base:
                data.writerow(b)


'''
        if len(identifiant)==1 and len(doctorant)==1 and len(titre)==1 and len(domaine)==1 and len(directeur)==1 and len(université)==1:
                identifiant = identifiant[0]
                doctorant = doctorant[0]
                titre = titre[0]
                domaine = domaine[0]
                directeur = directeur[0]
                université = université[0]
        else:
                pdb.set_trace()

with open("thesefinance.txt","w",encoding='utf8') as outfile:
        outfile.write(Result)

https://funds360.euronext.com/opcvm/palmares/categoryOpcvm/mixtes-mondial-flexible/fundType/all/universe/all/sgp/all/currency/all/isr/all/licontract/all/customized/0/by/perf/page/1/sortfield/varPYTD/order/DESC
'''
