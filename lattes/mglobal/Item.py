"""Criando um modelo para armazenar dados"""
def azul(s):
    return "\033[97;1m"+str(s)+"\033[m"

def roxo(s):
    return "\033[95;1m"+str(s)+"\033[m"

class Item:
    def __init__(self):
        self.__ano = "--"
        self.__jcr = "--"
        self.__cite = "--"
        self.__doi = "--"
        self.__soup = "--"

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self,ano):
        self.__ano = str(ano)
        self.__ano = self.__ano.strip()

    @property
    def jcr(self):
        return self.__jcr

    @jcr.setter
    def jcr(self,jcr):
        self.__jcr = str(jcr)
        self.__jcr = self.__jcr.strip()

    @property
    def cite(self):
        return self.__cite

    @cite.setter
    def cite(self,cite):
        self.__cite = str(cite)
        self.__cite = self.__cite.strip()

    @property
    def doi(self):
        return self.__doi

    @doi.setter
    def doi(self,doi):
        self.__doi = str(doi)
        self.__doi = self.__doi.strip()

    @property
    def soup(self):
        return self.__soup

    @soup.setter
    def soup(self,soup):
        self.__soup = soup

    def __str__(self):
        return "\n" + azul("ano: ") + roxo(self.ano) \
            + azul("\njcr: ") + roxo(self.jcr)\
            + azul("\ndoi: ") + roxo(self.doi)\
            + azul("\ncite: ") + roxo(self.cite)\
            + azul("\nsoup: ") + roxo(self.soup) + "\n"
    def __repr__(self):
        return self.__str__()
