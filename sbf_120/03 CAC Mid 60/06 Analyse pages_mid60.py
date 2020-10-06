# -*- coding: utf8 -*-
import pdb
import re
import os
import pickle
import html
import csv
 
L=os.listdir('pages_mid60')
Base=[['firme','price','market_cap','price_to_earnings','beta','earnings_per_share','dividend','shares_outstanding','sector','employees','revenue','indices']]
for k in L:
        with open('pages_mid60/'+k,'r',encoding='utf8') as output:
                    content = output.read()

        content = html.unescape(content)

        pattern1 = '<h1 class="float_lang_base_1 relativeAttr"\n\tdir="ltr" itemprop="name">(.+?(?=\t</h1>))'
        firme = re.findall(pattern1,content)

        pattern2 = 'Clôture précédente</span><span class="float_lang_base_2 bold">(.+?(?=</span></div>))'
        price = re.findall(pattern2,content)

        pattern3 = 'Cap. boursière</span><span class="float_lang_base_2 bold">(.+?(?=</span></div>))'
        market_cap = re.findall(pattern3,content)

        pattern4 = 'PER</span><span class="float_lang_base_2 bold">(.+?(?=</span></div>))'
        price_to_earnings = re.findall(pattern4,content)

        pattern5 = 'Bêta</span><span class="float_lang_base_2 bold">(.+?(?=</span></div>))'
        beta = re.findall(pattern5,content)

        pattern6 = 'BPA</span><span class="float_lang_base_2 bold">(.+?(?=</span></div>))'
        earnings_per_share = re.findall(pattern6,content)

        pattern7 = 'Dividende</span><span class="float_lang_base_2 bold">(.+?(?= .{4,9}</span></div>))'
        dividend = re.findall(pattern7,content)
        
        pattern8 = 'Act. en circulation</span><span class="float_lang_base_2 bold">(.+?(?=</span></div>))'
        shares_outstanding = re.findall(pattern8,content)

        pattern9 = '<div>Secteur<a href="/stock-screener/?sp=country::22|sector::9|industry::a|equityType::a<eq_market_cap;1">(.+?(?=</a></div>))'
        sector = re.findall(pattern9,content)
        
        pattern10 = '<div>Employés<p class="bold">(.+?(?=</p></div>))'
        employees = re.findall(pattern10,content)

        pattern11 = 'Performance</span><span class="float_lang_base_2 bold">(.+?(?=</span></div>))'
        revenue = re.findall(pattern11,content)

        indices = "cac mid 60"

        if len(firme)==1 and len(price)==1 and len(market_cap)==1 and len(price_to_earnings)==1 and len(beta)==1 and len(earnings_per_share)==1 and len(dividend)==1 and len(shares_outstanding)==1 and len(sector)==1 and len(employees)==1 and len(revenue)==1:
                print("Extraction réaliser avec succès ",k)
        else:
                if len(firme)!=1:
                    pattern1 = '<h1 class="float_lang_base_1 relativeAttr" n/dir="ltr" itemprop="name">(.+?(?=	</h1>))'
                    firme = re.findall(pattern1,content)
                if len(price) !=1:
                    pattern2 = 'Prev. Close</span><span class="float_lang_base_2 bold">(.+?(?=</span></div>))'
                    price = re.findall(pattern2,content)
                if len(market_cap) !=1:
                    pattern3 ='Market Cap</span><span class="float_lang_base_2 bold">(.+?(?=</span></div>))'
                    market_cap = re.findall(pattern3,content)
                if len(price_to_earnings) !=1:
                    pattern4 = 'P/E Ratio</span><span class="float_lang_base_2 bold">(.+?(?=</span></div>))'
                    price_to_earnings = re.findall(pattern4,content)
                if len(beta)!=1:
                    pattern5 = 'Beta</span><span class="float_lang_base_2 bold">(.+?(?=</span></div>))'
                    beta = re.findall(pattern5,content)
                if len(earnings_per_share) !=1:
                    pattern6 = 'EPS</span><span class="float_lang_base_2 bold">(.+?(?=</span></div>))'
                    earnings_per_share = re.findall(pattern6,content)
                if len(dividend) !=1:
                    dividend = "NaN"
                if len(shares_outstanding) !=1:
                    pattern8 = 'Shares Outstanding</span><span class="float_lang_base_2 bold">(.+?(?=</span></div>))'
                    shares_outstanding = re.findall(pattern8,content)
                if len(employees) !=1:
                    pattern10 ='Employees<p class="bold">(.+?(?=</p></div>))'
                    employees = re.findall(pattern10,content)
                if len(revenue) !=1:
                    pattern11 = 'Revenue</span><span class="float_lang_base_2 bold">(.+?(?=</span></div>))'
                    revenue = re.findall(pattern11,content)

        firme = firme[0]
        price = price[0]
        market_cap = market_cap[0]
        price_to_earnings = price_to_earnings[0]
        beta = beta[0]
        earnings_per_share = earnings_per_share[0]
        dividend = dividend[0]
        shares_outstanding = shares_outstanding[0]
        sector = sector[0]
        employees = employees[0]
        revenue = revenue[0]
        indices = indices[0]

        Result = [firme,price,market_cap,price_to_earnings,beta,earnings_per_share,dividend,shares_outstanding,sector,employees,revenue]
        Base.append(Result)
        

with open("cac_mid60_base.csv", "w",encoding='utf8') as outfile:
        data=csv.writer(outfile,delimiter=',',lineterminator='\n')
        for b in Base:
                data.writerow(b)
