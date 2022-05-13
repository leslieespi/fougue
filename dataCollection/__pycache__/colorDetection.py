from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import cv2
from collections import Counter
from skimage.color import rgb2lab, deltaE_cie76
import os
import csv






def RGB2HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))

def get_image(image_path):
    image = image_path
    image = cv2.cvtColor(image_path, cv2.COLOR_BGR2RGB)
    return image


def get_colors(image, number_of_colors, show_chart):
    
  #check for a proper image through its dimensions
    if len(image) <= 0:
        return 0,0

    
    if image.shape[0] == 0 or image.shape[1] == 0:
        return 0,0
    # print(image.shape[:2])
    new_img = cv2.resize(image, (600, 400), interpolation = cv2.INTER_AREA)



    new_img = new_img.reshape(new_img.shape[0]*new_img.shape[1], 3)


    clf = KMeans(n_clusters = numColors)
    labels = clf.fit_predict(new_img)


    counts = Counter(labels)

    #
    midColor = clf.cluster_centers_

    oColors = [midColor[i] for i in counts.keys()]
    hexColors = [RGB2HEX(oColors[i]) for i in counts.keys()]
    rgbColors = [oColors[i] for i in counts.keys()]

    if (show_chart):
        plt.figure(figsize = (10, 8))


        plt.pie(counts.values(), labels = hexColors, colors = hexColors)
        plt.show()

    #return list of colors and the success flag
    
    #return hexColors

    return hexColors, 1




#running python program will give an example using a sample image
get_colors(get_image('person.jpeg'), 10, True)
