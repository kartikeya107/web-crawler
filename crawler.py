from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import json

class WebCrawler:

    def __init__(self, config):
        self.productList = []
        self.config = config
        
    def loadUrl(self, url):
        page = urlopen(url)
        #print("page loaded")
        #page = open('shop.txt', 'r')
        self.soup = bs(page.read(), "html.parser")

    def getNumResults(self, keyword):
        url = self.getUrlNumResults(keyword)
        try:
            self.loadUrl(url)
            resultSpans = self.soup.findAll("span", self.config["numTotalResults"])
            if(len(resultSpans)==0):
                numResults = 0
            else:
                resultStr = resultSpans[0].string.strip()
                if "of" in resultStr:
                    ofIndex = resultStr.index('of')
                    resCntStr = resultStr[ofIndex+2:]
                    resCntStr = resCntStr.strip()
                    numResults = resCntStr;
                else:
                    numResults = 0
        except:
            numResults = 0

        return numResults

    def getProducts(self, pageNum, keyword):
        url = self.getUrlProducts(pageNum, keyword)
        try:
            self.loadUrl(url)
            gridBoxes = self.soup.findAll("div", self.config["gridBox"])
            for gridBox in gridBoxes:
                try:
                    productSpan = gridBox.find('a', self.config["productName"]).find('span')
                    productName = productSpan['title']
                except:
                    productSpan = gridBox.find('a', self.config["productName"])
                    productName = productSpan['title']

                try:    
                    productImg = gridBox.find('img', self.config["imgUrl"])
                    productImgUrl = productImg['src']
                except:
                    productImgUrl = ""

            
                spanProductPrice = gridBox.find('span', self.config["productPrice"])
                try:
                    toSalePrice = spanProductPrice.find('a')
                    productPrice = toSalePrice.string.strip()
                except:
                    productPrice = spanProductPrice.string.strip()

                try:
                    merchantNameTag = gridBox.find('a', self.config["merchantName"])
                    merchantName = merchantNameTag.string
                except:
                    merchantNameTag = gridBox.find('span', self.config["merchantName"])
                    merchantName = merchantNameTag.string

                product = Product(productName, productImgUrl, productPrice, merchantName)
                self.productList.append(product)
                
        except:
                self.productList = []

        return self.productList

    def getUrlNumResults(self, keyword):
        return self.config["shopUrl"]+"?KW="+keyword

    def getUrlProducts(self, pageNum, keyword):
        return self.config["shopUrl"]+"~PG-"+str(pageNum)+"?KW="+keyword


class Product:

    def __init__(self, productName, productImgUrl, productPrice, merchantName):
        self.productName = productName
        self.productImgUrl = productImgUrl
        self.productPrice = productPrice
        self.merchantName = merchantName
        
    def getProductName(self):
        return self.productName

    def setProductName(self, productName):
        self.productName = productName
            
    def getProductImgUrl(self):
        return self.productImgUrl

    def setProductName(self, productImgUrl):
        self.productImgUrl = productImgUrl

    def getProductPrice(self):
        return self.productPrice

    def setProductName(self, productPrice):
        self.productPrice = productPrice

    def getMerchantName(self):
        return self.merchantName

    def setMerchantName(self, merchantName):
        self.merchantName = merchantName
