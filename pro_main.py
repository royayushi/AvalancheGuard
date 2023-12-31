import cv2
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import pywhatkit
import datetime
img=cv2.imread("static\\testimg1.jpeg")
classname=[]
classfile='coco.names'
with open(classfile,'rt') as f:
    classname=f.read().rstrip('\n').split('\n')
proto= 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
model='frozen_inference_graph.pb'
net=cv2.dnn_DetectionModel(proto,model)
net.setInputSize(320,320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5, 127.5, 127.5))

net.setInputSwapRB(True)
classids,confs,bbox=net.detect(img,confThreshold=0.5)
#print(classids,bbox)
for classid,confidencebox,box in zip(classids.flatten(),confs.flatten(),bbox):
    cv2.rectangle(img,box,color=(0,255,0),thickness=4)
    cv2.putText(img, classname[classid-1], (box[0] + 10, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
cv2.imshow("image",img)    
cv2.waitKey(0)
'''
sender_email = 'ishanroybarman845@gmail.com'
sender_password = 'Ishan125#'
recipient_email = 'akashsrimani.2002@gmail.com'

def send_email_notification():
    subject = 'Human Detected Alert'
    message = 'A human has been detected.'

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    text = MIMEText(message)
    msg.attach(text)

    try:

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        print('Notification email sent successfully.')

    except Exception as e:
        print('Error sending notification email:', str(e))
'''
# def detect_human():
#     human_detected = True
#     if human_detected:
#         send_email_notification()
# detect_human()
# pywhatkit.sendwhatmsg_instantly("+918967570225", "Person_detected", 0, 0)# 0,0 indicates instant 