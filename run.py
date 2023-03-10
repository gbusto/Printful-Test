import requests
import os

"""
curl --location --request GET 'https://api.printful.com/oauth/scopes' --header 'Authorization: Bearer amPFnWAkcjtgf8RZbbk7QLvJHaxfmgHapxtLGh43'

curl --location --request GET 'https://api.printful.com/products' --header 'Authorization: Bearer amPFnWAkcjtgf8RZbbk7QLvJHaxfmgHapxtLGh43'

--header "X-PF-Store-Id: 10117137"

curl --location --request GET 'https://api.printful.com/store/products' --header 'Authorization: Bearer amPFnWAkcjtgf8RZbbk7QLvJHaxfmgHapxtLGh43' --header "X-PF-Store-Id: 10117137"
"""

API_URL = "https://api.printful.com"
PRODUCTS_URL = "{}/products".format(API_URL)
STORE_PRODUCTS_URL = "{}/store/products".format(API_URL)
STORE_ID = "10117137"
TOKEN = "amPFnWAkcjtgf8RZbbk7QLvJHaxfmgHapxtLGh43"

if not TOKEN:
    print("[!] Token not found!")

storeHeader = { "X-PF-Store-ID": STORE_ID }

authHeader = { "Authorization": "Bearer {}".format(TOKEN) }

combinedHeaders = {
    "X-PF-Store-ID": STORE_ID,
    "Authorization": "Bearer {}".format(TOKEN),
}

def getStoreProducts():
    response = requests.get(STORE_PRODUCTS_URL, headers=combinedHeaders)

    if response.status_code == 200:
        return response.json()

    raise Exception("Error getting store products: {}".format(response.text))

if __name__ == "__main__":
    products = getStoreProducts()
    print(products)