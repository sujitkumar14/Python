import requests
from bs4 import BeautifulSoup

url = "http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(url)
soup= BeautifulSoup(r.text,"lxml")
data = soup.find_all('div',{"class":"content drop-cap"})
for section in data[0]:
    print section.text
