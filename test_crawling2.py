import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

#res = requests.get('https://blog.naver.com/suinn0904/222766165124')
#res = requests.get('https://naver.com')
#soup = BeautifulSoup(res.content, 'html.parser')

#title = soup.find('div')

#print(title.get_text())

# a = urlopen('https://naver.com')
# soup = BeautifulSoup(a.read(), 'html.parser')
# c = soup.find('div', {'id': 'account'})
# print(c.text)


url = urlopen("https://music.bugs.co.kr/chart?wl_ref=M_left_02_01")
soup = BeautifulSoup(url.read(), 'html.parser')
# td 태그에 check라는 class가 있는 td 태그를 모두 가져온다.

# musics = soup.find_all('td', "check")
# # musics의 각 태그들에 대해서
# for i, music in enumerate(musics):
#     # input 태그안에 title 속성값을 parsing한다.
#     print("{}위: {}".format(i+1, music.input['title']))

#musics = soup.find_all('td', 'check')
#musics2 = soup.find_all('td', 'left')
musics3 = soup.find_all(attrs={'class':'artist','adult_yn':'N'})
print(musics3)
# musics의 각 태그들에 대해서
#for i, music in enumerate(musics):
    # input 태그안에 title 속성값을 parsing한다.
    #print("{}위: {}".format(i+1, music.input['title']))
    # print("{}위: {}".format(i + 1, music.find('input')['title']))