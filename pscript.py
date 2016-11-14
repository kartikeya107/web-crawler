from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from crawler import WebCrawler
import json
import sys

with open('config.json', 'r') as f:
    config = json.load(f)

webCrawler = WebCrawler(config)
args = sys.argv
if(len(args)==2):
    keyword = args[1]
    numResults = webCrawler.getNumResults(keyword)
    if(numResults==0):
        print("Sorry, No results found")
    else:
        print("No. of results found - "+str(numResults))
        
elif(len(args)==3):
    keyword = args[1]
    pageNum = args[2]
    productList = webCrawler.getProducts(pageNum, keyword)
    if(len(productList)==0):
        print("Sorry, No results found")
    else:
        print("Items found:")
        for product in productList:
            print("Name - "+product.getProductName())
            print("Price - "+product.getProductPrice())
            print("Merchant - "+product.getMerchantName())
            print("Image - "+product.getProductImgUrl())
            print("")

    


