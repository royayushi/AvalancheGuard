import cv2
humancascade=cv2.CascadeClassifier('haarcascade_fullbody.xml')
image_path="testimg.jpg"
image=cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

humans = humancascade.detectMultiScale(gray, 1.9, 1)
print(humans)
while(True):
    ret, image = cap.read()


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    humans = human_cascade.detectMultiScale(gray, 1.9, 1)
    
    for (l,b,w,h) in humans:
         cv2.rectangle(frame,(l,b),(l+b,w+h),(255,0,0),2)
    cv2.imshow("image",image)
    cv2.waitKey(1)
