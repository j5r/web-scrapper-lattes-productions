
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
            contador += 1
            # Uma tupla com os itens interessantes
            self.__producoes.append(
                (contador,
                Producoes.__getDoiFromProducoesItem(soup),
                soup,
                    )
            )
        self.__answer_builded = 1


    def get(self):
        """retorna uma tupla"""
        if not self.__answer_builded:
            self.__BuildAnswer()
        return self.__producoes


    def __getDoiFromProducoesItem(producoesItem):
        """retorna o http://doi.dx/..."""
        try:
            doiUrl = producoesItem.find("a",\
                    {"class":"icone-producao icone-doi"}
                    )["href"]
        except Exception as e:
            #print(e)
            return None
        return doiUrl.strip()











eduardo = Producoes(eduardo)
