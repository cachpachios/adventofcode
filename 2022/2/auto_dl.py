from datetime import datetime
import time

from utils import download_input

RELEASE_TIME = 6*60*60 + 2 # 6:00:02

while True:
    now = datetime.now()
    second_of_day = now.hour * 3600 + now.minute * 60 + now.second + now.microsecond / 1000000
    if second_of_day > RELEASE_TIME:
        break
    else:
        print(now.strftime("%H:%M:%S"), second_of_day)
        time.sleep(1)
        
YEAR = "2022"
DAY = 2

download_input(DAY, year=YEAR)