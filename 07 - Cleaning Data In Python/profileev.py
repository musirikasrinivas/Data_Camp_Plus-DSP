# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 22:00:21 2019

@author: Lenovo
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup as soup



myurl = "http://www.profileevaluator.com/List-Of-Universities"
url_connection = urlopen(myurl)
page_html = url_connection.read()
page_soup = soup(page_html,"html.parser")
url_connection.close()


universities_names=page_soup.find("div", {"class": "content"})
