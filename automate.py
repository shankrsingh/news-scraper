from bs4 import BeautifulSoup
import urllib.request as u
import lxml,pickle
#Scraping function
def scrape_ret(link,desc):
	
	req=u.urlopen(link).read()
	reqSoup=BeautifulSoup(req,'lxml')
	reqSoup.prettify()
	x=reqSoup.select(desc)
	xl=[x[i].text for i in range(len(x))]
	return xl
#pickleDumping
def pickleDump(linklist,name):
	f = open(name,'wb')
	pickle.dump(linklist,f)
	f.close() 
#pickleOpening 
def pickleOpen(name):
	f = open(name,'rb')  
	name = pickle.load(f)
	return name

def main():
	links={'toi':['toi','http://timesofindia.indiatimes.com/','.list8 > li > a'],'theHindu':['th','http://www.thehindu.com/','.story-card-news > h3 > a'],
			'ndtv':['ndtv','http://www.ndtv.com/','.lead_stories_opt > ul > li']}
	
	for news_sites in links:
		l=scrape_ret(links[news_sites][1],links[news_sites][2])
		pickleDump(l,links[news_sites][0])


if __name__ == '__main__':
	main()
	name=pickleOpen('toi')
	print(name)



