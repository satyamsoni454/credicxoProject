import requests
import json
from bs4 import BeautifulSoup

# Initialising url 
url = "https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1"

# Initialising United State Proxy from http://www.freeproxylists.net/ 
proxies = {
 "http": "http://140.238.28.179:3128",
}

# Get the HTML
r = requests.get(url, proxies=proxies)
htmlContent = r.content

# Parse the Content 
soup = BeautifulSoup(htmlContent, 'html.parser')

# HTML Tree Traversal
# Scap All Products One By One 
products = soup.find_all('div', class_="product")
allProducts = {}
for product in products:

    # Scrap Product Title 
    productTitle = product.find("a", class_="catalog-item-name")
    productTitleText = productTitle.get_text()

    # Scrap Product Price 
    productPrice = product.find("span", class_="price")
    productPriceText = productPrice.get_text()
    
    # Scap Product ID Number
    productID = product.find("span", class_="product-id")
    productIDText = productID.get_text()

    # Scrap Product BrandName
    productBrandName = product.find("a", class_="catalog-item-brand")
    productBrandNameText = productBrandName.get_text()

    # Scrap Product Stock Status
    productStockStatus = product.find("span", class_="status")
    productStockStatusText = productStockStatus.get_text()
    if productStockStatusText == "Out of Stock":
        productStatus = False
    else:
        productStatus = True

    # Add Product Details in Main Dictionary
    allProducts.update({productIDText: {"Product Title": productTitleText, "Product Price": productPriceText, "Brand Name": productBrandNameText, "Stock Status": productStatus}})

# Convery Dictionary into Json
jsonContent = json.dumps(allProducts, indent=10)
print(jsonContent)