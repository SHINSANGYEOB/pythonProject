from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chromedriver = 'C:\\Users\\신상엽\\Desktop\\git workspace\\chormeDriver\\chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
driver.get('https://www.naver.com/')
driver.maximize_window()

print("driver.title :: " + driver.title)   # 크롤링한 페이지의 title 정보

'''
spanList = driver.find_elements(By.TAG_NAME, value="a")
spanList[0].get_attribute('href')
'''
driver.implicitly_wait(1)
search = driver.find_element(By.ID, value="query").send_keys("교촌치킨 안양 1호점", Keys.ENTER)

#driver.find_element(By.ID, value="search_btn").send_keys("교촌치킨 안양 1호점", Keys.ENTER);



while(True):
    pass

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