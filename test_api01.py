import requests, os #라이브러리 / 파일

def fn_grade(grade):
    value = ''
    if(grade == '1'):
        value = '좋음'
    elif (grade == '2'):
        value = '보통'
    elif (grade == '3'):
        value = '나쁨'
    elif (grade == '4'):
        value = '매우나쁨'
    return value

# r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/5/16')
# rjson = r.json()
#
# citys = rjson["RealtimeCityAir"]["row"]
#
# for city in citys:
#     gu_name = city["MSRSTE_NM"]
#     gu_mise = city["IDEX_MVL"]
#     print(gu_name, gu_mise)

print(os.path.isfile("html_test.html"))

file = open('html_test.html','w',encoding='euc-kr')

# file.write("<html><head><title>테스트 타이틀</title></head><body>테스트 입니다. </body></html>")
# file.close()

url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'
params = {  'serviceKey' : '3X5CZiq86N+q3mEysZhYXnfsVZnmeQbJgtkkKxbdGCU+S2W1v/1vbuKGp+4jh2DHHfFptFASJjvlHNSmwixk7g=='   #일반 인증키 : []Encoding / [v]Decoding
          , 'returnType' : 'json'   #xml, json
          , 'numOfRows' : '200'
          , 'pageNo' : '1'
          , 'sidoName' : '경기'   #서울, 경기, 충청, 등...
          , 'ver' : '1.0' }

response = requests.get(url, params=params)
#print(response.content)
#response.json()['response']['body']['items'][0].get('stationName')
items = response.json()['response']['body']['items']
sBody = ''
index = 0
for item in items:
    dataTime = item["dataTime"]
    stationName = item["stationName"]
    pm10Value = item["pm10Value"]
    pm10Grade = item["pm10Grade"]
    pm25Value = item["pm25Value"]
    pm25Grade = item["pm25Grade"]
    o3Value = item["o3Value"]
    o3Grade = item["o3Grade"]
    index = index + 1
    #print(dataTime, stationName, pm10Value, pm25Value)
    #if(stationName == '안양8동' or stationName == '고잔동'):
    #sBody += str(index) + ' / ' + dataTime + ' / ' + stationName + ' / ' + o3Grade + ' / ' + pm10Grade + ' / ' + pm25Grade + '<br>'
    sBody +="       <tr bgcolor = '' align ='center' style='font-size:17; font-family:consolas'>"
    sBody +="           <td align = 'center' width = '5%'>"+str(index)+"</td>"
    sBody +="           <td width = '25%'>"+dataTime+"</td>"
    sBody +="           <td width = '20%'>"+stationName+"</td>"
    sBody +="           <td width = '15%'>"+o3Value+"["+fn_grade(o3Grade)+"]</td>"
    sBody +="           <td width = '15%'>"+pm10Value+"["+fn_grade(pm10Grade)+"]</td>"
    sBody +="           <td width = '15%'>"+pm25Value+"["+fn_grade(pm25Grade)+"]</td>"
    sBody +="       </tr>"


#sBody = '123'
file.write(
"<html>"
"   <head>"
"       <title>경기도 미세먼지 농도</title>"
"   </head>"
"   <body>"
"   <table border='1' bordercolor='skybule' width ='1000' height='50' align = 'center'>"
"       <th colspan='6' style='font-size:30; font-family:Arial'>경기도 미세먼지 농도</th>"
"       <tr bgcolor = '' align ='center' style='font-size:20; font-family:consolas'>"
"           <td align = 'center'>No.</td>"
"           <td>Data Time</td>"
"           <td>지역</td>"
"           <td>오존</td>"
"           <td>미세먼지</td>"
"           <td>초미세먼지</td>"
"       </tr>"
+sBody+
"   </table>"

"   </body>"
"</html>")

file.close()