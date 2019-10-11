import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image
from project7test1 import image_process
import glob
import json 

# D:\semproject\road_dataset\road_dataset\label_data_0313.json

# D:\semproject\road_dataset\road_dataset\label_data_0531.json

# D:\semproject\road_dataset\road_dataset\label_data_0601.json    

count=1

# with open('C:\\Users\\arind\\Downloads\\label_data_0601.json', 'r') as f:
#     data = json.load(f)
# for x in data["imagedata"]:
#     image_process(x["lanes"],x["h_samples"],x["raw_file"],count)
#     count=count+1

# with open('C:\\Users\\arind\\Downloads\\label_data_0531.json', 'r') as f:
#     data = json.load(f)
# for x in data["imagedata"]:
#     image_process(x["lanes"],x["h_samples"],x["raw_file"],count)
#     count=count+1

with open('C:\\Users\\arind\\Downloads\\label_data_0313.json', 'r') as f:
    data = json.load(f)
for x in data["imagedata"]:
    image_process(x["lanes"],x["h_samples"],x["raw_file"],count)
    count=count+1
