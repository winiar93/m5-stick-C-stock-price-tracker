import wifiCfg
from m5stack import *
from m5ui import *
from uiflow import *
import urequests as requests
from time import sleep
import network, machine
setScreenColor(0x111111)

#wifiCfg.autoConnect()
wifiCfg.doConnect('@@@', '@@@')


def gold_price_api():
    gold_price_api = "https://api.thingspeak.com/apps/thinghttp/send_request?api_key=AT8VTTC4BMVYUWRT"
    response = requests.get(gold_price_api).text
    gold_data = response.split(" ")[0]
    label0 = M5TextBox(127, 67, "Gold", lcd.FONT_DejaVu40, 0xffd11a, rotate=90)
    label1 = M5TextBox(75, 35, gold_data, lcd.FONT_DejaVu40, 0xFFFFFF, rotate=90)
    label2 = M5TextBox(25, 75, "usd/oz", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=90)


def btc_price_api():
    btc_price = "https://api.thingspeak.com/apps/thinghttp/send_request?api_key=QH0XOAJSY3ZN8KP7"
    response = requests.get(btc_price).text
    btc_price = response.replace("USD", "")
    label0 = M5TextBox(127, 60, "BitCoin", lcd.FONT_DejaVu40, 0xffd11a, rotate=90)
    label1 = M5TextBox(75, 5, btc_price, lcd.FONT_DejaVu40, 0xFFFFFF, rotate=90)
    label2 = M5TextBox(25, 85, "usd", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=90)


while True:
    gold_price_api()
    time.sleep(30)
    setScreenColor(0x111111)
    btc_price_api()
    time.sleep(30)
    setScreenColor(0x111111)