from bs4 import BeautifulSoup
import requests
re=requests.get('https://news.ycombinator.com/news')
soup=BeautifulSoup(re.text,'html.parser')
links=soup.select('.titleline')
votes=soup.select('.score')

for i , j in enumerate(votes):
    if  int(j.text.replace(' points','')) >100:
        print(links[i].text,j.text.replace(' points',''))
    else:
        break