from m5stack import *
from m5ui import *
from uiflow import *

setScreenColor(0x111111)

setScreenColor(0x111111)

import urequests as requests
setScreenColor(0x111111)


gold_price_api = "https://api.thingspeak.com/apps/thinghttp/send_request?api_key=8MR8VNV0VF4EPKTM"

response =  requests.get(gold_price_api).text
gold_data_list = response.split(" ")




label0 = M5TextBox(111, 12, gold_data_list[0], lcd.FONT_DejaVu18, 0xFFFFFF, rotate=90)

