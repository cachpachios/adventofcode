from datetime import datetime
import time

from utils import get_input, CURRENT_DAY, CURRENT_YEAR

print("Year:", CURRENT_YEAR, "Day:", CURRENT_DAY)

def get_day_seconds():
    now = datetime.now()
    return now.hour * 3600 + now.minute * 60 + now.second + now.microsecond / 1000000

BREAK_TIME = 6 * 3600 + 1

print(f"Downloading {CURRENT_YEAR}, Day: {CURRENT_DAY}")

while True:
    if get_day_seconds() > BREAK_TIME:
        with open("input.txt", "w") as f:
            f.write(get_input(CURRENT_YEAR, CURRENT_DAY))
        break
    else:
        print(datetime.now().strftime("%H:%M:%S"), end="\r")
        time.sleep(1)