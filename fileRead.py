import requests
from bs4 import BeautifulSoup

if __name__=="__main__":
    #fetch all the names from url
    url = "http://www.practicepython.org/assets/nameslist.txt"
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"lxml")
    print soup
    data = soup.find('p')
    #write the names into the names.txt file
    with open("C:/Users/sujit/Desktop/names.txt",'w') as names_file:
        names_file.write(data.text)
    #read the names from the names.text file
    names = {}
    with open("C:/Users/sujit/Desktop/names.txt",'r') as names_file:
        line = names_file.readline()
        while line:
            if line in names:
                names[line] +=1
            else:
                names[line] = 1
            line = names_file.readline()
    print names 
