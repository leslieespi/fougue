import pandas as pd
import glob
import os 
import csv

f1 = open('Fougue/database/__pycache__/colors/masterfaces.csv', 'w', encoding='UTF8')

files = os.path.join("Fougue/database/__pycache__/faces", "faces*.csv")


files = glob.glob(files)

df = pd.concat(map(pd.read_csv, files), ignore_index=True)


df.to_csv('Fougue/database/__pycache__/faces/masterfaces.csv')


f1.close()