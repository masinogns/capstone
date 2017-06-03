import time

from bs4 import BeautifulSoup
from pip._vendor import requests


class MenuAPI:
    url = "https://www.jejunu.ac.kr/camp/stud/foodmenu"
    list = []
    number = 100
    menuList = [[]]


    def getList(self, url):
        list = []

        # ssl issue가 발생한다
        html = requests.get(url, verify=False)
        bsObject = BeautifulSoup(html.content, 'html.parser', from_encoding='utf-8')

        nameList = bsObject.findAll("td", {"class": "border_right"})
        for name in nameList:
            name = name.get_text().replace(" ", "")
            list.append(name)

        return list
    # 출처 http://ourcstory.tistory.com/77

    def getDayInNumber(self, list):
        now = time.localtime()

        s = "%02d/%02d" % (now.tm_mon, now.tm_mday)
        # print(s)

        for i in range(0, 5):
            op = 0 + (13 * i)
            whether = list[op]
            result = whether[1:6]
            # print(result)
            if result == s:
                # print(i)
                break

        return i

    def getMenu(self, number, day):
        op = 0
        today = "today"
        tomorrow = "tomorrow"

        if number<5:
            if day == today:
                op = 13 * number
            elif day == tomorrow:
                if number!=4:
                    op = 13 * (number+1)
                    # print(number+1)
                else:
                    print("금요일 다음날은 없습니다")
                    exit()
        else:
            print("잘못된 접근입니다")
            exit()

        menuList = [
            [list[1 + op], list[2 + op], list[3 + op]],
            [list[4 + op], list[5 + op], list[6 + op]],
            [list[7 + op], list[8 + op], list[9 + op]],
            [list[10 + op], list[11 + op], list[12 + op]]
        ]

        return menuList
