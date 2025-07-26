import cv2

face_C=cv2.CascadeClassifier('opencv/haarcascade_frontalface_default.xml')
vedio= cv2.VideoCapture(0)
while vedio.isOpened():
    x,frame = vedio.read()
    faces = face_C.detectMultiScale(frame,1.2,5)
    for (x,y,w,h) in faces:
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.rectangle(frame,(x,y),((x+w),(y+h)),(0,0,255),3)
        cv2.imshow('video',frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    cv2.imshow('video',frame)

    # if cv2.waitKey(1) & 0xff == ord('q'):
    #     break

vedio.release()