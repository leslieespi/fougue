import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgba_array
import csv
import os.path


ide = []
color1 = []
color2 = []
color3 = []
color4 = []
color5 = []



with open('master2.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        ide.append(row[0])
        color1.append(row[2])
        color2.append(row[3])
        color3.append(row[4])
        color4.append(row[5])
        color5.append(row[6])

        # data = color2 + color3 + color4 + color5
        # plt.imshow(to_rgba_array(data).reshape(2,2,4))
        # plt.show()  


# color1.append(color2)
# color1.append(color3)
# color1.append(color4)
# color1.append(color5)

data = color2 + color3 + color4 + color5
# data2 = []
# for d in data:
#     data2.append(hex_to_rgb(d))


print(len(data))
  
# plt.show()

plot = to_rgba_array(data).reshape(12,487,8)
plt.imshow(plot)
plt.show()


