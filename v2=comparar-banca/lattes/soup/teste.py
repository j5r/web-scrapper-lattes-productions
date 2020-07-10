from bs4 import BeautifulSoup as BS
import exam_commissions_manager as EM

file_html = open("/home/junior/web-scrapper-lattes-productions/v2=comparar-banca/download_paginas_lattes_aqui_teste/Eduardo_Fontoura_Costa.nk","rb")
bs = BS(file_html.read().decode("latin8"),"html.parser")
file_html.close()

print(EM.get_itens(bs))
