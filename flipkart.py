import requests
from bs4 import BeautifulSoup as bs

search_url = "https://www.flipkart.com/search?q="+"iphone12pro"
response = requests.get(search_url)

flipkart_page=response.text

flipkart_html=bs(flipkart_page,'html.parser');


bigbox=flipkart_html.findAll('div',{"class":{"cPHDOP col-12-12"}}) 
# finding all the class having key as class and values as cPHDOP col-12-12
del bigbox[0:2]
productlink="https://www.flipkart.com"+bigbox[1].div.div.div.a['href']
product_req=requests.get(productlink)
product_html=(bs(product_req.text,'html.parser'))

comment_box=product_html.findAll('div',{"class":{"col EPCmJX"}})
# print(comment_box[1].findAll('p',{"class":"_2NsDsF AwS1CA"}))

# for i in bigbox:
#     print("https://www.flipkart.com"+i.div.div.div.a['href'])

for i in comment_box:
    print(comment_box[2].div.div.findAll('p',{"class":{"_2NsDsF AwS1CA"}}))
    
