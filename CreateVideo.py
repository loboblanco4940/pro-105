import os
import cv2

path="Images/"

imagenes = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)   
        imagenes.append(file_name)

print(len(imagenes))
count = len(imagenes)

frame = cv2.imread(imagenes[0])
height, width, layers = frame.shape
size = (width,height)

out = cv2.VideoWriter('KDA.avi',cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)
for i in range(0,count):
     print(imagenes[i])
     frame = cv2.imread(imagenes[i])
     out.write(frame)
    
out.release() 
print("Listo")