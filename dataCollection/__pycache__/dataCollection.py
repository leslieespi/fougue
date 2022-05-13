from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import cv2
from collections import Counter
from skimage.color import rgb2lab, deltaE_cie76
import os
import csv

from yolo import findPerson
from colorDetection import get_colors, get_image
from dateFinder import *

def analyze(file):
    

    date = findDate(file)
    
    cropped, yolo, found = findPerson(file)


    
    if found == 1:


 
        person = cropped
        colors, flag = get_colors(person, 5, True)

        if flag == 0:
            return 0,0,0,0
        # else:
        #     person = np.asarray(cropped)
        #     return 0,0,0


        return yolo, colors, 1, date


    elif found == 0:
        return 0, 0, 0, date


def main():

    # directory = '/Volumes/Photography/Covers'
    # directory = '/Volumes/easystore/Vogue/ProcessedDataFromLibrary/CoversOnly/Covers'
    # directory = '/Users/leslieespinosa/Fougue/files'

    ##open csv files to write to
    f1 = open('/Fougue/database/__pycache__/faces.csv', 'w', encoding='UTF8')
    f2 = open('/Fougue/database/__pycache__/colors.csv', 'w', encoding='UTF8')
    f3 = open('/Fougue/database/__pycache__/master.csv', 'w', encoding='UTF8')

    writer1 = csv.writer(f1)
    writer2 = csv.writer(f2)
    writer3 = csv.writer(f3)

    h1 = ['id', 'x', 'y', 'month', 'year', 'season']
    h2 = ['id', 'color1', 'color2', 'color3', 'color4', 'color5']
    h3 = ['date', 'x', 'y', 'color1', 'color2', 'color3', 'color4', 'color5']

    writer1.writerow(h1)
    writer2.writerow(h2)
    writer3.writerow(h3)



    
    #loop through each image and analyze
    for filename in os.listdir(directory):
        
        # f = open('/Users/leslieespinosa/Fougue/database/__pycache__/faces.csv', 'w', encoding='UTF8')
        f = directory + '/' + filename

        
        yolo, colors, success, date = analyze(f)

        


        if success == 1:
            neww = [date, yolo[0], yolo[1], colors[0], colors[1], colors[2], colors[3]]
            print(neww)
            writer1.writerow(yolo)
            writer2.writerow(colors)
            writer3.writerow(neww)
            

            
        #return faces.row and colors.row
        #write to faces and row csv

    print("done")
    #close csv files


if __name__ == "__main__":
    main()
