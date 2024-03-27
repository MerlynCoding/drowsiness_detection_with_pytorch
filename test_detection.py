import cv2

from model import  *
model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5x.pt')
image="https://ultralytics.com/images/zidane.jpg"
results=model(image)
print(results)

cap=cv2.VideoCapture(0)
while cap.isOpened():

    ret,frame=cap.read()
    results=model(frame)
    cv2.imshow('CAMERA',np.squeeze(results.render()))
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break

cv2.release()
cv2.destroyAllWindows()
