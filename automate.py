from bs4 import BeautifulSoup
import urllib.request as u
import lxml,pickle

#TOI
linkTOI='http://timesofindia.indiatimes.com/'
toi = u.urlopen(linkTOI).read()
Toisoup = BeautifulSoup(toi)
Toisoup.prettify()
x=Toisoup.select('.list8 > li > a')
xl=[]
for i  in range(len(x)):
	xl.append(x[i].text)




# open the file for writing
fileObject = open('toi','wb') 

# this writes the object a to the
# file named 'testfile'
pickle.dump(xl,fileObject)  
fileObject.close()


#TheHindu
linkTH='http://www.thehindu.com/'
th=u.urlopen(linkTH).read()
thSoup=BeautifulSoup(th)
thSoup.prettify()
x=thSoup.select('.story-card-news > h3 > a')
for i in range(len(x)):
	print(x[i].text)
xl=[]
for i  in range(len(x)):
	xl.append(x[i].text)




# open the file for writing
fileObject = open('thehindu','wb') 

# this writes the object a to the
# file named 'testfile'
pickle.dump(xl,fileObject)  
fileObject.close()





#NDTV
linkNDTV='http://www.ndtv.com/'
ndtv=u.urlopen(linkNDTV).read()
ndtvSoup=BeautifulSoup(ndtv)
ndtvSoup.prettify()
x=ndtvSoup.select('.lead_stories_opt > ul > li')
xl=[]
for i  in range(len(x)):
	xl.append(x[i].text)
# open the file for writing
fileObject = open('ndtv','wb') 

# this writes the object a to the
# file named 'testfile'
pickle.dump(xl,fileObject)  
fileObject.close()



#Pickle Loading
fileObject = open('ndtv','rb')  
# load the object from the file into var b
ndtv = pickle.load(fileObject)
fileObject.close()
#toi
fileObject = open('toi','rb')
toi = pickle.load(fileObject)
fileObject.close()

