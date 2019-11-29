"""
Link to obtain the ChromeDriver for GoogleChrome browser:
    https://chromedriver.chromium.org/downloads

Set the <chrome_drive_url> bottom with the location of the
chromedriver on your machine.
"""
from lattes import *
from soup_lattes import *
from xlsxmanager import *



chrome_drive_url = "/home/junior/chromedriver"
excel_file_name = "planilha"
my_lattes_url = "http://buscatextual.cnpq.br/buscatextual/visualizacv.do?id=K4775855H8"





my_lattes = LattesBS(url=my_lattes_url,cdriver=chrome_drive_url)
#my_lattes.download() # do this at least once
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


