#!/usr/bin/python3

import requests,os,signal
from bs4 import BeautifulSoup
from colorama import Fore, init
init(autoreset=True)

# Script to find all urls in a web page.
# Autor: @federicocabreraf

# Class 
class Contador(object):
  def __init__(self, inicial=0):
    self.numero = inicial
  def siguiente(self):
    self.numero += 1
    return self.numero

# Function  

# Exit
def ctrl_c(sig,frame):
    print(Fore.RED +"\n\n\n[!] CTRL_C --> Saliendo\n\n")
    quit()
signal.signal(signal.SIGINT, ctrl_c)

# Get Url
def url(url):
  cant_url = Contador()
  url = ("http://"+url+"/")
  page = requests.get(url)
  soup = BeautifulSoup(page.content, "html.parser")
  for link in soup.find_all("a"):
    if link.get("href") != "#" and link.get("href") != None:
      print(Fore.BLUE+"\n[+] URL: "+link.get("href"))
      cant_url.siguiente()
  print(Fore.YELLOW+"\n[+] Total de direcciones web encontradas: "+str(cant_url.siguiente()))          

# Main
try:
  os.system("cls")
  while True:
    dir_url = input(Fore.RED+"\n[!] ctrl-c para salir."+Fore.RESET+"\n\nIngrese una direccion web (example: www.example.com): ")
    url(dir_url)
except:
  print(Fore.RED+"\n\n[+] URL: "+dir_url)
  print(Fore.RED+"\n[!] No se encontró nada.\n")






