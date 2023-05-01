from bs4 import BeautifulSoup
import requests
import re
import random
import pandas as pd

#url = 'https://www.apkmirror.com/'
user_agents_list = [
    'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
]

new_url = 'https://www.apkmirror.com/apk/chess-com/chess-play-learn/chess-play-learn-4-5-16-googleplay-release/'


req = requests.get(new_url, headers={'User-Agent': random.choice(user_agents_list)})


soup = BeautifulSoup(req.text, 'lxml')
soup

result = soup.find_all('h5',class_='appRowTitle')

result = soup.find('div',string='All Releases ')
releases = result.parent

    
versions = soup.find_all(class_='infoSlide t-height')
versions


all_versions = []


for v in versions:
    v = v.find_all('p')[0].text
    pattern = r':(.+)-'
    match = re.search(pattern, v)
    if match:
        v = match.group(1)
       
    
    all_versions.append(v)
    
    

table = pd.DataFrame({'Version': all_versions})

table.to_csv('D:\Studies\Web scraping\MirrorAPK/table.csv')
