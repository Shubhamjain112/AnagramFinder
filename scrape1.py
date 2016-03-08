from bs4 import BeautifulSoup
from urllib import urlopen

hello=raw_input("Enter any word : ")

BASE_URL = "http://wordsmith.org/anagram/anagram.cgi?anagram="+hello+"&language=english&t=1000&d=&include=&exclude=&n=&m=&source=adv&a=n&l=n&q=n&k=1"


html = urlopen(BASE_URL).read()
soup = BeautifulSoup(html, "lxml")
boccat = soup.find("div",attrs={'class': 'p402_premium'})
#print (boccat)
gh=boccat.findAll("p")
fj=(gh[1].find_all(text=True))
i=1
while i<len(fj):
	print fj[i]
	i=i+1

	


