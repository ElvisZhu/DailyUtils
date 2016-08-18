#!python
import json
from urllib import request
from bs4 import BeautifulSoup

def getdata():
	header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36'}
	l_url = request.Request('http://www.ishadowsocks.com/',headers=header)
	soup = BeautifulSoup(request.urlopen(l_url).read(), "html.parser")
	free_section = soup.find("section",attrs={"id":"free"})
	free_div = free_section.findAll("div",attrs={"class":"col-lg-4 text-center"})
# 	{
# "server" : "US3.SSSERVER.PW",
# "server_port" : 8989,
# "password" : "29722133",
# "method" : "aes-256-cfb",
# "remarks" : "c"}
	configs = ["server","server_port","password","method","remarks"]
	s=[]
	for fdiv in free_div:
		h4s = [ x.getText().split(":")[-1] for x in fdiv.findAll('h4')]
		d = h4s[0:4]
		d.append(d[0].split(".")[0])
		s.append({x:y for (x,y) in zip(configs,d)})
	return s
#	return [free_div[0].findAll('h4')[2].getText()[-8:],free_div[1].findAll('h4')[2].getText()[-8:],free_div[2].findAll('h4')[2].getText()[-8:]]

def main():
	file = 'gui-config.json'
	fp = open(file, 'r')
	dict = json.loads(fp.read())
	fp.close()
	dict["configs"]=getdata()
	s = json.dumps(dict)
	fp = open(file, 'w')
	fp.write(s)
	fp.close()

if __name__ == '__main__':
	main()
