

# principal função do programa com o objetivo de capturar os dados da seção
#----- Participação em bancas de trabalhos de conclusão -----
def get_itens(soup):
    #b 0: pegando a sopa de todos os 'Artigos completos publicados em periódicos'
    try: #texto: Trabalhos completos publicados em anais de congressos
        itens_a = soup.find_all("a",{"name":"ParticipacaoBancasTrabalho"})
        itens_a_parent = itens_a[0].findParent()
        itens_div = itens_a_parent.find_all("div",class_="layout-cell-pad-5")
        print(len(itens_div))
        lista_de_itens = []
        for item in itens_div:
            if len(item["class"])==1:
                texto = item.get_text()
                texto = " ".join(texto.split())
                lista_de_itens.append(texto)
    except Exception as e:
        print("Erro!",e)
        lista_de_itens = []
    #e 0: resultando em uma lista de strings
    return lista_de_itens


