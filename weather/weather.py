from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from MainWindow import Ui_MainWindow

from datetime import datetime
import json
import os
import requests
from urllib.parse import urlencode

OPENWEATHERMAP_API_KEY = os.environ.get('09d677368549b360d451b662922057a3')


def from_ts_to_time_of_day(ts):
    dt = datetime.fromtimestamp(ts)
    return dt.strftime("%I%p").lstrip("0")


class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(str)
    result = pyqtSignal(dict, dict)


class WeatherWorker(QRunnable):
    signals = WorkerSignals()
    is_interrupted = False

    def __init__(self, location):
        super(WeatherWorker, self).__init__()
        self.location = location

    @pyqtSlot()
    def run(self):
        try:
            params = dict(
                q=self.location,
                appid='09d677368549b360d451b662922057a3'
            )

            url = 'http://api.openweathermap.org/data/2.5/weather?%s&units=metric' % urlencode(params)
            r = requests.get(url)
            weather = json.loads(r.text)

            if weather['cod'] != 200:
                raise Exception(weather['message'])

            url = 'http://api.openweathermap.org/data/2.5/forecast?%s&units=metric' % urlencode(params)
            r = requests.get(url)
            forecast = json.loads(r.text)

            self.signals.result.emit(weather, forecast)

        except Exception as e:
            self.signals.error.emit(str(e))

        self.signals.finished.emit()


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.pushButton.pressed.connect(self.update_weather)

        self.threadpool = QThreadPool()

        self.show()

    def alert(self, message):
        alert = QMessageBox.warning(self, "Warning", message)

    def update_weather(self):
        worker = WeatherWorker(self.lineEdit.text())
        worker.signals.result.connect(self.weather_result)
        worker.signals.error.connect(self.alert)
        self.threadpool.start(worker)

    def weather_result(self, weather, forecasts):
        self.latitudeLabel.setText("%.2f ??" % weather['coord']['lat'])
        self.longitudeLabel.setText("%.2f ??" % weather['coord']['lon'])

        self.windLabel.setText("%.2f m/s" % weather['wind']['speed'])

        self.temperatureLabel.setText("%.1f ??C" % weather['main']['temp'])
        self.pressureLabel.setText("%d hPa" % weather['main']['pressure'])
        self.humidityLabel.setText("%d %%" % weather['main']['humidity'])

        self.sunriseLabel.setText(from_ts_to_time_of_day(weather['sys']['sunrise']))

        main_weather = ''
        main_kor = ['????????????', '?????????', '???', '???', '??????', '?????????', '??????', '??????', '???',
                    '??????', '????????????', '??????', '??????']

        if weather['weather'][0]['main'] == 'Thunderstorm':
            main_weather = main_kor[0]
        elif weather['weather'][0]['main'] == 'Drizzle':
            main_weather = main_kor[1]
        elif weather['weather'][0]['main'] == 'Rain':
            main_weather = main_kor[2]
        elif weather['weather'][0]['main'] == 'Snow':
            main_weather = main_kor[3]
        elif weather['weather'][0]['main'] == 'Mist' or weather['weather'][0]['main'] == 'Haze' or \
                weather['weather'][0]['main'] == 'Fog':
            main_weather = main_kor[4]
        elif weather['weather'][0]['main'] == 'Smoke':
            main_weather = main_kor[5]
        elif weather['weather'][0]['main'] == 'Dust':
            main_weather = main_kor[6]
        elif weather['weather'][0]['main'] == 'Sand':
            main_weather = main_kor[7]
        elif weather['weather'][0]['main'] == 'Ash':
            main_weather = main_kor[8]
        elif weather['weather'][0]['main'] == 'Squall':
            main_weather = main_kor[9]
        elif weather['weather'][0]['main'] == 'Tornado':
            main_weather = main_kor[10]
        elif weather['weather'][0]['main'] == 'Clear':
            main_weather = main_kor[11]
        elif weather['weather'][0]['main'] == 'Clouds':
            main_weather = main_kor[12]

        description_weather = ''
        description_kor = ['????????? ?????? ????????? ????????????', '?????? ????????? ????????????', '????????? ????????? ????????????',
                           '?????? ????????????', '????????????', '?????? ????????????', '???????????? ????????????', '?????? ???????????? ????????? ????????????',
                           '???????????? ????????? ????????????', '?????? ???????????? ????????? ????????????', '????????? ?????????', '?????????', '?????? ?????????',
                           '????????? ?????????', '?????????', '?????? ?????????', '???????????? ?????????', '?????? ???????????? ?????????', '?????????',
                           '????????? ???', '????????? ???', '?????? ???', '?????? ?????? ???', '????????? ???', '??????', '?????? ????????? ???', '????????? ???',
                           '?????? ????????? ???', '???????????? ????????? ???', '????????? ???', '?????? ???', '??????', '????????????', '????????? ????????????',
                           '????????? ?????? ???', '?????? ???', '????????? ????????? ???', '????????? ???', '??????', '??????', '??????', '??????',
                           '?????? ??????', '??????', '??????', '??????', '?????????', '??????', '????????????', '?????? ??? ??? ?????? ?????? ??????',
                           '????????? ????????? ??? ??????', '???????????? ????????? ??? ??????', '????????? ?????? ?????? ??????', '???????????? ????????? ?????? ??????',
                           '??????', '????????????', '??????', '??????', '????????????', '??????', '????????? ?????? ??????', '?????? ??????', '???????????? ??????',
                           '?????? ?????? ??????', '????????? ??????', '??? ??????', '????????? ????????? ??? ??????', '??????', '????????? ??????', '??????',
                           '?????? ??????']

        if weather['weather'][0]['description'] == 'thunderstorm with light rain':
            description_weather = description_kor[0]
        elif weather['weather'][0]['description'] == 'thunderstorm with rain':
            description_weather = description_kor[1]
        elif weather['weather'][0]['description'] == 'thunderstorm with heavy rain':
            description_weather = description_kor[2]
        elif weather['weather'][0]['description'] == 'light thunderstorm':
            description_weather = description_kor[3]
        elif weather['weather'][0]['description'] == 'thunderstorm':
            description_weather = description_kor[4]
        elif weather['weather'][0]['description'] == 'heavy thunderstorm':
            description_weather = description_kor[5]
        elif weather['weather'][0]['description'] == 'ragged thunderstorm':
            description_weather = description_kor[6]
        elif weather['weather'][0]['description'] == 'thunderstorm with light drizzle':
            description_weather = description_kor[7]
        elif weather['weather'][0]['description'] == 'thunderstorm with drizzle':
            description_weather = description_kor[8]
        elif weather['weather'][0]['description'] == 'thunderstorm with heavy drizzle':
            description_weather = description_kor[9]
        elif weather['weather'][0]['description'] == 'light intensity drizzle':
            description_weather = description_kor[10]
        elif weather['weather'][0]['description'] == 'drizzle':
            description_weather = description_kor[11]
        elif weather['weather'][0]['description'] == 'heavy intensity drizzle':
            description_weather = description_kor[12]
        elif weather['weather'][0]['description'] == 'light intensity drizzle rain':
            description_weather = description_kor[13]
        elif weather['weather'][0]['description'] == 'drizzle rain':
            description_weather = description_kor[14]
        elif weather['weather'][0]['description'] == 'heavy intensity drizzle rain':
            description_weather = description_kor[15]
        elif weather['weather'][0]['description'] == 'shower rain and drizzle':
            description_weather = description_kor[16]
        elif weather['weather'][0]['description'] == 'heavy shower rain and drizzle':
            description_weather = description_kor[17]
        elif weather['weather'][0]['description'] == 'shower drizzle':
            description_weather = description_kor[18]
        elif weather['weather'][0]['description'] == 'light rain':
            description_weather = description_kor[19]
        elif weather['weather'][0]['description'] == 'moderate rain':
            description_weather = description_kor[20]
        elif weather['weather'][0]['description'] == 'heavy intensity rain':
            description_weather = description_kor[21]
        elif weather['weather'][0]['description'] == 'very heavy rain':
            description_weather = description_kor[22]
        elif weather['weather'][0]['description'] == 'extreme rain':
            description_weather = description_kor[23]
        elif weather['weather'][0]['description'] == 'freezing rain':
            description_weather = description_kor[24]
        elif weather['weather'][0]['description'] == 'light intensity shower rain':
            description_weather = description_kor[25]
        elif weather['weather'][0]['description'] == 'shower rain':
            description_weather = description_kor[26]
        elif weather['weather'][0]['description'] == 'heavy intensity shower rain':
            description_weather = description_kor[27]
        elif weather['weather'][0]['description'] == 'ragged shower rain':
            description_weather = description_kor[28]
        elif weather['weather'][0]['description'] == 'light snow':
            description_weather = description_kor[29]
        elif weather['weather'][0]['description'] == 'snow':
            description_weather = description_kor[30]
        elif weather['weather'][0]['description'] == 'heavy snow':
            description_weather = description_kor[31]
        elif weather['weather'][0]['description'] == 'sleet':
            description_weather = description_kor[32]
        elif weather['weather'][0]['description'] == 'shower sleet':
            description_weather = description_kor[33]
        elif weather['weather'][0]['description'] == 'light rain and snow':
            description_weather = description_kor[34]
        elif weather['weather'][0]['description'] == 'rain and snow':
            description_weather = description_kor[35]
        elif weather['weather'][0]['description'] == 'light shower snow':
            description_weather = description_kor[36]
        elif weather['weather'][0]['description'] == 'shower snow':
            description_weather = description_kor[37]
        elif weather['weather'][0]['description'] == 'heavy shower snow':
            description_weather = description_kor[38]
        elif weather['weather'][0]['description'] == 'mist':
            description_weather = description_kor[39]
        elif weather['weather'][0]['description'] == 'smoke':
            description_weather = description_kor[40]
        elif weather['weather'][0]['description'] == 'haze':
            description_weather = description_kor[41]
        elif weather['weather'][0]['description'] == 'sand, dust whirls':
            description_weather = description_kor[42]
        elif weather['weather'][0]['description'] == 'fog':
            description_weather = description_kor[43]
        elif weather['weather'][0]['description'] == 'sand':
            description_weather = description_kor[44]
        elif weather['weather'][0]['description'] == 'dust':
            description_weather = description_kor[45]
        elif weather['weather'][0]['description'] == 'volcanic ash':
            description_weather = description_kor[46]
        elif weather['weather'][0]['description'] == 'squalls':
            description_weather = description_kor[47]
        elif weather['weather'][0]['description'] == 'tornado':
            description_weather = description_kor[48]
        elif weather['weather'][0]['description'] == 'clear sky':
            description_weather = description_kor[49]
        elif weather['weather'][0]['description'] == 'few clouds':
            description_weather = description_kor[50]
        elif weather['weather'][0]['description'] == 'scattered clouds':
            description_weather = description_kor[51]
        elif weather['weather'][0]['description'] == 'broken clouds':
            description_weather = description_kor[52]
        elif weather['weather'][0]['description'] == 'overcast clouds':
            description_weather = description_kor[53]
        elif weather['weather'][0]['description'] == 'tropical storm':
            description_weather = description_kor[54]
        elif weather['weather'][0]['description'] == 'hurricane':
            description_weather = description_kor[55]
        elif weather['weather'][0]['description'] == 'cold':
            description_weather = description_kor[56]
        elif weather['weather'][0]['description'] == 'hot':
            description_weather = description_kor[57]
        elif weather['weather'][0]['description'] == 'windy':
            description_weather = description_kor[58]
        elif weather['weather'][0]['description'] == 'hail':
            description_weather = description_kor[59]
        elif weather['weather'][0]['description'] == 'calm':
            description_weather = description_kor[60]
        elif weather['weather'][0]['description'] == 'light breeze':
            description_weather = description_kor[61]
        elif weather['weather'][0]['description'] == 'gentle breeze':
            description_weather = description_kor[62]
        elif weather['weather'][0]['description'] == 'moderate breeze':
            description_weather = description_kor[63]
        elif weather['weather'][0]['description'] == 'fresh breeze':
            description_weather = description_kor[64]
        elif weather['weather'][0]['description'] == 'strong breeze':
            description_weather = description_kor[65]
        elif weather['weather'][0]['description'] == 'high win':
            description_weather = description_kor[66]
        elif weather['weather'][0]['description'] == 'gale':
            description_weather = description_kor[67]
        elif weather['weather'][0]['description'] == 'severe gale':
            description_weather = description_kor[68]
        elif weather['weather'][0]['description'] == 'storm':
            description_weather = description_kor[69]
        elif weather['weather'][0]['description'] == 'violent storm':
            description_weather = description_kor[70]

        self.weatherLabel.setText("%s (%s)" % (
            main_weather,
            description_weather
        )
                                  )

        self.set_weather_icon(self.weatherIcon, weather['weather'])

        for n, forecast in enumerate(forecasts['list'][:5], 1):
            getattr(self, 'forecastTime%d' % n).setText(from_ts_to_time_of_day(forecast['dt']))
            self.set_weather_icon(getattr(self, 'forecastIcon%d' % n), forecast['weather'])
            getattr(self, 'forecastTemp%d' % n).setText("%.1f ??C" % forecast['main']['temp'])

    def set_weather_icon(self, label, weather):
        label.setPixmap(
            QPixmap(os.path.join('images', "%s.png" %
                                 weather[0]['icon']
                                 )
                    )

        )


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec_()
