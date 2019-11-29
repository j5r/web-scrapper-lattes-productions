# Web-scrapper-lattes-productions
You can keep up with this help in this [video(pt-br)](https://youtu.be/HE90vC02sMQ).
## Step 0: installations - Python3, (pip), Selenium, BS4, OpenPyXL
This is an web scrapper for getting data about one's productions in Lattes CV implemented in Python3.
To get Python3, download it from [here](https://www.python.org). 

For LINUX users, you may install it 
by the terminal with 

 - sudo apt-get install python3.*

in which * may be 6, 7 or 8. I recommend use 7.

For installing all requirements, you may try one of these:

 - <p style="color:blue">pip3 install -r requirements.txt</p>
(generally on platforms that have both Python2 and Python3) or
 - <p style="color:blue">pip install -r requirements.txt</p>
(when you have just the Python3 version)

LINUX: If you do not have the PIP Package Manager installed on linux, try this before the previous step:
<ul><li><p style="color:blue">sudo apt-get install python3-pip</p></li></ul>

<p style="color:red">If you can not install all requirements with the commands above, try install them manually
by typing (depending on your pip version, type pip or pip3)
<ul> <li style="color:#a33">
pip(3) install selenium bs4 openpyxl
</li></ul>
</p>



# ChromeDriver
## Step 1: getting the Chrome Driver (chrome_drive_url)
You must to have the ChromeDriver in your machine. You can get it [Here](https://chromedriver.chromium.org/downloads).
It do not need to be installed, just downloaded. You will need to use the path where the ChromeDriver is in the code.
More specifically, the "chrome_drive_url" parameter in the "main.py" file need to take that path.

 - Remark: You must to download a version compatible with your GoogleChrome browser version. To see your browser's 
version, look for "About Google Chrome (pt-br: Sobre o Google Chrome)" in the menu, as illustrated below.

![Versão do Google Chrome](https://www.howtogeek.com/wp-content/uploads/2017/03/fixed-settings.png)






# Use
## Step 2: setting the other parameters:
You need to pass an url in the "main.py" file. More specifically, the "my_lattes_url" must to take an url like this one

 - http://buscatextual.cnpq.br/buscatextual/visualizacv.do?metodo=apresentar&id=K4440740Y4 or this one
 - http://buscatextual.cnpq.br/buscatextual/visualizacv.do?id=K4440740Y4

because I need to use the id=K4440740Y4 for a file name.
In order to get this url, follow the link just below your name, where it is writted something like

 - "Endereço para acessar este CV: http://lattes.cnpq.br/3866983332299702"


You can also set a name for your excel file. To do this, simply set the "excel_file_name" in "main.py" the way you want.

# Remark: What data I will get?
The current version just take the data in the 

 - "Produções: Artigos completos publicados em periódicos"

section of your Lattes CV.

They will be: 

 - Year
 - DOI
 - Article
 - JCR

The Excel file will have 3 sheets: "dados", "lattes" and "orcid".
The first two are important, because the third one is not implemented.

