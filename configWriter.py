import json

config = {
    "shopUrl" : "http://www.shopping.com/products",
    "numTotalResults": {
        "class" : "numTotalResults"
        },
    "gridBox" : {
        "class" : "gridBox"
        },
    "productName" : {
        "class" : "productName"
        },
    "imgUrl" : {
        "class" : "imgZoomUrl149"
        },
    "productPrice" : {
        "class" : "productPrice"
        },
    "merchantName" : {
        "class" : "newMerchantName"
        },
    }

with open('config.json', 'w') as f:
    json.dump(config, f)
