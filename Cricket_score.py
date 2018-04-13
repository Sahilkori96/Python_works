import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReqs


my_url="http://www.cricbuzz.com/"
Client=uReqs(my_url)

html_p=Client.read()
Client.close()

soup_page = soup(html_p,"html.parser")

score_box=soup_page.findAll("div",{"class":"cb-col cb-col-25 cb-mtch-blk"})
print(len(score_box))
for i in range(10):
	print(score_box[i].a["title"])
	print(score_box[i].a.text)
	print()
