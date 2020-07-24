from openpyxl import Workbook as WB
from lattes.excel.excel_manager import (
                        artigos_completos as FULLARTS,
                        trabalhos_completos as FULLWORKS,
                        participacao_bancas_trabalhos_conclusao as EXAMCOMMISSION,
                        membro_editorial as EDITORIALMEMBER,
                        revisor_de_periodico as EDITORIALREVIEWER,
                        projetos_pesquisa as RESEARCHPROJECTS
                    )


class XL:
    def __init__(self, arquivo):
        #espera-se um arquivo ".nk"
        self.arquivo = arquivo[:arquivo.find(".html")] + ".xls"

        # criando um Workbook
        self.wb = WB()

    def save(self):
        self.wb.save(self.arquivo)


    def artigos_completos(self, itens):
        FULLARTS(self.arquivo, itens, self.wb)

    def trabalhos_completos(self, itens):
        FULLWORKS(self.arquivo, itens, self.wb)

    def bancas(self, itens):
        EXAMCOMMISSION(self.arquivo, itens, self.wb)

    def membro_editorial(self, itens):
        EDITORIALMEMBER(self.arquivo, itens, self.wb)

    def revisor_de_periodico(self,itens):
        EDITORIALREVIEWER(self.arquivo, itens, self.wb)

    def projetos_pesquisa(self,itens):
        RESEARCHPROJECTS(self.arquivo, itens, self.wb)



