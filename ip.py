import requests
from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/wiki/Nineteen_Eighty-Four'
r = requests.get (url)
soup = BeautifulSoup (r.text ,'html.parser' )
link = soup('div' , {'id' : 'mw-content-text'})
for i in link:
    print (i.get_text())


