#라이브러리 가져오기
from tkinter import *
import requests
import json
import datetime
from PIL import ImageTk, Image

root = Tk()
root.title("날씨알리미 프로그램")
root.geometry("450x600")
root['background'] = "white"

# 날짜 생성
dt = datetime.datetime.now()
date = Label(root, text=dt.strftime('%a %d'), bg='white', font=("bold", 15))
date.place(x=5, y=130)
month = Label(root, text=dt.strftime('%b'), bg='white', font=("bold", 15))
month.place(x=100, y=130)

# 시간 생성
hour = Label(root, text=dt.strftime('%I:%M:%p'), bg='white', font=("bold", 15))
hour.place(x=10, y=160)

# 17~8시 사이에는 밤(이미지: 달) 출력, 아니면 낮(이미지: 해) 출력
if int((dt.strftime('%I'))) >= 8 or int((dt.strftime('%I'))) <= 5:
    img = ImageTk.PhotoImage(Image.open('moon.png'))
    panel = Label(root, image=img)
    panel.place(x=150, y=150)
else:
    img = ImageTk.PhotoImage(Image.open('sun.png'))
    panel = Label(root, image=img)
    panel.place(x=150, y=150)

# 도시 검색 (그리드 이용한 위치 배치)
city_name = StringVar()
city_entry = Entry(root, textvariable=city_name, width=45)
city_entry.grid(row=1, column=0, ipady=10, stick=W + E + N + S)

def city_name(api_key=None):
    # API 호출
    api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}")
    api = json.loads(api_request.content)

    # 기온 정보
    y = api['main']
    current_temprature = y['temp']
    humidity = y['humidity']
    tempmin = y['temp_min']
    tempmax = y['temp_max']

    # Coordinates
    x = api['coord']
    longtitude = x['lon']
    latitude = x['lat']

    # 국가정보 끌고 오기
    z = api['sys']
    country = z['country']
    city = api['name']

    lable_temp.configure(text=current_temprature)
    lable_humidity.configure(text=humidity)
    max_temp.configure(text=tempmax)
    min_temp.configure(text=tempmin)
    lable_lon.configure(text=longtitude)
    lable_lat.configure(text=latitude)
    lable_country.configure(text=country)
    lable_city.configure(text=city)

# 검색 버튼 설정
city_nameButton = Button(root, text="Search", command=city_name)
city_nameButton.grid(row=1, column=1, padx=5, stick=W + E + N + S)

lable_city = Label(root, text="...", width=0, bg='white', font=("bold", 15))
lable_city.place(x=10, y=63)

lable_country = Label(root, text="...", width=0, bg='white', font=("bold", 15))
lable_country.place(x=135, y=63)

lable_lon = Label(root, text="...", width=0, bg='white', font=("bold", 15))
lable_lon.place(x=25, y=95)

lable_lat = Label(root, text="...", width=0, bg='white', font=("bold", 15))
lable_lat.place(x=95, y=95)

# 현재 온도
lable_temp = Label(root, text="...", width=0, bg='white', font=("bold", 110), fg='black')
lable_temp.place(x=18, y=220)

# 기타 기상정보
humi = Label(root, text="Humidity: ", width=0, bg='white', font=("bold", 15))
humi.place(x=3, y=400)

lable_humidity = Label(root, text="...", width=0, bg='white', font=("bold", 15))
lable_humidity.place(x=107, y=400)

maxi = Label(root, text="Max. Temp.: ", width=0, bg='white', font=("bold", 15))
maxi.place(x=3, y=430)

max_temp = Label(root, text="...", width=0, bg='white', font=("bold", 15))
max_temp.place(x=128, y=430)

mini = Label(root, text="Min. Temp.: ", width=0, bg='white', font=("bold", 15))
mini.place(x=3, y=460)

min_temp = Label(root, text="...", width=0, bg='white', font=("bold", 15))
min_temp.place(x=128, y=460)

root.mainloop()