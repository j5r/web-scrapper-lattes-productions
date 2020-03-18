from tkinter import *
from tkinter.filedialog import askopenfilename as Open #::>str
from tkinter.filedialog import asksaveasfile as Save #::>file
from tkinter.filedialog import askdirectory as Directory #::>str
from lattes.mglobal.configs import JSON as JSON_
import os
import time
from lattes.main.main import processar_arquivos_pastas_e_gerar_planilhas as MAIN




class Gui(Tk):

    JSON = JSON_

    def __init__(self):
        #b 0: inicializando classe e criando parâmetros
        Tk.__init__(self)
        self.option_add('*tearOff', FALSE) #tira ---- da barra de menu
        self.geometry(
                    Gui.JSON["self"]["geometry"]
                    )
        self.title("Lattes2Excel")
        self.fonte = ("Arial",14,)

        if os.sys.platform == "linux":
            #comando para executar um url no navegador: http://...
            self.__comando = "xdg-open "
            #linux
        else:
            self.__comando = "rundll32 url.dll,FileProtocolHandler "
            #windows
        #e 0: parâmetros inicializados

        #b 1: criando as variáveis internas da gui
        self.url_list = []
        self.url_list_erros = []
        self.nome_arquivo = Gui.JSON["self"]["unknown_file"]
        self.file_text = ""
        self.caminho = ""
        self.nome_pasta = Gui.JSON["self"]["folder_to_download"]
        self.cor_fundo = Gui.JSON["self"]["bg_for_the_end"]
        #e 1: as variáveis serão atualizadas para controle do programa

        #b 2: declarando contêineres
        self.fr1 = Frame(
                    self,
                    pady = 15,
                    )
        self.fr1.pack()

        self.fr2 = Frame(
                    self,
                    pady = 15,
                    )
        self.fr2.pack()

        self.fr3 = Frame(
                    self,
                    pady = 15,
                    )
        self.fr3.pack()
        #e 2: contêineres criados

        #b 3: criando widgets: sempre começam com a letra do seu tipo
        #b ..0: barra de menus
        self.m_barra_de_menus = Menu(self)
        self['menu'] = self.m_barra_de_menus


        self.m_menu_principal = Menu(self.m_barra_de_menus)
        self.m_barra_de_menus.add_cascade(
                    menu=self.m_menu_principal,
                    label=Gui.JSON["menu"]["main_menu"],
                    font = self.fonte,
                    )

        self.m_menu_ajuda = Menu(self.m_barra_de_menus)
        self.m_barra_de_menus.add_cascade(
                    menu=self.m_menu_ajuda,
                    label=Gui.JSON["menu"]["help_menu"],
                    font = self.fonte,
                    )
        #e ..0: barra de menus

        #b ..1: opções dos menus MENU e AJUDA
        self.m_menu_principal.add_command(
                    label= Gui.JSON["menu"]["main_menu_open"],
                    command=self.cll_abrir_arquivo,
                    font = self.fonte,
                    )
        self.m_menu_principal.add_command(
                    label= Gui.JSON["menu"]["main_menu_new"],
                    command=self.cll_novo_arquivo,
                    font = self.fonte,
                    )
        self.m_menu_principal.add_command(
                    label= Gui.JSON["menu"]["main_menu_run"],
                    command=self.cll_processar_html,
                    font = self.fonte,
                    )

        self.m_menu_ajuda.add_command(
                    label= Gui.JSON["menu"]["help_menu_how_to_use"],
                    command=self.cll_abrir_video_ajuda,
                    font = self.fonte,
                    )
        self.m_menu_ajuda.add_command(
                    label= Gui.JSON["menu"]["help_menu_about"],
                    command=None,
                    font = self.fonte,
                    )
        #e ..1: opções dos menus adicionadas

        #b ..2: widgets do frame 1
        self.l_arquivo = Label(
                    self.fr1,
                    text= Gui.JSON["label"]["file"],
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
        self.l_nome_arquivo["fg"] = Gui.JSON["label"]["file_fg"]
        self.l_nome_arquivo["bg"] = Gui.JSON["label"]["file_bg"]
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
                    text = Gui.JSON["button"]["save_and_next"],
                    fg = Gui.JSON["button"]["save_and_next_fg"],
                    font = self.fonte,
                    bg = Gui.JSON["button"]["save_and_next_bg"],
                    )

        #e ..4: botões no frame 3
        #e 3:


        #b 4: elementos a serem lançados por outras callbacks
        self.l_numero_links = Label(#label
                    self.fr2,
                    text = Gui.JSON["label"]["url_number"],
                    font = self.fonte,
                    )
        self.e_numero_links = Entry(
                    self.fr2,
                    font = self.fonte,
                    width = 10,
                    )
        self.b_abrir = Button(
                    self.fr3,
                    text = Gui.JSON["label"]["open_urls"],
                    command = self.cll_abrir_no_navegador,
                    fg = Gui.JSON["label"]["open_urls_fg"],
                    font = list(self.fonte) + ["bold"],
                    bg = Gui.JSON["label"]["open_urls_bg"],
                    )
        self.l_mensagem_final = Label(
                    self.fr1,
                    text = Gui.JSON["label"]["last_msg"],
                    font = ("Arial", 20, "bold"),
                    fg = Gui.JSON["label"]["last_msg_fg"],
                    bg = self.cor_fundo,
                    pady = 50
                    )
        #e 4: elementos foram criados

        #b 5: executando loop infinito
        self.mainloop()
        #e 5: loop infinito
    ####################################################################


    def cll_abrir_arquivo(self):
        #b 0: abrindo arquivo
        arquivos = [(
                    Gui.JSON["open_save_file"]["format_description"],
                    Gui.JSON["open_save_file"]["allowed_extension"],
                    )]
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
        arquivos = [(
                    Gui.JSON["open_save_file"]["format_description"],
                    Gui.JSON["open_save_file"]["allowed_extension"],
                    )]
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
        self.l_nome_arquivo["text"] = nome_arquivo
        arquivo.close()
        #e 2: o nome do arquivo e o seu caminho foram capturados
        #   : modifica label nome_do_arquivo


        #b 3: abrindo o arquivo com as eventuais modificações
        arquivo = open(caminho_arquivo+"/"+nome_arquivo,"r")
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
        self.cll_avancar()
        #e 5: preparando para a execução final

    def cll_avancar(self):
        #b 0: apagando o borão de avançar e desabilitando menus
        self.b_salvar_avancar.destroy()
        self.m_menu_principal.entryconfigure(0, state="disabled")
        self.m_menu_principal.entryconfigure(1, state="disabled")
        #e 0: menus foram desativados

        #b 1: adicionando botão: número de links e abrir links
        self.l_numero_links.pack(side=LEFT)


        self.e_numero_links.insert(0,"7")
        self.e_numero_links.pack()
        self.e_numero_links.focus()


        self.b_abrir.pack()
        #e 1: botões criados

    def cll_abrir_no_navegador(self):
        try:
            numero_de_links_para_abrir = int(self.e_numero_links.get())
        except Exception as e:
            print("Erro!", e)
            self.cll_abrir_mensagem_erro_Apenas_Numeros_Inteiros()
            return None

        for i in range(numero_de_links_para_abrir):
            try:
                url = self.url_list.pop()
                print(url)
                resultado = os.system(self.__comando + '"' + url + '"')
                if resultado:
                    print("Erro!!",url)
                    self.url_list_erros.append(url)


            except Exception as e:
                print(e)
                f = open(Gui.JSON["error"]["url_list_error"],"w")
                f.write("\n".join(self.url_list_erros))
                f.close()
                self.e_numero_links.destroy()
                self.b_abrir.destroy()
                self.l_numero_links["text"] = Gui.JSON["label"]["access_menu_process_html"]
                self.l_numero_links["font"] = self.fonte
                break






    def cll_abrir_mensagem_erro_Apenas_Numeros_Inteiros(self):
        pass


    def cll_abrir_video_ajuda(self):
        self.cll_abrir_link(Gui.JSON["menu"]["help_menu_about__url"])


    def cll_fim_do_programa(self):
        #b 0: apagando widgets
        self.l_arquivo.destroy()
        self.l_nome_arquivo.destroy()
        self.l_numero_links.destroy()
        self.e_numero_links.destroy()
        self.b_abrir.destroy()
        #e 0: agora vamos adicionar uma mensagem de adeus

        #b 1: lançando mensagem
        self.l_mensagem_final.pack()
        #e 1: mensagem lançada

        #b 2: pintando mensagem
        self.configure(bg = self.cor_fundo)
        self.fr1["bg"] = self.cor_fundo
        self.fr2["bg"] = self.cor_fundo
        self.fr3["bg"] = self.cor_fundo
        #e 2: janela foi colorida

        #b 3: executar o programa gerador de planilhas
        """EXECUTAR O PROGRAMA PRINCIPAL AQUI------------------------"""
        MAIN()
        #e 3: planilhas foram geradas

        #b 4: fechando o programa
        self.after(
                    int(Gui.JSON["self"]["milisseconds_before_close"]),
                    self.destroy
                    )
        #e 4: FIM DO PROGRAMA!

    def cll_processar_html(self):
        #entrar na pasta, chamar cll_fim_do_programa
        directory = Directory()
        if not directory:
            return None
        os.chdir(directory)
        self.cll_fim_do_programa()







