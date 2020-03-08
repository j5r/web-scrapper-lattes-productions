import os
import main_package


#b 0: listando todos os arquivos html na pasta atual
lista_de_arquivos_html = filter(lambda x: x.endswith(".html"), os.listdir())
#e 0: retorna uma lista de strings, os nomes dos arquivos


#b 1: renomeando os arquivos: a extensão .html será alterada para .nk
for arquivo in lista_de_arquivos_html:
    nome = arquivo.split("(")[1].split(")")[0].replace(" ","_") + ".nk"
    os.rename(arquivo, nome)
#e 1: o nome do arquivo será o nome entre parênteses, com _ no lugar de
#e 1:                                                           espaços
#e 1: Exemplo:
#e 1:   'Currículo do Sistema de Currículos Lattes (Junior Rodrigues Ribeiro).html'
#e 1: passa a ser Junior_Rodrigues_Ribeiro.nk


#b 2: listando os arquivos .nk presentes na pasta atual
lista_de_arquivos_nk = filter(lambda x: x.endswith(".nk"), os.listdir())
#e 2: uma lista de strings, os nomes dos arquivos.



#b *: deletando todas as demais pastas
pastas = list(os.walk("."))[0][1]
try:
    pastas.remove(".git")
except:
    pass
for pasta in pastas:
    os.system('rm -r "' + pasta + '"')
#e *: todas as pastas serão deletadas




#b 3: iterando sobre a lista de arquivos .nk
for arquivo in lista_de_arquivos_nk:
    main_package.pega_arquivo_nk_e_faz_tudo(arquivo)
#e 3: uma planilha excel será gerada para cada arquivo .html
