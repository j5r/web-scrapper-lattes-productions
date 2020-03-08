from bs4 import BeautifulSoup as BS
import os
from Item import Item
import full_articles_manager as full_art
import excel_manager
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


    #b 5:
    #e 5:


    #b 6:
    #e 6:


    #b 7:
    #e 7:


    #b 8:
    #e 8:


    #b 9:
    #e 9:


    #b 10:
    #e 10:


    #b 11:
    #e 11:


    #b 12:
    #e 12:


    #b 13:
    #e 13:
