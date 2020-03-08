from openpyxl import Workbook as WB

# nome das colunas da planilha excel gerada
colunas = [
"Counter",
"Year",
"JCR",
"DOI",
"Cite",
]


def criar_excel(arquivo, itens): #espera-se um arquivo ".nk"
    arquivo = arquivo[:arquivo.find(".nk")] + ".xlsx"

    wb = WB()
    wb.create_sheet("lattes")


    try: #tentando excluir a folha padrão "Sheet"
        wb.remove(wb.get_sheet_by_name("Sheet"))
    except Exception as e:
        print(e)


    lattes = wb.get_sheet_by_name("lattes")
    lattes.append(colunas)


    for i in range(len(itens)):
        linha = [
            i+1,
            itens[i].ano,
            itens[i].jcr,
            itens[i].doi,
            itens[i].cite,
        ]
        lattes.append(linha)
    wb.save(arquivo)



