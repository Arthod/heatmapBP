import schedule

import requests
import time
import os
from datetime import datetime

worlds = ["en153", "en154"]

def request_and_save_file(url, file_path):
    with open(file_path, "wb") as f:
        r = requests.get(url)
        f.write(r.content)

def snapshot():
    time_now_str = datetime.now().strftime("%Y_%d_%m-%H_%M_%S")
    print(f"Saved at {time_now_str}.")

    names = ["player_kills_att", "player_kills_def"]

    for world in worlds:
        for name in names:
            if (not os.path.exists(os.path.join("data", world, time_now_str))):
                os.mkdir(os.path.join("data", world, time_now_str))
            request_and_save_file(f"https://{world}.grepolis.com/data/{name}.txt.gz", os.path.join("data", world, time_now_str, f"{name}.txt.gz"))

if __name__ == "__main__":
    schedule.every(30).minutes.do(snapshot)

    while True:
        schedule.run_pending()
        time.sleep(1)