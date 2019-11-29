
from lattes import *


class Producoes:
    def __init__(self,lattesbs):
        self.__soup = lattesbs.get()
        self.__soup_list = lattesbs.get().find("div",
                    {"id":"artigos-completos"}
                    ).find_all("div",
                    {"class":"artigo-completo"}
                )
        self.__answer_builded = 0
        self.__producoes = []


    def getSoupList(self):
        """Obtém uma lista com todos os soups dos artigos"""
        return self.__soup_list


    def __BuildAnswer(self):
        """Constrói a resposta: uma tupla com os itens interessantes"""
        ls = self.getSoupList()
        contador = 0
        for soup in ls:
            soup = soup.div.find_next_sibling("div").div
            soup.div.clear()
            contador += 1
            # Uma tupla com os itens interessantes
            self.__producoes.append(
                {"item": contador,
                "doi":Producoes.__getDoiFromProducoesItem(soup),
                "ano":Producoes.__getAnoFromProducoesItem(soup),
                "jcr":Producoes.__getJCRFromProducoesItem(soup),
                "text":Producoes.__gettext__(soup),
                "soup":soup,
                    }
            )
        self.__answer_builded = 1


    def get(self):
        """retorna uma tupla"""
        if not self.__answer_builded:
            self.__BuildAnswer()
        return self.__producoes


    def __getDoiFromProducoesItem(soup):
        """retorna o http://doi.dx/..."""
        try:
            doiUrl = soup.find("a",\
                    {"class":"icone-producao icone-doi"}
                    )["href"]
        except Exception as e:
            #print(e)
            return None
        return doiUrl.strip()


    def __getAnoFromProducoesItem(soup):
        try:
            ano = soup.find("span",
                    {"data-tipo-ordenacao":"ano"}
                    ).string
        except Exception as e:
            #print(e)
            return None
        return ano.strip()


    def __getJCRFromProducoesItem(soup):
        try:
            jcr = soup.find("span",
                    {"data-tipo-ordenacao":"jcr"}
                    ).string
        except Exception as e:
            #print(e)
            return None
        return jcr.strip()

    def __gettext__(soup):
        for i in soup.find_all("span"):
            try:
                i.clear()
            except Exception as e:
                #print(e)
                return None
        return soup.getText().strip()




eduardosoup = Producoes(eduardo)
