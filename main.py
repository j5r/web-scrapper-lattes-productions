import os
import main_package

lista_de_arquivos_html = filter(lambda x: x.endswith(".html"), os.listdir())


for arquivo in lista_de_arquivos_html:
    nome = arquivo.split("(")[1].split(")")[0].replace(" ","_") + ".nk"
    os.rename(arquivo, nome)


lista_de_arquivos_nk = filter(lambda x: x.endswith(".nk"), os.listdir())



for i in lista_de_arquivos_nk:
    main_package.pega_arquivo_nk_e_faz_tudo(i)

