# -*- coding: utf8 -*-
import requests
import pdb
import re

'''
    Page de deuxième collecte qui permet de collecter les identifiants
    des pages déjà collectées et extraire
'''

with open('pagecomment/commentaires.txt','r',encoding='utf8') as output:
    content = output.read()

        #contenudelapage.find('identifiant unique de la page')

p=300
contenu = contenudelapage[658223-p:658223+p]
pdb.set_trace()

        #puis ecrire print(contenu) et chercher la balise contenant l'identifiant


'''
pattern='
Result=re.findall(pattern,contenudelapage)
if len(Result)==20:
    print('Extraction reussit')
else:
    print('problème au niveau de l\'extraction')
'''
