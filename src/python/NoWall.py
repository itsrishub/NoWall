import requests
from bs4 import BeautifulSoup

link = str(input('Enter the link you want: '))

res = requests.get(f'http://webcache.googleusercontent.com/search?q=cache:{link}&strip=0&vwsrc=1')

soup = BeautifulSoup(res.content, "html.parser")
pre = soup.find('pre')

res = pre.text.replace('<script>window.main();</script>', '')

print(res)

with open('res.html', 'w') as f:
    f.write(str(res))
    f.close()
