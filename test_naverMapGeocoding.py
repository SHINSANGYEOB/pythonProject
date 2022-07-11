import json
import urllib
from urllib.request import Request, urlopen

location = '경기도 안양시 만안구 안양8동 461-1 삼아연립 B동 201호'

def get_location(location) :
    client_id = "hmil3ri1se"
    client_secret = "ykTPoNutAJZGeobtoRbfzNhqJDw3meJkOE8rzk4G"
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
        print(response_body)
        #if(response_body["meta"]["totalCount"] == 1) :
        if("addresses" in response_body) :
            x_space = response_body["addresses"][0]["x"]
            y_space = response_body["addresses"][0]["y"]
            return (x_space, y_space)
        else :
            print("totalCount == 0")
            x_space = None
            y_space = None
    else :
        print("ERROR")
        x_space = None
        y_space = None

location_space = get_location(location)
print(location_space)

option = ""

def get_optimal_route() :
