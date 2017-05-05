import requests
from bs4 import BeautifulSoup

if __name__=="__main__":
    url = "https://www.flipkart.com/lenovo-k6-power-grey-dark-grey-32-gb/p/itmezenfhm4mvptw?pid=MOBEZENFZBPW8UMF&srno=b_1_1&otracker=hp_omu_Top%20Offers_1_Flat%20%E2%82%B91%2C000%20Off_049a4e02-faef-40cb-84be-1c00d356a77d_0&lid=LSTMOBEZENFZBPW8UMF7P8NY0"
    r = requests.get(url)
    print r.status_code
    soup = BeautifulSoup(r.text,"lxml")
    data = soup.find_all("div",{"class":"_2Kp3n6"})
    #print data
    
