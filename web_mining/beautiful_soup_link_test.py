import urllib2
from bs4 import BeautifulSoup

def getAllLinks(url):
    response = urllib2.urlopen(url)
    content = response.read()
    soup = BeautifulSoup(content) #, "html5lib")
    return soup.find_all("a")

links1 = getAllLinks('http://www.stanford.edu')
links2 = getAllLinks('http://med.stanford.edu/')

print len(links1)
print len(links2)
