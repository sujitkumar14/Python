import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"lxml")
    data = soup.find_all('div',{"class":"content drop-cap"})
    dataString =""
    for section in data[0]:
        print section.text.encode('utf-8')
    with open('C:/Users/sujit/Desktop/myFile.txt','w') as open_file:
        open_file.write(section.text.encode('utf-8'))
