#import library
from urllib .request import Request, urlopen as uReq
from bs4 import BeautifulSoup as soup

#web url
myUrl = 'https://elrahexclusive.my/product-category/baju-melayu/magnificent-4-0/?products-per-page=all'

#request
uClient = uReq(myUrl)
page_html = uClient.read()
uClient.close()

#parse page
page_soup = soup(page_html,"html.parser")

#csv file
fileName = "Elrah(Magnificent 4.0).csv"
f = open(fileName, "w")

headers = "Product Name,Product Price,Category\n"
f.write(headers)

shoeContainers = page_soup.findAll("div",{"class":"product-inner clr"})

for container in shoeContainers:
    name_container = container.findAll("li",{"class":"title"})
    prod_name = name_container[0].find("a").text
    print("Product Name: " + prod_name)

    price_container = container.findAll("span", {"class":"woocommerce-Price-amount amount"})
    prod_price = price_container[0].find("bdi").text
    print("Product Price: " + prod_price)

    cat_container = container.findAll("li", {"class":"category"})
    category = cat_container[0].find("a").text
    
    print("Product Name: " + prod_name)
    print("Product Price: " + prod_price)
    print("Category: " + category)

    f.write(prod_name.replace(",","|") + "," + prod_price.replace(",",".") + "," + category + "\n")

f.close()
#test