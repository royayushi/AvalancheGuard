import cv2
import imutils

# Initializing the HOG person
# detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cap = cv2.imread('C:\Users\Dhrubojyoti\Desktop\Python in 100 days\object-detector\WhatsApp Image 2023-09-19 at 1.31.01 PM (1).jpeg')

while cap.isOpened():
	ret, image = cap.read()
	if ret:
		image = imutils.resize(image,
							width=min(400, image.shape[1]))

		(regions, _) = hog.detectMultiScale(image,
											winStride=(4, 4),
											padding=(4, 4),
											scale=1.05)

		for (x, y, w, h) in regions:
			cv2.rectangle(image, (x, y),(x + w, y + h),(0, 255, 0), 2)
			cv2.putText(image, "status:{}".format("Detected"),(10,20),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),2)


		# Showing the output Image
		cv2.imshow("Image", image)
		if cv2.waitKey(25) & 0xFF == ord('q'):
			break
	else:
		break

cap.release()
cv2.destroyAllWindows()