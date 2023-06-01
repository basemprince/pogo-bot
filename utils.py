import json
import pandas as pd
import os
from adbutils import adb
import scrcpy.core as scrcpy
from difflib import get_close_matches
import numpy as np
import cv2
from PIL import Image
import re
import yaml


def connect_to_device(ip):
    adb.connect("127.0.0.1:5037")
    try:
        client = scrcpy.Client(device=adb.device_list()[0])
    except IndexError:
        raise Exception("No devices connected.")

    client.start(threaded=True)
    print(f'Connected to: {client.device_name}')
    return client

def get_next_filename(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        
    files = os.listdir(directory)
    files = [f for f in files if f.endswith('.mp4')]
    
    if not files:
        return os.path.join(directory, '1.mp4')
    else:
        nums = sorted([int(f.split('.')[0]) for f in files])
        next_num = nums[-1] + 1
        return os.path.join(directory, f'{next_num}.mp4')
    
