from flask import Flask, render_template, request, send_file
import cv2
import os

app = Flask(__name__)

# Function for object detection
classname=[]

# def detect_objects(image_path, output_path):
def detect_objects(image_path, output_path):

    global classname
    img = cv2.imread(image_path)

    classfile = 'coco.names'
    with open(classfile, 'rt') as f:
        classname = f.read().rstrip('\n').split('\n')
    proto = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
    model = 'frozen_inference_graph.pb'
    net = cv2.dnn_DetectionModel(proto, model)
    net.setInputSize(320, 320)
    net.setInputScale(1.0/127.5)
    net.setInputMean((127.5, 127.5, 127.5))

    net.setInputSwapRB(True)
    classids, confs, bbox = net.detect(img, confThreshold=0.5)

    for classid, confidencebox, box in zip(classids.flatten(), confs.flatten(), bbox):
        cv2.rectangle(img, box, color=(0, 255, 0), thickness=4)
        cv2.putText(img, classname[classid-1], (box[0] + 10, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)

    # Save the modified image with bounding boxes
    cv2.imwrite(output_path, img)

    return classids, confs, bbox

@app.route("/base")
def base():
    return render_template('base.html')

@app.route("/", methods=['GET', 'POST'])
@app.route("/home")
def home_page():
    # Route for the main page
    if request.method == 'POST':
        # Get the uploaded file from the form
        file = request.files['file']

        if file:
            # Save the uploaded file temporarily
            uploaded_image_path = 'static/uploads/temp.jpg'
            file.save(uploaded_image_path)

            # Perform object detection and save the modified image
            modified_image_path = 'static/detected_image.jpg'
            classids, confs, bbox = detect_objects(uploaded_image_path, modified_image_path)

            detection_results = [(classname[classid - 1], confidence) for classid, confidence in zip(classids.flatten(), confs.flatten())]

            # Render the template with the paths to the uploaded and modified images
            return render_template('home.html', detection_results=detection_results, uploaded_image_path=uploaded_image_path, modified_image_path=modified_image_path)

    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

