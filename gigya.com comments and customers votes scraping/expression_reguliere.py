# -*- coding: utf8 -*-
import requests
import pdb
import re

contenu='AAA<a href=097678289>Albane Geslin</span>\n\n<a href=096621317>Joffrey Drouard</span>AAA'
pattern ='AAA<a href=.{9,9}>(.{1,20}</span>'
Result = re.findall(pattern,contenu)


'''
On a des carractères spéciques aux  expressions regulières
Lorsqu'on met des parenthèses cela signifie de collecté (.{9,9})
les caractères et sans parenthèses, il s'agira des les masquer  .{9,9}
Pourqu'elle collecte tout, il faut mettre (?s) avant
Pour éviter les caractères spécifique, on met un dollar devant

 (.+?(?=)) est une expression regulière qui fonctionne indépendament de
la longueur de l'élément que nous souhaitons collecter.
'''
