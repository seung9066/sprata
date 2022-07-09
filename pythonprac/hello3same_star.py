import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# 가져오기
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

# 솎아내기
soup = BeautifulSoup(data.text, 'html.parser')

# 코딩 시작

title1 = soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')
print(title1.text)
print(title1['href'])

trs = soup.select('#old_content > table > tbody > tr')
for tr in trs:
    a_tag = tr.select_one('td.title > div > a')
    if a_tag is not None:
        rank = tr.select_one('td:nth-child(1) > img')['alt']
        title = a_tag.text
        star = tr.select_one('td.point').text
        doc = {
            'rank':rank,
            'title':title,
            'star':star
        }
        db.movies.insert_one(doc)

movie = db.movies.find_one({'title':'매트릭스'})['star']
same_star = list(db.movies.find({'star':movie},{'_id':False}))
for target in same_star:
    print(target['title'])