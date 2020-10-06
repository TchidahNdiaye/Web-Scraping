# -*- coding: utf8 -*-
import pdb
import re
import os
import pickle
import html
import csv
 
L=os.listdir('ratios_next20')
Base=[['firme','stock','book_to_market','price_to_sales','price_to_cash_flow','price_to_book','dividend_yield','g','payout_ratio']]
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

        pattern2 = '<h2 class="float_lang_base_1 inlineblock">Ratios (.+?(?=</h2>))'
        stock = re.findall(pattern2,content)
        if stock==[]:
            print("Problème d\'extraction du sigle de l'action: ",k)
        else:
            print(stock)
            print("le sigle de l\'action est:",stock)

        pattern3 = 'Valeur comptable par action <i class="lighterGrayFont arial_11">MRQ</i></span></td>\n                                <td>(.+?(?=</td>))'
        book_to_market = re.findall(pattern3,content)
        if book_to_market==[]:
            print("Problème d\'extraction de ma valeur comptable sur la valeur de marché de: ",k)
        else:
            print(book_to_market)
            print("la valeur comptable sur la valeur de marché de",k,"est:",book_to_market)
        
        pattern4 = 'Cours/Ventes <i class="lighterGrayFont arial_11">TTM</i></span></td>\n                                <td>(.+?(?=</td>))'
        price_to_sales = re.findall(pattern4,content)
        if price_to_sales==[]:
            print("Problème d\'extraction du Price_to_sales de l'action: ",k)
        else:
            print(price_to_sales)
            print("le Price_to_sales est:",price_to_sales)

        pattern5 = 'Cours/Flux de trésorerie <i class="lighterGrayFont arial_11">MRQ</i></span></td>\n                                <td>(.+?(?=</td>))'
        price_to_cash_flow = re.findall(pattern5,content)
        if price_to_cash_flow==[]:
            print("Problème d\'extraction du Price_to_Cash_Flow de l'action: ",k)
        else:
            print(price_to_cash_flow)
            print("le Price_to_Cash_Flow est:",price_to_cash_flow)

        pattern6 = 'Cours/Valeur comptable <i class="lighterGrayFont arial_11">MRQ</i></span></td>\n                                <td>(.+?(?=</td>))'
        price_to_book = re.findall(pattern6,content)
        if price_to_book==[]:
            print("Problème d\'extraction du Price_to_Book de l'action: ",k)
        else:
            print(price_to_book)
            print("le Price_to_Book est:",price_to_book)

        pattern7 = 'Rendement action <i class="lighterGrayFont arial_11">ANN</i></span></td>\n                                <td>(.+?(?=</td>))'
        dividend_yield = re.findall(pattern7,content)
        if dividend_yield==[]:
            print("Problème d\'extraction du Dividend_Yield de l'action: ",k)
        else:
            print(dividend_yield)
            print("le Dividend_Yield est:",dividend_yield)

        pattern8 = 'Taux de croissance du dividende <i class="lighterGrayFont arial_11">ANN</i></span></td>\n                                <td>(.+?(?=</td>))'
        g = re.findall(pattern8,content)
        if g==[]:
            print("Problème d\'extraction du g de l'action: ",k)
        else:
            print(g)
            print("le taux de croissance des dividendes est:",g)
        
        pattern9 = 'Ratio de distribution <i class="lighterGrayFont arial_11">TTM</i></span></td>\n                                <td>(.+?(?=</td>))'
        payout_ratio = re.findall(pattern9,content)
        if payout_ratio==[]:
            print("Problème d\'extraction du taux de distribution de: ",k)
        else:
            print(payout_ratio)
            print("le taux de distribution du résultat est:",payout_ratio)
            
        if len(stock)==1 and len(book_to_market)==1 and len(price_to_sales)==1 and len(price_to_cash_flow)==1 and len(price_to_book)==1 and len(dividend_yield)==1 and len(g)==1 and len(payout_ratio)==1:
                print("Extraction réaliser avec succès ",k)
        else:
                if len(stock)!=1:
                    pattern2 = '<h2 class="float_lang_base_1 inlineblock">(.+?(?= Ratios</h2>))'
                    stock = re.findall(pattern2,content)
                if len(book_to_market) !=1:
                    pattern3 = 'Book Value/Share <i class="lighterGrayFont arial_11">MRQ</i></span></td>\n                                <td>(.+?(?=</td>))'
                    book_to_market = re.findall(pattern3,content)
                if len(price_to_sales) !=1:
                    pattern4 ='Price to Sales <i class="lighterGrayFont arial_11">TTM</i></span></td>\n                                <td>(.+?(?=</td>))'
                    price_to_sales = re.findall(pattern4,content)
                if len(price_to_cash_flow) !=1:
                    pattern5 = 'Price to Cash Flow <i class="lighterGrayFont arial_11">MRQ</i></span></td>\n                                <td>(.+?(?=</td>))'
                    price_to_cash_flow = re.findall(pattern5,content)
                if len(price_to_book)!=1:
                    pattern6 = 'Price to Book <i class="lighterGrayFont arial_11">MRQ</i></span></td>\n                                <td>(.+?(?=</td>))'
                    price_to_book = re.findall(pattern6,content)
                if len(dividend_yield) !=1:
                    pattern7 = 'Dividend Yield <i class="lighterGrayFont arial_11">ANN</i></span></td>\n                                <td>(.+?(?=</td>))'
                    dividend_yield = re.findall(pattern7,content)
                if len(g) !=1:
                    pattern8 = 'Dividend Growth Rate <i class="lighterGrayFont arial_11">ANN</i></span></td>\n                                <td>(.+?(?=</td>))'
                    g = re.findall(pattern8,content)
                if len(payout_ratio) !=1:
                    pattern9 = 'Payout Ratio <i class="lighterGrayFont arial_11">TTM</i></span></td>\n                                <td>(.+?(?=</td>))'
                    payout_ratio = re.findall(pattern9,content)

        firme = firme[0]
        stock = stock[0]
        book_to_market = book_to_market[0]
        price_to_sales = price_to_sales[0]
        price_to_cash_flow = price_to_cash_flow[0]
        price_to_book = price_to_book[0]
        dividend_yield = dividend_yield[0]
        g = g[0]
        payout_ratio = payout_ratio[0]

        Result = [firme,stock,book_to_market,price_to_sales,price_to_cash_flow,price_to_book,dividend_yield,g,payout_ratio]
        Base.append(Result)
        

with open("cac_next20_ratios.csv", "w",encoding='utf8') as outfile:
        data=csv.writer(outfile,delimiter=',',lineterminator='\n')
        for b in Base:
                data.writerow(b)
