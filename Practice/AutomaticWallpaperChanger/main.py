import ctypes
import os 
import random
import time
import keyboard  

FOLDER_PATH = r"D:\Python\WallpaperChange"  
WALLPAPERS_LIST = os.listdir(os.path.join(FOLDER_PATH, "images"))
print("Press '1' to stop...")  # Display message
while True:
    WALLPAPER_RANDOM = random.choice(WALLPAPERS_LIST)
    FULL_PATH = os.path.join(FOLDER_PATH, "images", WALLPAPER_RANDOM)

    ctypes.windll.user32.SystemParametersInfoW(20, 0, FULL_PATH, 0x01 | 0x02)
    time.sleep(1)  

    if keyboard.is_pressed('1'):  
        break




