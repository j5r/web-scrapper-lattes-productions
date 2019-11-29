# Web-scrapper-lattes-productions
This is an web scrapper for getting data about one's productions in Lattes CV implemented in Python3.
To get Python3, download it from [here](https://www.python.org). For Linux users, you may install it 
by the terminal with 

 - sudo apt-get install python3.*

in which * can be 6, 7 or 8. I recommend use 7.

For installing all requirements, you may try one of these:

 - <p style="color:blue">pip3 install -r requirements.txt</p>
(generally on platforms that have both Python2 and Python3) or
 - <p style="color:blue">pip install -r requirements.txt</p>
(when you have just the Python3 version)

LINUX: If you do not have the PIP Package Manager installed on linux, try this before the previous step:
<ul><li><p style="color:blue">sudo apt-get install python3-pip</p></li></ul>

<p style="color:red">If you can not install all requirements with the commands above, try install them manually
by typing
<ul> <li style="color:#a33">
pip(3) install selenium bs4 openpyxl
</li></ul>
</p>



# ChromeDriver
You must to have the ChromeDriver in your machine. You can get it [Here](https://chromedriver.chromium.org/downloads).
It do not need to be installed, just downloaded. You will need to use the path where the ChromeDriver is in the code.
More specifically, the "chrome_drive_url" parameter in the "main.py" file need to take that path.

 - Remark: You must to download a version compatible with your GoogleChrome browser version. To see your browser's 
version, look for "About Google Chrome (pt-br: Sobre o Google Chrome)" in the menu, as illustrated below.

![Versão do Google Chrome](https://www.howtogeek.com/wp-content/uploads/2017/03/fixed-settings.png)

