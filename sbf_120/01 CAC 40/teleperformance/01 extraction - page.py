# -*- coding: utf8 -*-
import pdb
import re
import os
import pickle
import html
import csv

Base=[['firme','price','market_cap','price_to_earnings','beta','earnings_per_share','dividend','shares_outstanding','sector','employees','revenue','indices']]

with open('teleperformance.txt','r',encoding='utf8') as output:
        content = output.read()

        content = html.unescape(content)

        pattern1 = '<h1 class="float_lang_base_1 relativeAttr"\n\tdir="ltr" >(.+?(?=\t</h1>))'
        firme = re.findall(pattern1,content)

        pattern2 = 'Prev. Close</span><span class="float_lang_base_2 bold">(.+?(?=</span>))'
        price = re.findall(pattern2,content)

        pattern3 = 'Market Cap</span><span class="float_lang_base_2 bold">(.+?(?=</span>))'
        market_cap = re.findall(pattern3,content)

        pattern4 = 'P/E Ratio</span><span class="float_lang_base_2 bold">(.+?(?=</span>))'
        price_to_earnings = re.findall(pattern4,content)

        pattern5 = 'Beta</span><span class="float_lang_base_2 bold">(.+?(?=</span>))'
        beta = re.findall(pattern5,content)

        pattern6 = 'EPS</span><span class="float_lang_base_2 bold">(.+?(?=</span>))'
        earnings_per_share = re.findall(pattern6,content)

        pattern7 = 'Dividend (Yield)</span><span class="float_lang_base_2 bold">(.+?(?= .{5,7}</span>))'
        dividend = re.findall(pattern7,content)
        
        pattern8 = 'Shares Outstanding</span><span class="float_lang_base_2 bold">(.+?(?=</span>))'
        shares_outstanding = re.findall(pattern8,content)

        pattern9 = 'Sector<a href="/stock-screener/?sp=country::22|sector::2|industry::a|equityType::a<eq_market_cap;1">(.+?(?=</a></div>))'
        sector = re.findall(pattern9,content)
        
        pattern10 = 'Employees<p class="bold">(.+?(?=</p></div>))'
        employees = re.findall(pattern10,content)

        pattern11 = 'Revenue</span><span class="float_lang_base_2 bold">(.+?(?=</span>))'
        revenue = re.findall(pattern11,content)

        indices = "cac 40"

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

        Result = [firme,price,market_cap,price_to_earnings,beta,earnings_per_share,dividend,shares_outstanding,sector,employees,revenue,indices]
        Base.append(Result)
        

with open("teleperformance_page.csv", "w",encoding='utf8') as outfile:
        data=csv.writer(outfile,delimiter=',',lineterminator='\n')
        for b in Base:
                data.writerow(b)
