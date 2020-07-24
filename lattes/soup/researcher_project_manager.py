

# principal função do programa com o objetivo de capturar os dados da seção
#----- Participação em bancas de trabalhos de conclusão -----
def get_itens(soup):
    def year_or_self(string):
        lista_de_anos = [str(ano) for ano in range(1980,2050)]
        for ano in lista_de_anos:
            if ano in string:
                return 1
        return 0
    #b 0: pegando a sopa de todos os 'Artigos completos publicados em periódicos'
    try: #texto: Trabalhos completos publicados em anais de congressos
        itens_a = soup.find_all("a",{"name":"ProjetosPesquisa"})
        itens_a_parent = itens_a[0].findParent()
        DOM_ITEMS = list(itens_a_parent.children)
        ITEMS = []



        try:
            for item in DOM_ITEMS:
                try:
                    if set(["layout-cell", "layout-cell-12", "data-cell"]).issubset(
                        set(item["class"])
                        ):
                        parent = item
                        break
                except Exception as e:
                    print("Warn[ok]",e)

            
            
            ############################
            nodes = parent.find_all("div",class_="layout-cell-pad-5")
            new_item = None
            for item in nodes:
                texto = " ".join(item.get_text().split()).strip()
                if year_or_self(texto) and len(texto)<15:
                    ITEMS.append(new_item)
                    new_item = [texto]
                else:
                    new_item.append(texto)
                    try:
                        new_item.remove('')
                    except:
                        pass
            ITEMS.append(new_item)   
            ITEMS.remove(None)
            

            return ITEMS
        except Exception as e:
            print("Error!",e)
            return []

    except Exception as e:
        print("Erro[unknown]",e)
        ITEMS = []
    return ITEMS





