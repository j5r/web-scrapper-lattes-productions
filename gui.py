from tkinter import *
from tkinter.filedialog import askopenfilename as Open
import os


class Gui(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.option_add('*tearOff', FALSE)
        self.geometry("500x300")
        self.title("Lattes2Excel")
        self.fonte = ("Arial",14,"bold")

        if os.sys.platform == "linux":
            self.__comando = "xgd-open "
        else:
            self.__comando = "start "


        self.links = []
        self.nome_arquivo = "unknown.txt"
        self.links_as_texto = ""

        barra_de_menus = Menu(self)
        self['menu'] = barra_de_menus

        menu_principal = Menu(barra_de_menus)
        menu_ajuda = Menu(barra_de_menus)

        barra_de_menus.add_cascade(menu=menu_principal, label='Menu')
        barra_de_menus.add_cascade(menu=menu_ajuda, label='Ajuda')

        menu_principal.add_command(label='Abrir...', command=self.abrir_arquivo)
        menu_principal.add_command(label='Novo Arquivo', command=self.novo_arquivo)

        menu_ajuda.add_command(label='Como usar', command=None)
        menu_ajuda.add_command(label='Sobre Lattes2Excel', command=None)

        self.lnome_arquivo = Label(self,text="Arquivo",width=15)
        self.lnome_arquivo.pack(side=RIGHT)
        self.lnnome_arquivo = Label(self,text=self.nome_arquivo)
        self.lnnome_arquivo.pack()
        self.lnnome_arquivo["fg"] = "#f00"
        self.lnnome_arquivo["bg"] = "#fdd"

        self.text_area = Text(self, width=55,height=12)


        self.mainloop()

    def abrir_arquivo(self):
        arquivo = Open()
        self.nome_arquivo = arquivo.split("/")[-1]
        f = open(arquivo,"r")
        self.links = list(map(lambda l: l.strip(),f.readlines()))
        self.links_as_texto = "\n".join(self.links)
        f.close()
        self.novo_arquivo()
        self.lnnome_arquivo["text"] = self.nome_arquivo
        print(self.links_as_texto)

    def abrir_link(self, link):
        os.system(self.__comando + link)

    def novo_arquivo(self):
        self.text_area.pack()
        self.text_area.insert(0.0,self.links_as_texto)

        self.salvar_avancar = Button(self,)


Gui()
