from bs4 import BeautifulSoup
soup = BeautifulSoup(req.text, 'html.parser')

productName = input('Please enter the product you want to find: ')
urlProduct = 'https://www.sainsburys.co.uk/gol-ui/SearchDisplayView?filters[keyword]='+productName
req = requests.get(urlProduct)

productTitle = soup.h1['pd_header']
descriptionProduct = soup.findAll('p',attrs={'section', class_='pd__description'})
retailPrice = = soup.findAll('p',attrs={'section', class_='pd__cost__total undefined'})
unitPrice = = soup.findAll('p',attrs={'section', class_='pd__cost__per-unit'})

print(productTitle, descriptionProduct, retailPrice, unitPrice)
