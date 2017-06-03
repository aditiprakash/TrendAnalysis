import urllib.request 
from bs4 import BeautifulSoup

address = 'http://celebscinema.com/india/rajinikanth-next-president-india/5982/'
soup = BeautifulSoup(urllib.request.urlopen(address).read(), "html.parser")
span = soup.find("p", {"style":"text-align: justify;"})  
paras = [x for x in span.findAllNext("p")]

start = span.string
middle = "\n\n".join(["".join(x.findAll(text=True)) for x in paras[:-1]])
last = paras[-1].contents[0]
final = "%s\n\n%s\n\n%s" % (start, middle, last)
print(final)
#print("%s\n\n" % (start))
