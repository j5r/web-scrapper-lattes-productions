"""
O CHROMEDRIVER pode ser obtido no link
    https://chromedriver.chromium.org/downloads
Seu Chrome deve ser de versão mínima compatível com a versão do
CHROMEDRIVER. Confira a versão do seu Chrome em
    Configurações -> Sobre o Google Chrome
Se seu Chrome estiver desatualizado, considere atualizá-lo.

Ao terminar a etapa acima, configure o próximo parâmetro com o endereço
do executável em sua máquina.
"""

from selenium import webdriver
from tkinter import Tk, Button, Label
import shelve
from time import sleep

chrome_driver_address_of_executable = "/home/junior/chromedriver"
lattes = "http://buscatextual.cnpq.br/buscatextual/visualizacv.do?metodo=apresentar&id=K4787743D1"
teste = "https://github.com/j5r/web-scrapper-lattes-productions"






class LattesHTML:
    def __init__(self,**kw):
        kw.setdefault("url",None)
        kw.setdefault("cdriver","/home/junior/chromedriver")

        if kw["url"] is None:
            msg = "You must to give a lattes-page url with\n\t"
            msg += "LattesHTML(url=theUrl, cdriver=ChromeDriverDirectory)"
            raise SyntaxError(msg)

        # 0: File Name for temporary file (file to save the main data)
        kw.setdefault("filename",kw["url"].split("id=")[1])
        if not kw["filename"].endswith(".shelve"):
            kw["filename"] += ".shelve"
        self.__file_name = kw["filename"]
        ####

        self.__kw = kw


    def init(self):
        kw = self.__kw
        # 1: Browser
        self.browser = webdriver.Chrome(kw["cdriver"])
        self.browser.get(kw["url"])
        ####

        # 2: GUI
        self.tk = Tk()
        self.tk.geometry("450x100+50+50")
        self.msg = Label(self.tk)
        self.msg["text"] = "Quando conseguir logar, clique neste botão."
        self.msg.pack()
        self.button = Button(self.tk)
        self.button["text"] = "Pronto!"
        self.button["command"] = self.__quitGUI
        self.button.pack()
        self.tk.mainloop()
        print("Getting the page and saving into a <shelve> file.")
        ####

        # 3: Data
        page = self.browser.page_source
        url = self.browser.current_url
        self.__db = shelve.open(self.__file_name)
        self.__db["lattes"] = page
        self.__db["url"] = url
        self.__db.close()
        ####

        self.__quitBROWSER()

    def getPage(self):
        self.__db = shelve.open(self.__file_name)
        ans = self.__db["lattes"]
        self.__db.close()
        return ans

    def getUrl(self):
        self.__db = shelve.open(self.__file_name)
        ans = self.__db["url"]
        self.__db.close()
        return ans

    def __quitGUI(self):
        print("Wait a moment. . .")
        sleep(5)
        self.tk.destroy()

    def __quitBROWSER(self):
        self.browser.quit()

