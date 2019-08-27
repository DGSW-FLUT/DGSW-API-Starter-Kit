import requests

class MonthFood:
    def __init__(self, yyyy, mm):
        yyyy_mm = '%d-%02d' % (yyyy, mm)
        link = 'http://www.dgsw.hs.kr/user/carte/calendarlist.do?searchStartDt=%s' % (yyyy_mm)
        content = requests.get(link).content.decode('utf8')
        sp, ep = content.find('<tbody>') + 7, content.find('</tbody>')
        out_mon = content[sp:ep].replace('\r', '').replace('\t', '').replace('<tr>', '')
        out_week = out_mon.split('</tr>')
        del out_week[-1]
        cal = {}
        for _ in out_week:
            _ = _.split("</td>")
            for __ in _:
                if __.find('</dt>') == -1:
                    continue
                day = __[:__.find('<div')]
                __ = __[__.find('<div'):]
                day = day[day.rfind('  ') + 2:]
                day = day[:day.find('\n')]
                cal[day] = {}
                ___ = __.split('<dt>')
                del ___[0]
                for ____ in ___:
                    if ____.find('alt="조식"') != - 1:
                        ____ = ____[____.find('<dd>') + 4:]
                        ____ = ____[:____.find('</dd>')].replace('\n', '').split('<br />')
                        cal[day]['B'] = ____
                    elif ____.find('alt="중식"') != - 1:
                        ____ = ____[____.find('<dd>') + 4:]
                        ____ = ____[:____.find('</dd>')].replace('\n', '').split('<br />')
                        cal[day]['L'] = ____
                    elif ____.find('alt="석식"') != - 1:
                        ____ = ____[____.find('<dd>') + 4:]
                        ____ = ____[:____.find('</dd>')].replace('\n', '').split('<br />')
                        cal[day]['D'] = ____
        self.data = cal
        print(cal)
        
#   *** Example *** 
#s = MonthFood(2019, 4)
