from bs4 import BeautifulSoup as BS
from editorial_member_manager import *

f = open("../../download_paginas_lattes_aqui_teste/Currículo do Sistema de Currículos Lattes (Eduardo Fontoura Costa).html","rb")
soup = BS(f.read().decode("latin8"),"html.parser")
f.close()

DOM_ITEMS = get_itens(soup)


for i in DOM_ITEMS:
    try:
        print("\033[93;1m",i.prettify(),"\n","\033[m","-"*20,type(i),i["class"],"\n")
    except:
        print("\033[94;1m",i,"\n","\033[m","-"*20,type(i),"\n")

