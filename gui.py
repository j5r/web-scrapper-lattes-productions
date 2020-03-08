from tkinter import *
from tkinter.filedialog import askopenfilename as Open
import os


class Gui(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.option_add('*tearOff', FALSE)
        self.geometry("500x300")
        self.title("Lattes2Excel")

        if os.sys.platform == "linux":
            self.__comando = "xgd-open "
        else:
            self.__comando = "start "


        self.links = []
        self.nome_arquivo = "unknown.txt"

        barra_de_menus = Menu(self)
        self['menu'] = barra_de_menus

        menu_principal = Menu(barra_de_menus)
        menu_ajuda = Menu(barra_de_menus)

        barra_de_menus.add_cascade(menu=menu_principal, label='Menu')
        barra_de_menus.add_cascade(menu=menu_ajuda, label='Ajuda')

        menu_principal.add_command(label='Abrir...', command=self.abrir_arquivo)
        menu_principal.add_command(label='Novo Arquivo', command=None)

        menu_ajuda.add_command(label='Como usar', command=None)
        menu_ajuda.add_command(label='Sobre Lattes2Excel', command=None)


        self.mainloop()

    def abrir_arquivo(self):
        arquivo = Open()
        self.nome_arquivo = arquivo.split("/")[-1]
        f = open(arquivo,"r")
        self.links = list(map(lambda l: l.strip(),f.readlines()))
        f.close()
        print(self.links)

    def abrir_link(self, link):
        os.system(self.__comando + link)

Gui()
