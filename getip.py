from urllib2 import urlopen
from bs4 import BeautifulSoup
import re
import random
import datetime

random.seed(datetime.datetime.now())
def getLinks(articlUrl):
	html=urlopen("http://en.wikipedia.org"+articlUrl)
	bsObj=BeautifulSoup(html)
	return bsObj.find("div")