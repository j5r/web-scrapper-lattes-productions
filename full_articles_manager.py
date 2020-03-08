from Item import Item

def get_artigos_completos_publicados_em_periodicos(soup):
    itens = map(lambda item: item.find_all("div",{"class":"layout-cell-pad-5"})[-1],
            soup.find_all("div",{"class", "artigo-completo"}))

    lista_de_itens = []
    for item in itens:
        ans = Item()
        try: # tentando pegar o JCR
            ans.jcr = item.find("span",{"data-tipo-ordenacao":"jcr"}).text
        except:
            pass

        try: # tentando pegar o URL DOI
            ans.doi = item.find("a", {"class":"icone-producao icone-doi"})["href"]
        except:
            pass


        ans.ano = item.find("span",{"data-tipo-ordenacao":"ano"}).text
        ans.soup = item
        ans.cite = get_cite_para_item(item)
        lista_de_itens.append(ans)
    return lista_de_itens



def get_cite_para_item(item):
    #vamos tratar strings: encontrar o ano e pegar a string que vem
    #imediatamente depois
    anos = list(map(str,range(1900,2050))) # faixa de anos
    string = item.text
    for i in range(len(string)):
        teste = string[i:i+4]
        if teste in anos: # encontrando o primeiro ano dentro da string
            string = string[i+4:]
            return string



