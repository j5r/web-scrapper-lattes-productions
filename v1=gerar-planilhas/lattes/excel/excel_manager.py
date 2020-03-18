from openpyxl import Workbook as WB
from lattes.mglobal.configs import JSON





def artigos_completos(arquivo, itens, wb):
    # nome das colunas da planilha excel gerada
    colunas_full_articles = JSON["excel"]["full_articles_columns"]


    full_articles = JSON["excel"]["full_articles_sheet_name"]
    wb.create_sheet(full_articles)
    FULL_ARTICLES = wb.get_sheet_by_name(full_articles)

    try: #tentando excluir a folha padrão "Sheet"
        wb.remove(wb.get_sheet_by_name("Sheet"))
    except Exception as e:
        print(e)

    FULL_ARTICLES.append(colunas_full_articles)


    for i in range(len(itens)):
        linha = [
            i+1,
            itens[i].ano,
            itens[i].jcr,
            itens[i].doi,
            itens[i].cite,
        ]
        FULL_ARTICLES.append(linha)



def trabalhos_completos(arquivo, itens, wb):
    # nome das colunas da planilha excel gerada
    colunas_full_works = JSON["excel"]["full_works_columns"]

    full_works = JSON["excel"]["full_works_sheet_name"]
    wb.create_sheet(full_works)
    FULL_WORKS = wb.get_sheet_by_name(full_works)

    try: #tentando excluir a folha padrão "Sheet"
        wb.remove(wb.get_sheet_by_name("Sheet"))
    except Exception as e:
        print(e)

    FULL_WORKS.append(colunas_full_works)

    for i in range(len(itens)):
        linha = [
            i+1,
            itens[i].ano,
            itens[i].jcr,
            itens[i].doi,
            itens[i].cite,
        ]
        FULL_WORKS.append(linha)




