"""
Link to obtain the ChromeDriver for GoogleChrome browser:
    https://chromedriver.chromium.org/downloads

Set the <chrome_drive_url> bottom with the location of the
chromedriver on your machine.
"""
from lattes import *
from soup_lattes import *
from xlsxmanager import *
from tkinter import Tk, filedialog



use_html_file = True

if use_html_file:
    root = Tk()
    html_filename =  filedialog.askopenfilename(initialdir = ".",title = "Escolha um arquivo html",filetypes = (("arquivos html","*.html"),("all files","*.*")))
    root.destroy()


chrome_drive_url = "/home/junior/chromedriver"
excel_file_name = "planilha"
my_lattes_url = "http://buscatextual.cnpq.br/buscatextual/visualizacv.do?metodo=apresentar&id=K4240480A3"



if not use_html_file:
    # Para abrir o navegador, use a sintaxe
    my_lattes = LattesBS(url=my_lattes_url,cdriver=chrome_drive_url)

else:
    # Para abrir um arquivo html, use a sintaxe, substituindo
    my_lattes = LattesBS(filename=html_filename,cdriver=chrome_drive_url)

my_productions = Producoes(my_lattes)





excel = Excel()
for itemLattes in my_productions.get():
    try:
        excel.lattes(**itemLattes)
        excel.dados(**itemLattes)
    except Exception as e:
        print(e)
excel.save(excel_file_name)

print(f"THE END!!! The file <<{excel_file_name}>> has been generated.")


