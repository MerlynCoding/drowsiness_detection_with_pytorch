import os

from model import *

image_path = os.path.join(os.getcwd(),'dataset', 'images')
os.makedirs(image_path, exist_ok=True)
print(image_path)
labels=['awake','drowsy']
total_images=20

cap=cv2.VideoCapture(0)
for label in labels:
    print(f'colllecting images for : {label}')
    time.sleep(2)

    for num in range(total_images):
        print(f'collecting images number :{num}')

        ret,frame=cap.read()
        img_name=os.path.join(image_path,label+' '+str(uuid.uuid1())+'.jpg')
        cv2.imwrite(img_name,frame)
        cv2.imshow('take_photo',frame)
        time.sleep(2)

cap.release()
cv2.destroyAllWindows()
