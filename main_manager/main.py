import os
from bs4 import BeautifulSoup as BS
import os
from main_manager.Item import Item
import main_manager.full_articles_manager as full_art
import main_manager.excel_manager as excel_manager
#Identificação
#Formação acadêmica/titulação
#Pós-doutorado e Livre-docência
#Atuação Profissional
#Linhas de pesquisa
#Projetos de pesquisa
#Membro de corpo editorial
#Áreas de atuação
#Idiomas
#Prêmios e títulos
#Artigos completos publicados em periódicos ------- desenvolvendo
#Livros publicados/organizados ou edições
#Capítulos de livros publicados
#Trabalhos completos publicados em anais de congressos
#--Participação em bancas de trabalhos de conclusão
##Mestrado
##Teses de doutorado
#Qualificações de Doutorado
#Qualificações de Mestrado
#Trabalhos de conclusão de curso de graduação
#--Outros tipos
#--Participação em bancas de comissões julgadoras
##Concurso público
##Outras participações
#--Eventos
##Participação em eventos, congressos, exposições e feiras
##Organização de eventos, congressos, exposições e feiras
#Orientações
#--Orientações e supervisões em andamento
#Dissertação de mestrado
#--Orientações e supervisões concluídas
##Dissertação de mestrado
##Tese de doutorado
##Iniciação científica
#Inovação
#Projetos de pesquisa


def pega_arquivo_nk_e_faz_tudo(arquivo): #arquivo .nk
    #b 0: verificando se o arquivo é um arquivo .nk
    if not arquivo.endswith(".nk"):
        print(f'Arquivo {arquivo} não é um arquivo ".nk"!')
        return None
    #e 0: se o arquivo não é um arquivo .nk, retorna vazio



    #b 1: criando um BS; se houver erro na leitura do .nk retorna vazio
    try:
        arquivo_para_ler = open(arquivo,"rb")
        bs = BS(arquivo_para_ler.read().decode("latin8"),"html.parser")
        arquivo_para_ler.close()
    except Exception as e:
        print("ERRO!",e)
        return None
    #e 1: BS criado como "bs"


    #b 2: obtendo a lista de artigos completos
    itens_artigos_completos_publicados_em_periodicos = full_art.get_artigos_completos_publicados_em_periodicos(\
            bs.find("div",{"id":"artigos-completos"})
            )
    #e 2: o resultado é uma lista de "Item"


    #b 3: criar uma planilha com os itens
    excel_manager.criar_excel(arquivo, itens_artigos_completos_publicados_em_periodicos)
    #return itens_artigos_completos_publicados_em_periodicos
    #e 3:


    #b 4:
    #e 4:














def processar_arquivos_pastas_e_gerar_planilhas():
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
            pega_arquivo_nk_e_faz_tudo(arquivo)
    #e 3: uma planilha excel será gerada para cada arquivo .html
