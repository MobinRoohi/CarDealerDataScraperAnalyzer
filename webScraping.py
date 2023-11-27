from socket import socket
from bs4 import BeautifulSoup
import requests
from requests import Session



def tream(arr):
    if len(arr) == 0:
        return 'None'
    sum = arr[0]
    for i in range(1, len(arr)):
        sum += '-'
        sum += arr[i]
    return sum

def checkNums(string):
    for c in range(9):
        if str(c) in string:
            return 1
    return 0

def sendCarData():
    ses = Session()
    source = ses.post("http://utproject.ir/bp/login.php", data = {"username": "610300060", "password": "27424545250765406769" , "captcha": ''}).text
    lst = []
    x = True
    i = 0
    while source:    
        source = ses.get(f"http://utproject.ir/bp/Cars/page{i}.php").text
        bama = BeautifulSoup(source, 'lxml')
        for item in bama.find_all('li', class_="car-list-item-li list-data-main"):
            cars_dict = {}
            a = item.find('div', class_="car-func-details")
            karkard = a.find('span').text
            karkard = karkard.split()
            b = item.find('div', class_="title")
            car_name_split = b.a['href'].split('-')
            cars_dict['company'] = car_name_split[2]
            cars_dict['car'] = car_name_split[3]
            cars_dict['tream'] = tream(car_name_split[4:-1])
            if len(karkard) == 1:
                f = '0'
            else:
                if checkNums(karkard[1]):
                    v = karkard[1]
                    f = v.replace(',', '')
                else:
                    f = '0'
            cars_dict['kilometer'] = f
            cars_dict['year'] = car_name_split[-1]
            c = item.find('p', class_="cost")
            c = c.find('span')
            if c['content'] == 'IRR':
                d = '0'
            else:
                v = c['content']
                d = v.replace(',', '')
            cars_dict['price'] = d   
            lst.append(cars_dict)     
        i += 1
        source = ses.get(f"http://utproject.ir/bp/Cars/page{i}.php")
sendCarData()


    


 



