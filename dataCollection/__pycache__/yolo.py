import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def findPerson(photo):

    yolo = cv2.dnn.readNet("./yolov3.weights", "./yolov3.cfg")


    classes = []

    with open("./coco.names",'r') as f:
        classes = f.read().splitlines()

    
    # print(len(classes))

    img = cv2.imread(photo,1)

    im = Image.open(photo)

    blob = cv2.dnn.blobFromImage(img, 1/255, (320,320), (0,0,0), swapRB=True, crop=False)

    i = blob[0].reshape(320,320,3)

    width = img.shape[1]
    height = img.shape[0]


    

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


    yolo.setInput(blob)

    output_layers_name = yolo.getUnconnectedOutLayersNames()

    outputl = yolo.forward(output_layers_name)

    boxes = []
    conf = []
    class_ids = []

    for output in outputl:
        for d in output:


            score = d[5:]
            class_id = np.argmax(score)
            confidence = score[class_id]
            if confidence > 0.7:
                center_x = int(d[0]*width)
                center_y = int(d[1]*height)

               
                w = int(d[2]*width)
                h = int(d[3]*height)

                x = int(center_x- w/2)
                y = int(center_y- h/2)

                boxes.append([x,y,w,h])
                conf.append(float(confidence))
                class_ids.append(class_id)
                


    indexes = cv2.dnn.NMSBoxes(boxes, conf, 0.5, 0.4)

    font = cv2.FONT_HERSHEY_PLAIN
    colors =np.random.uniform(0, 255, size=(len(boxes),3))
    if len(indexes) == 0:
        return 0 , 0, 0
    # print(width)
    # print(height)
    for i in indexes.flatten():
        x,y,w,h = boxes[i]
        
        label = str(classes[class_ids[i]])
        
        confi = str(round(conf[i],2))
        color = colors[i]
        

        

        
        if label == "person":
            print(label)
            flag = 1
            # print("(", x, ",", y, ")")
            # print("(", x+w, ",", y+h, ")")
            img = cv2.rectangle(img, (x,y), (x+w,y+h), color, 2)
            img = cv2.putText(img, label + " "+confi, (x,y+50), font, 1, (255,255,255), 3)
            plt.imshow(img)
            plt.show()
            im1 = img[y:y+h, x:x+w]
            # plt.imshow(im1)
            # plt.show()


            row = im1.shape[0], im1.shape[1], 'jan', 2022, 's'

            # print(row)
            return im1, row, flag
        
        elif label != "person":
            im1 = 0
            row = [0]
            flag = 0


    return im1, row, flag


findPerson("/Users/leslieespinosa/Fougue/YOLO/Vogue_19720415_0159_008_0001_r.jpg")

# findPerson("/Users/leslieespinosa/Fougue/YOLO/Vogue_20070601_0197_006_0001_r.jpg")

# findPerson("/Users/leslieespinosa/Fougue/YOLO/Vogue_20130401_0203_004_0001_r.jpg")
