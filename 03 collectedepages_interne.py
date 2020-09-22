# -*- coding: utf8 -*-

import requests
import pdb
import re


with open('pagescollectees/finance_marché_page0.txt','r',encoding='utf8') as output:
    content = output.read()

#result=2012TOU10056
patern = '<div class="informations">\n\n<h2>\n\n<a href=/(.+?(?=>))'
result = re.findall(patern,content)
if result==[]:
    print("problème d\'extraction")
else:
    print(result)
    print('le résultat est :',result)

pdb.set_trace()


'''
d = 250
content0 = content[651732-d:651732+d]
'''
