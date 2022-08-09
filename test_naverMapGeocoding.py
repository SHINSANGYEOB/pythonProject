import io
import json
import urllib
from urllib.request import Request, urlopen
import requests
from PIL import Image


location = '경기도 안양시 만안구 안양8동 461-1 삼아연립 B동 201호'
client_id = "hmil3ri1se"
client_secret = "ykTPoNutAJZGeobtoRbfzNhqJDw3meJkOE8rzk4G"

def get_location(location) :
    url = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query=" + urllib.parse.quote(location)

    request = urllib.request.Request(url)
    request.add_header("X-NCP-APIGW-API-KEY-ID", client_id)
    request.add_header("X-NCP-APIGW-API-KEY", client_secret)

    #여기서 키가 다르면 오류가 떨어지는데 try-catch를 어떻게 해야 하는지 확인 필요
    response = urlopen(request)
    resCode = response.getcode()

    if(resCode == 200) :
        response_body = response.read().decode('utf-8')
        response_body = json.loads(response_body)
        #print(response_body)
        #if(response_body["meta"]["totalCount"] == 1) :
        if("addresses" in response_body) :
            x_space = response_body["addresses"][0]["x"]
            y_space = response_body["addresses"][0]["y"]
            return x_space, y_space
        else :
            print("totalCount == 0")
            x_space = None
            y_space = None
    else :
        print("ERROR")
        x_space = None
        y_space = None

location_space = get_location(location)
#print(location_space)

endpoint = "https://naveropenapi.apigw.ntruss.com/map-static/v2/raster"
headers = {
    "X-NCP-APIGW-API-KEY-ID": client_id,
    "X-NCP-APIGW-API-KEY": client_secret,
}
lon, lat = location_space[0], location_space[1]
_center = f"{lon},{lat}"
# 줌 레벨 - 0 ~ 20
_level = 16
# 가로 세로 크기 (픽셀)
_w, _h = 500, 300
# 지도 유형 - basic, traffic, satellite, satellite_base, terrain
_maptype = "satellite"
# 반환 이미지 형식 - jpg, jpeg, png8, png
_format = "png"
# 고해상도 디스펠레이 지원을 위한 옵션 - 1, 2
_scale = 1
# 마커
_markers = f"""type:d|size:mid|pos:{lon} {lat}|color:red"""
# 라벨 언어 설정 - ko, en, ja, zh
_lang = "ko"
# 대중교통 정보 노출 - Boolean
_public_transit = True
# 서비스에서 사용할 데이터 버전 파라미터 전달 CDN 캐시 무효화
_dataversion = ""

# URL
url = f"{endpoint}?center={_center}&level={_level}&w={_w}&h={_h}&maptype={_maptype}&format={_format}&scale={_scale}&markers={_markers}&lang={_lang}&public_transit={_public_transit}&dataversion={_dataversion}"
res = requests.get(url, headers=headers)

image_data = io.BytesIO(res.content)
image = Image.open(image_data)
#print(image)
image.save('map-test.jpg')

option = ''
# option : 탐색옵션 [최대 3개, traoptimal(기본 옵션)
# / trafast, tracomfort, traavoidtoll, traavoidcaronly]

def get_optimal_route(start, goal, waypoints=['',''], option=option ) :
    client_id = '-- 발급받은 client id 입력 --'
    client_secret = '-- 발급받은 client secret 입력 --'
    # start=/goal=/(waypoint=)/(option=) 순으로 request parameter 지정
    url = f"https://naveropenapi.apigw.ntruss.com/map-direction-15/v1/driving? \
    start={start[0]},{start[1]}&goal={goal[0]},{goal[1]}\
    &waypoint={waypoint[0]},{waypoint[1]}&option={option}"
    request = urllib.request.Request(url)
    request.add_header('X-NCP-APIGW-API-KEY-ID', client_id)
    request.add_header('X-NCP-APIGW-API-KEY', client_secret)

    response = urllib.request.urlopen(request)
    res = response.getcode()

    if (res == 200) :
        response_body = response.read().decode('utf-8')
        return json.loads(response_body)

    else :
        print('ERROR')

#get_optimal_route(start, goal, option=option)