from model import *

model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp15/weights/last.pt', force_reload=True)
cap=cv2.VideoCapture(0)
while cap.isOpened():

    ret,frame=cap.read()
    results=model(frame)
    cv2.imshow('CAMERA',np.squeeze(results.render()))
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break

cv2.release()
cv2.destroyAllWindows()
