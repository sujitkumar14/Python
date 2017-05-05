import requests
from bs4 import BeautifulSoup

if __name__=="__main__":
    urlPrime = "http://www.practicepython.org/assets/primenumbers.txt"
    urlHappy = "http://www.practicepython.org/assets/happynumbers.txt"
    rPrime = requests.get(urlPrime)
    rHappy = requests.get(urlHappy)
    soupPrime = BeautifulSoup(rPrime.text,"lxml")
    soupHappy = BeautifulSoup(rHappy.text,"lxml")
    listPrime = []
    listHappy = []
    dataPrime = soupPrime.find('p')
    dataHappy = soupHappy.find('p')
    #print dataPrime
    for line in dataPrime:
        listPrime = map(int,line.encode('utf-8').split('\n'))
       # print listPrime
    for line in dataHappy:
        listHappy = map(int,line.encode('utf-8').split('\n'))
    #print listPrime
    # print listHappy
    for i in range(0,len(listPrime)):
       # print listPrime[i]
       # print listHappy[i]
        if listPrime[i] in listHappy:
            print listPrime[i]
        
    
    
    
