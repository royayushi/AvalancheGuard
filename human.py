import cv2
import numpy as np
import imutils

proto = "MobileNetSSD_deploy.prototxt"
model = "MobileNetSSD_deploy.caffemodel"
detect = cv2.dnn.readNetFromCaffe(prototxt=proto, caffeModel=model)

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]


def main():
    image = cv2.imread('testimg.jpg')
    image = imutils.resize(image, width=600)

    (H, W) = image.shape[:2]

    blob = cv2.dnn.blobFromImage(image, 0.007843, (W, H), 127.5)

    detect.setInput(blob)
    person_detections = detect.forward()

    for i in np.arange(0, person_detections.shape[2]):
        confidence = person_detections[0, 0, i, 2]
        if confidence > 0.5:
            idx = int(person_detections[0, 0, i, 1])

            if CLASSES[idx] != "person":
                continue

            person_box = person_detections[0, 0, i, 3:7] * np.array([W, H, W, H])
            (startX, startY, endX, endY) = person_box.astype("int")

            cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)

    cv2.imshow("Results", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()