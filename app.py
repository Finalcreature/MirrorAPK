from bs4 import BeautifulSoup
import requests
import re
import random
import pandas as pd

user_input = input('please provide a url: ')



url = 'https://www.apkmirror.com'
user_agents_list = [
    'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
]

new_url = user_input  or 'https://www.apkmirror.com/uploads/?appcategory=eufy-security'



req = requests.get(new_url, headers={'User-Agent': random.choice(user_agents_list)})


soup = BeautifulSoup(req.text, 'lxml')


app_table = soup.find('div', class_='widget widget_appmanager_recentpostswidget')

app_rows = app_table.find_all('div', class_='appRow')


save_path = 'D:\Studies\Web scraping\MirrorAPK'


def createUrl(link):
    return url + link



for row in app_rows:
    title = row.find('h5', class_='appRowTitle').text.strip()
    if(title is not None):
        
        download_link = createUrl(row.find('a', class_='downloadLink').get('href')) 
        print(download_link)
        break
        req = requests.get(download_link, headers={'User-Agent': random.choice(user_agents_list)})
        soup = BeautifulSoup(req.text, 'lxml')
        download_button = soup.find('div', class_= 'table topmargin variants-table').find('a', 'accent_color').get('href')
        new_link =  url + download_button     
        req = requests.get(new_link, headers={'User-Agent': random.choice(user_agents_list)})
        soup = BeautifulSoup(req.text, 'lxml')
        final_button = url + soup.find('a', class_='downloadButton').get('href')
        req = requests.get(final_button,stream=True, headers={'User-Agent': random.choice(user_agents_list)})
        if req.status_code == 200:
            filename = save_path+'\\'+title+'.apk'
            with open(filename, 'wb') as f:
                for chunk in req.iter_content(chunk_size=1024):
                    f.write(chunk)
                    print('File downloaded successfully')
        else:
            print('Failed to download file')
  
        

    

# table = pd.DataFrame({'Version': all_versions})

# table.to_csv('D:\Studies\Web scraping\MirrorAPK/table.csv')
