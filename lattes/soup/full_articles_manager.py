from lattes.mglobal.Item import Item

# principal função do programa com o objetivo de capturar os dados da seção
#----- Artigos completos publicados em periódicos -----
def get_itens(soup):
    #b 0: pegando a sopa de todos os 'Artigos completos publicados em periódicos'
    try:
        soup = soup.find("div",{"id":"artigos-completos"})
        itens = map(lambda item: item.find_all("div",{"class":"layout-cell-pad-5"})[-1],
                soup.find_all("div",{"class": "artigo-completo"}))
    except Exception as e:
        print("Erro!",e)
        return [Item()]
    #e 0: resultando em uma lista de sopas

    #b 1: criando 'Item's para retornar
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

        #b 2-0: pegando a citação para um dado artigo
        ans.cite = get_cite_para_item(item)
        #e 2-0: o resultado é uma string

        lista_de_itens.append(ans)
    #e 2: retornando uma lista de 'Item's
    return lista_de_itens



def get_cite_para_item(item):
    """vamos tratar strings: encontrar o ano e pegar a string que vem
    imediatamente depois"""


    #b 0: criando uma faixa de anos em que as citações se situam
    anos = list(map(str,range(1900,2050)))
    #e 0: o resultado é uma lista de strings

    string = item.text


    """Um exemplo da string de entrada

    2.624CHÁVEZ-FUENTES, JORGE R.2017CHÁVEZ-FUENTES, JORGE R. ;
    MAYTA, JORGE E. ; Costa, Eduardo F. ; TERRA, MARCO H. .
    Stochastic and exponential stability of discrete-time Markov
    jump linear singular systems. SYSTEMS & CONTROL LETTERS, v. 107,
    p. 92-99, 2017.

    doi+autor+ano+citação -> citação
    """

    #b 1: iterando os caracteres da string para encontrar um ano da lista
    for i in range(len(string)):
        teste = string[i:i+4]
        if teste in anos: # encontrando o primeiro ano dentro da string
            string = string[i+4:]
            return string
    #e 1: o resultado retornado é uma string



