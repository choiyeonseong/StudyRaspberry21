import folium
from folium.plugins import HeatMap
import json
# 웹브라우저에서 실행하기 위해
import webbrowser   
import os

# 특정 지역 포인트 지정
point_data = json.loads(open('./data/point.json', mode='r', encoding='utf-8').read())
# 지도 표시
m2 = folium.Map(location=[36.505354,127.704334], zoom_start=7, tiles='Cartodb Positron')  
# 온도 표시
HeatMap(point_data).add_to(m2)
# html파일 저장
m2.save('./data/heatmap.html')
# 크롬에서 실행
chorme_path='C:/Program Files/Google/Chrome/Application/chrome.exe %s'
print(os.getcwd())
webbrowser.open(os.getcwd() + '/data/heatmap.html')