import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import requests
from bs4 import BeautifulSoup

source = requests.get('http://www.artistlab.co.kr/reserve/konkuk/a-hall/12-24-12-12/').text
soup = BeautifulSoup(source, "html.parser")

##hotKeys = soup.select("button.new-appt.button")
hotKeys = soup.select("span.timeslot-time")

index = 0
for key in hotKeys:
    index += 1
    print(str(index) + ", " + key.text)
    if index >= 20:
        break


req = requests.get('http://www.artistlab.co.kr/reserve/konkuk/a-hall/12-24-12-12/')
##print(req.text)
status = req.status_code ##제대로 됬으면 응답코드가 200
if status == 200:
    print('dfdf')
    html = req.text
    soup = BeautifulSoup(req.content, 'html.parser')
    print(soup.find("span").get_text())
##    print(soup.select(".span.button-text"))
    ##print(html)
    title1 = soup.select_one('body > div.wrapper > div.wrapper_inner > div > div > div > div > div:nth-child(3) > div > div.web-reservation-calendar-sub-row.wpb_column.vc_column_container.vc_col-sm-8 > div > div > div:nth-child(3) > div > div > div.booked-calendar-wrap.large > table > tbody > tr.entryBlock > td > div > div:nth-child(5) > span.timeslot-people > button > span.button-text')
    ##print (title.get_text())
    title2 = soup.select_one('body > div.wrapper > div.wrapper_inner > div > div > div > div > div:nth-child(3) > div > div.web-reservation-calendar-sub-row.wpb_column.vc_column_container.vc_col-sm-8 > div > div > div:nth-child(3) > div > div > div.booked-calendar-wrap.large > table > tbody > tr.entryBlock > td > div > div:nth-child(6) > span.timeslot-people > button > span.button-text')
    print (title2)
else:
    print('no!!')
