import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
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


#url = urlopen("https://music.bugs.co.kr/chart?wl_ref=M_left_02_01")
#soup = BeautifulSoup(url.read(), 'html.parser')
# td 태그에 check라는 class가 있는 td 태그를 모두 가져온다.

# musics = soup.find_all('td', "check")
# # musics의 각 태그들에 대해서
# for i, music in enumerate(musics):
#     # input 태그안에 title 속성값을 parsing한다.
#     print("{}위: {}".format(i+1, music.input['title']))

#musics = soup.find_all('td', 'check')
#musics2 = soup.find_all('td', 'left')
#musics3 = soup.find_all(attrs={'class':'artist', 'adult_yn':'N'})
#url = urlopen("https://www.melon.com/chart/index.html")
chromedriver = 'C:\\Users\\신상엽\\Desktop\\git workspace\\chormeDriver\\chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
driver.get('https://www.melon.com/chart/index.htm')
driver.
print("+" * 100)
print("driver.title :: " + driver.title)   # 크롤링한 페이지의 title 정보

'''
spanList = driver.find_elements(By.TAG_NAME, value="a")
spanList[0].get_attribute('href')
'''

songInfoList = driver.find_elements(By.CLASS_NAME, value="lst50")

for i, songInfo in enumerate(songInfoList):
    #input 태그안에 title 속성값을 parsing한다.
    aInfo = songInfo.text.split("\n")
    if(len(aInfo) == 6):
        print(aInfo[0]+ " // " + aInfo[1]+ " // " +aInfo[2]+ " // " +aInfo[3]+ " // " +aInfo[4]+ " // " +aInfo[5])
    else:
        print(aInfo[0]+ " // " + aInfo[2]+ " // " +aInfo[3]+ " // " +aInfo[4]+ " // " +aInfo[5]+ " // " +aInfo[6])

'''
#html 읽어오기
1)
res = requests.get('https://naver.com')
soup = BeautifulSoup(res.content, 'html.parser')

2)
#url = urlopen("https://music.bugs.co.kr/chart?wl_ref=M_left_02_01")
soup = BeautifulSoup(url.read(), 'html.parser')

3)
with open("example.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
'''