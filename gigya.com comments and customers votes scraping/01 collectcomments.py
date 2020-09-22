# -*- coding: utf8 -*-
import requests
import pdb
import json
import time


url='https://comments.us1.gigya.com/comments.getComments?categoryID=Products&streamID=1117254679&includeSettings=true&sort=votesDesc&threaded=true&includeStreamInfo=true&includeUserOptions=true&includeUserHighlighting=true&lang=en&ctag=comments_v2&APIKey=3_MD_HJHUOCjSeK80xcc1NTYJYTlZXtSSDOc3XHyRvw6dcljSs4YVf8OInYiEPtpeE&source=showCommentsUI&sourceData=%7B%22categoryID%22%3A%22Products%22%2C%22streamID%22%3A%221117254679%22%7D&sdk=js_latest&authMode=cookie&pageURL=https%3A%2F%2Fwww.barnesandnoble.com%2Freviews%2Fcapital-in-the-twenty-first-century-thomas-piketty%2F1117254679%3Fean%3D9780674979857&format=jsonp&callback=gigya.callback&context=R1284068403'
request_headers={'User-Agent': "(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6" }
req=requests.get(url,headers=request_headers,timeout=10)
content=req.text

content1 = content[15:len(content)-2]   # tu commence au caractère 15, tu vas jusqu'à la longueur de tout le content et à la fin, tu me vire les deux derniers
Dict=json.loads(content1)

for c in Dict['comments']:
    idenifiant=c['ID']
    try:
        commentaire=c['commentText']
    except:
        commentaire='no comment'
    Vote_positive=c['posVotes']
    Vote_negative=c['negVotes']
    print(commentaire,Vote_positive,Vote_negative) 

time.sleep(10)

pdb.set_trace()


