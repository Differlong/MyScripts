import os
import datetime
from PIL import ImageGrab
import time


default_root = "./file"

def save_grab():
    now = datetime.datetime.now()
    day = "%d_%d_%d/" % (now.year, now.month, now.day)
    cur_time = "%d_%d_%d" % (now.hour, now.minute, now.second)
    img_name = cur_time + ".jpg"
    file_path = os.path.join(default_root, day)
    if not os.path.isdir(file_path):
        os.makedirs(file_path)
    name = cur_time + ".jpg"
    img_path = os.path.join(file_path, img_name)
    img = ImageGrab.grab()
    img.save(img_path, "jpeg")
    print(img_name + " has been grabbed and saved.")


if __name__ == "__main__":
    while True:
        save_grab()
        time.sleep(30)
