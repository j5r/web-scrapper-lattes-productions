import urllib.request as request
from tkinter import Tk, Button, Label
import shelve
from bs4 import BeautifulSoup as BS
from time import sleep

murilo = "https://orcid.org/0000-0002-6398-8752"
eduardo = "https://orcid.org/0000-0002-9067-9234"
junior = "https://orcid.org/0000-0003-1443-2034"





class OrcidBS:
    def __init__(self,**kw):
        kw.setdefault("url",None)

        if kw["url"] is None:
            msg = "You must to give a lattes-page url with\n\t"
            msg += "OrcidBS(url=theUrl)"
            raise SyntaxError(msg)

        # 0: File Name for saving data
        kw.setdefault("filename",kw["url"].split(".org/")[1])
        if not kw["filename"].endswith(".shelve"):
            kw["filename"] += ".shelve"
        self.__file_name = kw["filename"]
        ####

        self.__kw = kw


    def init(self):
        """The initializer method. It saves the data into a shelve db."""
        # 3: Data
        self.__db = shelve.open(self.__file_name)
        self.__db["orcid"] = request.urlopen(self.__kw["url"]).read()
        self.__db["url"] = self.__kw["url"]
        self.__db.close()
        ####

    def get(self):
        """Returns a BeautifulSoup object."""
        self.__db = shelve.open(self.__file_name)
        ans = BS(self.__db["orcid"],"html.parser")
        self.__db.close()
        return ans

    def getUrl(self):
        """Return the main url."""
        self.__db = shelve.open(self.__file_name)
        ans = self.__db["url"]
        self.__db.close()
        return ans







murilo = OrcidBS(url=murilo)
eduardo = OrcidBS(url=eduardo)
