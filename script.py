#Made By zSkiddoh
#Date Creation: 28/10/2021

#MÓDULOS
import requests
import time
import colorama
from colorama import *
import os

#LIMPIEZA DE PANTALLA
os.system("cls")

#API
proxies = requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all')

#CREACIÓN DEL FICHERO EN DONDE SE GUARDARÁN LOS PROXIES
with open('proxies.txt', 'wb') as fp:
    fp.write(proxies.content)

#PAUSA POR SEGUNDOS
print(Fore.WHITE + "[-]", Fore.YELLOW + "Buscando Proxies...")
time.sleep(8)

#LIMPIEZA DE PANTALLA 2
os.system("cls")

#MENSAJE DE LOS PROXIES CONSEGUIDOS
print(Fore.WHITE + "[+]", Fore.YELLOW + "Proxies Obtenidos Correctamente!")
print(Fore.WHITE + "[+]", Fore.YELLOW + "Guardados en el fichero >> proxies.txt")
