import requests
from colorama import Fore, Back, Style
from colorama import init
import sys
from time import sleep

words = '''
  /$$$$$$  /$$$$$$ /$$      /$$ /$$$$$$       /$$$$$$ /$$   /$$ /$$$$$$$$/$$$$$$ 
 /$$__  $$|_  $$_/| $$  /$ | $$|_  $$_/      |_  $$_/| $$$ | $$| $$_____/$$__  $$
| $$  \ $$  | $$  | $$ /$$$| $$  | $$          | $$  | $$$$| $$| $$    | $$  \ $$
| $$  | $$  | $$  | $$/$$ $$ $$  | $$          | $$  | $$ $$ $$| $$$$$ | $$  | $$
| $$  | $$  | $$  | $$$$_  $$$$  | $$          | $$  | $$  $$$$| $$__/ | $$  | $$
| $$/$$ $$  | $$  | $$$/ \  $$$  | $$          | $$  | $$\  $$$| $$    | $$  | $$
|  $$$$$$/ /$$$$$$| $$/   \  $$ /$$$$$$       /$$$$$$| $$ \  $$| $$    |  $$$$$$/
 \____ $$$|______/|__/     \__/|______/      |______/|__/  \__/|__/     \______/ 
      \__/                                                                       
                                                                                 
                                      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
                                      |T|G|:| |@|H|A|C|K|E|R|_|P|H|O|N|E|_|V|I|P|
                                      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
'''
for char in words:
    sleep(0.005)
    sys.stdout.write(char)
    sys.stdout.flush()

token = input("\n► Введите токен: ")

if token == "":
  print("\n‼️ Введите токен!")
  quit()

session = requests.Session()
session.headers['Accept']= 'application/json'
session.headers['authorization'] = 'Bearer ' + token

try:
 req = session.get("https://edge.qiwi.com/person-profile/v1/profile/current?authInfoEnabled=true&contractInfoEnabled=true&userInfoEnabled=true").json()
 print("\n✔ Информация получена!")
 print("Номер телефона: +" + str(req['contractInfo']['contractId']))
 print("Никнейм: qiwi.com/n/" + req['contractInfo']["nickname"]["nickname"])
 print("Дата создания кошелька: " + req['contractInfo'] ['creationDate'])
 print("IP: " + req["authInfo"]["ip"])
 print("Привязаная почта: " + req["authInfo"]["boundEmail"])
 try:
  req2 = session.get("https://edge.qiwi.com/identification/v1/persons/" + str(req['contractInfo']['contractId']) + "/identification").json()
  print("\n★ Паспортные данные")
  print("Ф/И/О: " + req2["firstName"] + " " + req2["lastName"])
  print("Дата рождения: " + req2["birthDate"])
  print("Серия и номер: " + req2["passport"])
  print("ИНН: " + req2["inn"] + '\n')
 except:
  print("\n⛔️ Произошла ошибка при получении паспортных данных!")
except:
 print("\n⛔️ Произошла ошибка!")

