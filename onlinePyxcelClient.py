from socket import socket
from bs4 import BeautifulSoup
import requests
from requests import Session
import socket
import json
import pandas as pd

def header_creator(lst):
    lst = ['create(cars, 6, 1)', 'context(cars)']
    a = ['company', 'car', 'tream', 'kilometer', 'year', 'price']
    b = ['A', 'B', 'C', 'D', 'E', 'F']
    for i in range(len(a)):
        lst.append(f'{b[i]}1 = {a[i]}')
    lst.append('display(cars)')
    return lst

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
        if i % 10 == 0 and i > 0:
            lst = pyxcelInput(lst)
            sendMessage(lst)
            # send lst to server
            lst = []
        i += 1
        source = ses.get(f"http://utproject.ir/bp/Cars/page{i}.php")
    lst = pyxcelInput(lst)
    sendMessage(lst)

def pyxcelInput(lst):
    temp = [f'create(temp, 6, {len(lst)})', 'context(temp)']
    for i in range(len(lst)):
        temp.append(f'A{i + 1} = ' + lst[i]['company'])
        temp.append(f'B{i + 1} = ' + lst[i]['car'])
        temp.append(f'C{i + 1} = ' + lst[i]['tream'])
        temp.append(f'D{i + 1} = ' + lst[i]['kilometer'])
        temp.append(f'E{i + 1} = ' + lst[i]['year'])
        temp.append(f'F{i + 1} = ' + lst[i]['price'])
    temp.append('display(cars)')
    return temp
    

def receiveMessage():
    num = int(sock.recv(max_req_size).decode(FORMAT))
    return json.loads(sock.recv(num).decode(FORMAT)) 

def sendMessage(inp):
    dump = json.dumps(inp)
    dump = f"{len(dump):<{max_req_size}}" + dump
    sock.send(bytes(dump, FORMAT))

PORT = 9999
FORMAT = 'utf-8'
max_req_size = 5

sock = socket.socket()
sock.connect(('localhost', PORT))
print(receiveMessage())
header = header_creator([])
sendMessage(header)
sendCarData()
# now we send a message to server to get back our matrix!
array = ['return']
sendMessage(array)
x = True
matrix = receiveMessage()
while x != 'transfer complete':
    x = receiveMessage()
    if x != 'transfer complete':
        matrix += x
print(matrix)
print(len(matrix))
for i in range(len(matrix)):
    for j in range(3, len(matrix[0])):
        if matrix[i][j] == '0':
            matrix[i][j] = matrix[i][j]
        else:
            matrix[i][j] = int(matrix[i][j])