# Web-scrapper-lattes-productions
This is an web scrapper for getting data about one's productions in Lattes CV implemented in Python3.

For installing all requirements, you may try one of these:

 - <p style="color:blue">pip3 install -r requirements.txt</p>
(generally on platforms that have both Python2 and Python3) or
 - <p style="color:blue">pip install -r requirements.txt</p>
(when you have just the Python3 version)

LINUX: If you do not have the PIP Package Manager installed on linux, try this before the previous step:
<p style="color:blue">sudo apt-get install python3-pip</p>










#Example of use
##lattes.py

<pre>
<code style="color:#289548">
junior = LattesBS(url="http://buscatextual.cnpq.br/buscatextual/visualizacv.do?id=K4440740Y4",
              cdriver="/home/junior/chromedriver")

junior.init() #this downloads the Lattes CV webpage, use it just once

soup = junior.get() # this is a BeautifulSoup object

</code>
</pre>









#Example of use
## xlsxmanager.py
. . . (in development)










