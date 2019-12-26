import os, json, io
import MealInfo, ClassInfo, EventInfo, Weather
import datetime, time, os, time, sys, traceback

data = io.open('config.json', mode='r', encoding='utf-8').read()
conf = json.loads(data)

mod_mealinfo = MealInfo.MealInfo(
    conf['Open-NEIS-API']['KEY'],
    conf['Open-NEIS-API']['SD_SCHUL_CODE'],
    conf['Open-NEIS-API']['ATPT_OFCDC_SC_CODE']
)
mod_classinfo = ClassInfo.ClassInfo(
    conf['Open-NEIS-API']['KEY'],
    conf['Open-NEIS-API']['SD_SCHUL_CODE'],
    conf['Open-NEIS-API']['ATPT_OFCDC_SC_CODE']
)
mod_eventinfo = EventInfo.EventInfo(
    conf['Open-NEIS-API']['KEY'],
    conf['Open-NEIS-API']['SD_SCHUL_CODE'],
    conf['Open-NEIS-API']['ATPT_OFCDC_SC_CODE']
)
mod_weather = Weather.Weather(
    conf['KMA-Weather-Api']['ZoneID']
)
while True:
    print('1. get EventInfo')
    print('2. get ClassInfo')
    print('3. get WeatherInfo')
    print('4. get MealInfo')
    comm = input('')
    if comm == '1':
        #Event Info
        print('=========EventInfo========')
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
    elif comm == '2':
        #Class Info
        print('=========ClassInfo========')
        try:
            mod_classinfo.set_date(2019, 12, 10)# 2019년 12월 10일의 시간표를 불러옴
            class_list = mod_classinfo.get(2, 3)# 그 중 2학년 3반의 시간표를 불러옴
            for cls in class_list:
                print('교시: ',cls['PERIO'])
                print('이름: ',cls['ITRT_CNTNT'])
                print('---------------------------------')
                
        except Exception as e:
            print('Faield to load ClassInfo %s' % str(e))
    elif comm == '3':
        #Weather Info
        print('=========WeatherInfo========')
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
    elif comm == '4':        
        #Meal Info
        print('=========MealInfo========')
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
            
