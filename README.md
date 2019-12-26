# DGSW-API Starter Kit

대구소프트웨어 고등학교에서 앱 개발 입문자를 위한 API 모음 입니다.

다음 API가 포함되어 있습니다.
- 급식 API
- 시간표 API
- 학사일정 API
- 동네시간별예보 API

급식 받기
```python
try:
    mod_mealinfo.set_date(2019, 12)
    meal_list = mod_mealinfo.get(19)
    #print(meal_list.keys())

    if len(meal_list) > 0:
        print('........아침...........')
        
        for meal in meal_list[0]['DDISH_NM'].split('<br/>'):
            print(meal)
        if len(meal_list) > 1:
            print('........점심...........')
            for meal in meal_list[1]['DDISH_NM'].split('<br/>'):
                print(meal)
            if len(meal_list) > 2:
                print('........저녁...........')
                for meal in meal_list[2]['DDISH_NM'].split('<br/>'):
                    print(meal)
except Exception as e:
    print('Faield to load MealInfo %s' % str(e))
```

시간표 받기
```python
try:
    mod_classinfo.set_date(2019, 12, 10)# 2019년 12월 10일의 시간표를 불러옴
    class_list = mod_classinfo.get(2, 3)# 그 중 2학년 3반의 시간표를 불러옴
    for cls in class_list:
        print('교시: ',cls['PERIO'])
        print('이름: ',cls['ITRT_CNTNT'])
        print('---------------------------------')
        
except Exception as e:
    print('Faield to load ClassInfo %s' % str(e))
```
학사일정 받기
```python
try:
    mod_eventinfo.load()
    event_list = mod_eventinfo.get(2019, 12, 10, 3) # 2019년 12월 10일부터 최대 3개의 일정을 불러옴
    for event in event_list:
        print('일시: ',event['AA_YMD'])
        print('내용: ',event['EVENT_NM'])
        print('대상: ',event['TARGET'])
        print('휴일여부: ',event['SBTR_DD_SC_NM'])
        print('---------------------------------')
except Exception as e:
    print('Faield to load EventInfo %s' % str(e))
```
동네시간별예보 받기
```python
try:
    mod_weather.get()
    print(mod_weather.now)
    for weather in mod_weather.data:
        print('날짜:',weather['day'])#0:오늘 1:내일 2:모레
        print('시간:',weather['hour'])#시간(24)
        print('구름상태:',weather['sky'])#1:맑음 3:구름 많음 4: 흐림
        print('기후상태:',weather['pty'])#0:맑음 1:비구름 2:구름 3:눈구름 4:소나기
        print('강수확률:',weather['pop'])#강수확률
        print('풍속:',weather['ws'])#풍속
        print('---------------------------------')
        
except Exception as e:
    print('Faield to load WeatherInfo %s' % str(e))
```

## config.json

```json
{
  "Open-NEIS-API" : {
    "ATPT_OFCDC_SC_CODE" : "D10", //대구광역시 교육청
    "SD_SCHUL_CODE" : "7240393", //대구 소프트웨어 고둥학교
    "KEY" : "[Open Api Key]" //OpenApiKey
  },
  "KMA-Weather-Api" : {
    "ZoneID" : "2771038000" //대구광역시 달성군 구지면
  }
}
```

[OpenApiKey 발급 받기](https://open.neis.go.kr/portal/guide/actKeyPage.do)

[KMA-Weather-Api 지역번호 구하기](http://www.weather.go.kr/weather/lifenindustry/sevice_rss.jsp)