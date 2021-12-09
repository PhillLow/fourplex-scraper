from bs4 import BeautifulSoup
import requests

url = "https://xkcd.com/"
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
r = requests.get(url, headers=header).text

soup = BeautifulSoup(r, 'lxml')
soup.prettify()
soup = str(soup)

with open("webContents", 'w') as f:
    f.write(soup)
