import numpy as np
from matplotlib import pyplot as plt
import os 
from PIL import Image
import cv2 

data_dir = "C:\\Users\\malko\\Desktop\\Skola\\Labbar AI\\Labb1\\pictures\\"

categories = os.listdir(data_dir)
num_categories = len(categories)

images = []
print(categories)
x, y = 100, 100

for category in categories:
    category_path = os.path.join(data_dir, category)
    for filename in os.listdir(category_path):
        img_path = os.path.join(category_path, filename)
        img = cv2.imread(img_path)
        img = cv2.resize(img, (x, y))  # Resize to the desired resolution
        images.append(img)

images[1].show()
