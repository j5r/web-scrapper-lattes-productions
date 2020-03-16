from openpyxl import Workbook as WB
import json
import os
f = open("./main_manager/configs.json","rb")
getJSON = f.read()
f.close()
JSON = json.loads(getJSON)


def criar_excel(arquivo, fll_articles, fll_works):
    #espera-se um arquivo ".nk"
    arquivo = arquivo[:arquivo.find(".nk")] + ".xlsx"

    # nome das colunas da planilha excel gerada
    colunas_full_articles = JSON["excel"]["full_articles_columns"]
    colunas_full_works = JSON["excel"]["full_works_columns"]


    # criando um Workbook
    wb = WB()

    full_articles = JSON["excel"]["full_articles_sheet_name"]
    wb.create_sheet(full_articles)
    FULL_ARTICLES = wb.get_sheet_by_name(full_articles)


    full_works = JSON["excel"]["full_works_sheet_name"]
    wb.create_sheet(full_works)
    FULL_WORKS = wb.get_sheet_by_name(full_works)


    try: #tentando excluir a folha padrão "Sheet"
        wb.remove(wb.get_sheet_by_name("Sheet"))
    except Exception as e:
        print(e)

    FULL_ARTICLES.append(colunas_full_articles)
    FULL_WORKS.append(colunas_full_works)


    # processamento ----------------
    for i in range(len(fll_articles)):
        linha = [
            i+1,
            fll_articles[i].ano,
            fll_articles[i].jcr,
            fll_articles[i].doi,
            fll_articles[i].cite,
        ]
        FULL_ARTICLES.append(linha)


    for i in range(len(fll_works)):
        linha = [
            i+1,
            fll_works[i].ano,
            fll_works[i].jcr,
            fll_works[i].doi,
            fll_works[i].cite,
        ]
        FULL_WORKS.append(linha)
    wb.save(arquivo)



