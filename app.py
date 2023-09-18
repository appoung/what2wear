import requests
import json

city = "Anyang-si, KR"  # 도시
apiKey = "7b26c92417fd3678d52eac12dc870222"
lang = 'kr'  # 언어
units = 'metric'  # 화씨 온도를 섭씨 온도로 변경
api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang={lang}&units={units}"

result_get = requests.get(api)
result = result_get.json()
weather = result['weather'][0]['description']
temp = result['main']['temp']
temp_min = result['main']['temp_min']
temp_max = result['main']['temp_max']
feel_like = result['main']['feels_like']
print("날씨 : ", weather)
print("현재 온도 : ", temp)
if temp > 28:
    print("민소매,반팔,반바지")
elif temp > 23:
    print("반팔,얇은 셔츠,반바지")
elif temp > 20:
    print("얇은 가디건, 긴팔, 면바지")
elif temp > 17:
    print("얇은 니트, 맨투맨, 가디건, 청바지")
elif temp > 12:
    print("자켓, 가디건, 야상, 청바지")
elif temp > 10:
    print("트렌치코트, 야상, 점퍼, 청바지")
elif temp > 6:
    print("코트, 가죽자켓, 히트텍, 니트, 청바지")
elif temp > 4:
    print("코트, 가죽자켓, 히트텍, 니트, 청바지, 기모바지")
else:
    print("패딩, 두꺼운 코트, 목도리, 기모바지")
