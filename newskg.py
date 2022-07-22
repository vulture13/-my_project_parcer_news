import json
import requests
from datetime import datetime

last_dt = datetime.now()
limit = 30


url = 'http://newsline.kg/getNews.php?limit={}&last_dt={}'.format(limit, last_dt)
response = requests.get(url)
news_download = json.loads(response.text)
news_list = news_download['data']


loading_dict_json = {}
number_key = 0
for news_dict in news_list:
    number_key += 1
    loading_dict_json[number_key] = news_dict 

with open('file_news.json', 'w') as file_write:
    json.dump(loading_dict_json, file_write, ensure_ascii=False, indent=6)

