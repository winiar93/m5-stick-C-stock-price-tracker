from m5stack import *
from m5ui import *
from uiflow import *
import urequests as requests


setScreenColor(0x111111)


gold_price_api = "https://api.thingspeak.com/apps/thinghttp/send_request?api_key=AT8VTTC4BMVYUWRT"

response = requests.get(gold_price_api).text
gold_data = response.split(" ")[0]
label0 = M5TextBox(127, 67, "Gold", lcd.FONT_DejaVu40, 0xffd11a, rotate=90)
label1 = M5TextBox(75, 35, gold_data, lcd.FONT_DejaVu40, 0xFFFFFF, rotate=90)
label2 = M5TextBox(25, 75, "usd/oz", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=90)