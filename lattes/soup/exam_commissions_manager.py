

# principal função do programa com o objetivo de capturar os dados da seção
#----- Participação em bancas de trabalhos de conclusão -----
def get_itens(soup):
    lista_de_anos = [str(ano) for ano in range(1980,2050)]
    #b 0: pegando a sopa de todos os 'Artigos completos publicados em periódicos'
    try: #texto: Trabalhos completos publicados em anais de congressos
        itens_a = soup.find_all("a",{"name":"ParticipacaoBancasTrabalho"})
        itens_a_parent = itens_a[0].findParent()
        DOM_ITEMS = list(itens_a_parent.children)
        ITEMS = []

        tipo_a_de_banca = "--"
        tipo_b_de_banca = "--"


        for item in DOM_ITEMS:
            try:
                if "inst_back" in item["class"]:
                    tipo_a_de_banca = item.get_text()
                elif "cita-artigos" in item["class"]:
                    tipo_b_de_banca = item.get_text()
                else:
                    if item.div is not None:
                        if "layout-cell-pad-5" in item.div["class"] and len(item.div["class"])==1:
                            texto = item.div.get_text()
                            for ano in lista_de_anos:
                                if ano in texto:
                                    the_ano = ano
                                    break
                                else:
                                    the_ano = "--"
                            novo_item = (tipo_a_de_banca.strip(),
                                        tipo_b_de_banca.strip(),
                                        the_ano.strip(),
                                        " ".join(texto.split())
                                        )
                            ITEMS.append(novo_item)
            except:
                pass
        return ITEMS





#        itens_div = itens_a_parent.find_all("div",class_="layout-cell-pad-5")
#        print(len(itens_div))
#        lista_de_itens = []
#        for item in itens_div:
#            if len(item["class"])==1:
#                texto = item.get_text()
#                texto = " ".join(texto.split())
#                lista_de_itens.append(texto)
    except Exception as e:
        print("Erro!",e)
        ITEMS = []
    #e 0: resultando em uma lista de strings
    return ITEMS






# div class inst_back > b: Participação em bancas de trabalhos de conclusão
# div class cita-artigos > b: Mestrado
# ano
