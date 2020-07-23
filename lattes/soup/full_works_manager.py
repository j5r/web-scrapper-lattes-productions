from lattes.mglobal.Item import Item

# principal função do programa com o objetivo de capturar os dados da seção
#----- Artigos completos publicados em periódicos -----
def get_itens(soup):
    #b 0: pegando a sopa de todos os 'Artigos completos publicados em periódicos'
    try: #texto: Trabalhos completos publicados em anais de congressos
        itens_a = soup.find_all("a",{"name":"TrabalhosPublicadosAnaisCongresso"})
        itens = itens_a[0].parent.parent.findNextSiblings()
        for i in range(len(itens)):
            if itens[i].text == itens_a[1].parent.parent.text:
                itens = itens[0:i]
                break
        itens_ = []
        for i in itens:
            if len(i.text) > 10:
                itens_.append(i)
        itens = itens_

    except Exception as e:
        print("Erro!",e)
        return [Item()]
    #e 0: resultando em uma lista de sopas

    #b 1: criando 'Item's para retornar
    lista_de_itens = []
    for item in itens:
        ans = Item()

        try: # tentando pegar o URL DOI
            ans.doi = item.find("a", {"class":"icone-producao icone-doi"})["href"]
        except:
            pass

        ans.soup = item

        #b 2-0: pegando a citação e ano para um dado artigo
        ans = get_cite_e_ano_para_item(ans)
        #e 2-0: entra um Item e retorna um Item

        lista_de_itens.append(ans)
    #e 2: retornando uma lista de 'Item's
    return lista_de_itens



def get_cite_e_ano_para_item(item):
    """vamos tratar strings: encontrar o ano e pegar a string que vem
    imediatamente depois"""


    #b 0: criando uma faixa de anos em que as citações se situam
    anos = list(map(str,range(1900,2050)))
    #e 0: o resultado é uma lista de strings

    string = item.soup.text.strip()


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
        ano_teste = string[i:i+4]
        if ano_teste in anos: # encontrando o primeiro ano dentro da string
            item.ano = ano_teste
            item.cite = string
            return item
    return item
    #e 1: o resultado retornado é uma string



