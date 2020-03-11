from tkinter import *
from tkinter.filedialog import askopenfilename as Open
from tkinter.filedialog import asksaveasfile as Save
import os


class Gui(Tk):
    def __init__(self):
        #b 0: inicializando classe e criando parâmetros
        Tk.__init__(self)
        self.option_add('*tearOff', FALSE) #tira ---- da barra de menu
        self.geometry("800x300")
        self.title("Lattes2Excel")
        self.fonte = ("Arial",14,)

        if os.sys.platform == "linux":
            #comando para executar um url no navegador: http://...
            self.__comando = "xdg-open " #linux
        else:
            self.__comando = "start " #windows
        #e 0: parâmetros inicializados

        #b 1: criando as variáveis internas da gui
        self.url_list = []
        self.nome_arquivo = "sem_nome.urls"
        self.file_text = ""
        self.caminho = ""
        self.nome_pasta = "download_paginas_lattes_aqui"
        #e 1: as variáveis serão atualizadas para controle do programa

        #b 2: declarando contêineres
        self.fr1 = Frame(self)
        self.fr1["pady"] = 15
        self.fr1.pack()

        self.fr2 = Frame(self)
        self.fr2["pady"] = 15
        self.fr2.pack()

        self.fr3 = Frame(self)
        self.fr3["pady"] = 15
        self.fr3.pack()
        #e 2: contêineres criados

        #b 3: criando widgets: sempre começam com a letra do seu tipo
        #b ..0: barra de menus
        m_barra_de_menus = Menu(self)
        self['menu'] = m_barra_de_menus

        m_menu_principal = Menu(m_barra_de_menus)
        m_barra_de_menus.add_cascade(
                    menu=m_menu_principal,
                    label='Menu',
                    font = self.fonte,
                    )

        m_menu_ajuda = Menu(m_barra_de_menus)
        m_barra_de_menus.add_cascade(
                    menu=m_menu_ajuda,
                    label='Ajuda',
                    font = self.fonte,
                    )
        #e ..0: barra de menus

        #b ..1: opções dos menus MENU e AJUDA
        m_menu_principal.add_command(
                    label='Abrir...',
                    command=self.cll_abrir_arquivo,
                    font = self.fonte,
                    )
        m_menu_principal.add_command(
                    label='Novo Arquivo',
                    command=self.cll_novo_arquivo,
                    font = self.fonte,
                    )

        m_menu_ajuda.add_command(
                    label='Como usar',
                    command=None,
                    font = self.fonte,
                    )
        m_menu_ajuda.add_command(
                    label='Sobre Lattes2Excel',
                    command=None,
                    font = self.fonte,
                    )
        #e ..1: opções dos menus adicionadas

        #b ..2: widgets do frame 1
        self.l_arquivo = Label(
                    self.fr1,
                    text="Arquivo",
                    width=12,
                    font = self.fonte,
                    )
        self.l_arquivo.grid(row=0,column=0)

        self.l_nome_arquivo = Label(
                    self.fr1,
                    text=self.nome_arquivo,
                    font = self.fonte,
                    )
        self.l_nome_arquivo.grid(row=0,column=1)
        self.l_nome_arquivo["fg"] = "#f00"
        self.l_nome_arquivo["bg"] = "#fdd"
        #e ..2: widgets do frame 1

        #b ..3: área de texto no frame 2
        self.t_text_area = Text(
                    self.fr2,
                    width=70,
                    height=8,
                    insertwidth = 10,
                    font = ("Courier", 12)
                    )
        #e ..3: será lançada apenas pelo menu ABRIR ou NOVO

        #b ..4: botões no frame 3
        self.b_salvar_avancar = Button(
                    self.fr3,
                    command = self.cll_salvar_avancar,
                    text = "Salvar e Avançar",
                    fg = "#fff",
                    font = self.fonte,
                    bg = "#46f"
                    )

        #e ..4: botões no frame 3
        #e 3:


        #b 4: executando loop infinito
        self.mainloop()
        #e 4: loop infinito

    def cll_abrir_arquivo(self):
        #b 0: abrindo arquivo
        arquivos = [('Documento de texto', '*.urls')]
        caminho_arquivo = Open(
                        filetypes = arquivos,
                        defaultextension = arquivos,
                        )
        #e 0: obtemos uma string com o caminho completo do arquivo

        #b 1: se a abertura do arquivo for cancelada (string vazia)
        if len(caminho_arquivo) == 0:
            return None
        #e 1: encerramos a função sem fazer mais nada

        #b 2: pegando nome do arquivo para colocar no label
        self.nome_arquivo = caminho_arquivo.split("/")[-1]
        f = open(caminho_arquivo,"r")
        self.url_list = list(
                    map(lambda l: l.strip(),
                        f.readlines(),
                        )
                    )
        self.links_as_texto = "\n".join(self.url_list)
        f.close()
        #e 2: os links estão em self.url_list

        #b 3: chama a interface de novo arquivo
        self.cll_novo_arquivo()
        self.l_nome_arquivo["text"] = self.nome_arquivo
        self.t_text_area.insert(0.0,self.links_as_texto)
        #e 3: interface completamente lançada

    def cll_abrir_link(self, link):
        os.system(self.__comando + link)

    def cll_novo_arquivo(self):
        #b 0: limpando a text_area e colocando nela o foco
        self.t_text_area.delete(0.0,END)
        self.t_text_area.pack()
        self.t_text_area.focus()
        self.b_salvar_avancar.pack()
        #e 0: a text_area e o botão salvar_avanca foram lançados em tela

    def cll_salvar_avancar(self):
        #b 0: abrir uma janela para salvar arquivo
        arquivos = [('Documento de texto', '*.urls')]
        try: #tenta salvar arquivo, senão encerra a função sem fz nada
            arquivo = Save(
                        filetypes = arquivos,
                        defaultextension = arquivos,
                        )
        except Exception as e:
            print("Erro!",e)
            return None

        if arquivo is None: #se o salvamento foi cancelado, encerra fç
            return None
        #e 0: "arquivo" é um file cujo name é todo o caminho do arquivo


        #b 1: apaga a caixa de texto
        self.t_text_area.forget()
        #e 1: a caixa de texto desapareceu, mas ainda esta em memoria


        #b 2: escrevendo o conteúdo no arquivo que foi "salvo"
        arquivo.write(self.t_text_area.get(0.0,END))
        caminho_arquivo = "/".join(arquivo.name.split("/")[:-1])
        nome_arquivo = arquivo.name.split("/")[-1]
        arquivo.close()
        #e 2: o nome do arquivo e o seu caminho foram capturados


        #b 3: abrindo o arquivo com as eventuais modificações
        arquivo = open(nome_arquivo,"r")
        self.url_list = list(
                    map(lambda l: l.strip(),
                        arquivo.readlines(),
                        )
                    )
        arquivo.close()
        #e 3: os links contidos no arquivo são salvos em self.url_list


        #b 4: uma pasta é criada neste diretório
        self.caminho = caminho_arquivo
        os.chdir(self.caminho)
        try:
            os.mkdir(self.nome_pasta)
        except:
            pass
        finally:
            os.chdir(self.nome_pasta)
        #e 4: entramos na nova pasta

        #b 5: adicionando novos botões: número de links e avançar
        self.call_avancar()
        #e 5: preparando para a execução final

    def call_avancar(self):
        #b 0: apagando o borão de avançar
        self.b_salvar_avancar.destroy()
        #e 0:

        #b 1: adicionando botão: número de links e abrir links
        self.l_numero_links = Label(#label
                    self.fr2,
                    text = "Quantos links abrir: ",
                    font = self.fonte,
                    )
        self.l_numero_links.pack(side=LEFT)

        self.e_numero_links = Entry(
                    self.fr2,
                    font = self.fonte,
                    width = 10,
                    )
        self.e_numero_links.insert(0,"7")
        self.e_numero_links.pack()

        self.b_abrir = Button(
                    self.fr3,
                    text = "Abrir links",
                    command = self.call_abrir_no_navegador,
                    fg = "#fff",
                    font = list(self.fonte) + ["bold"],
                    bg = "#46f"
                    )
        self.b_abrir.pack()
        #e 1: botões criados

    def call_abrir_no_navegador(self):

        try:
            numero_de_links_para_abrir = int(self.e_numero_links.get())
        except Exception as e:
            print("Erro!", e)
            self.call_abrir_mensagem_erro_Apenas_Numeros_Inteiros()
            return None

        for i in range(numero_de_links_para_abrir):
            try:
                url = self.url_list.pop()
                print(url)
                os.system(self.__comando + url)
            except Exception as e:
                print(e)
                self.call_fim_do_programa()






    def call_abrir_mensagem_erro_Apenas_Numeros_Inteiros(self):
        pass

    def call_fim_do_programa(self):
        pass




Gui()
