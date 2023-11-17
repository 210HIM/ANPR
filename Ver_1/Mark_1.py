# from tkinter import *
# from PIL import Image, ImageTk
# import cv2 as cv
#
# class Read:
#     def __init__(self):
#         self.root = None
#         self.vid_EX = None
#
#     def guifream(self):
#         self.root = Tk()
#         self.root.geometry("200x200")
#         self.vid_label = Label(self.root)
#         self.vid_label.pack()
#         self.vid_EX = cv.VideoCapture('0')
#         self.read_video()
#
#     def read_video(self):
#         isTrue, frame = self.vid_EX.read()
#         cv.rectangle(frame,(730,420),(2,180),(0,255,0),thickness=2)
#         opencv_image = cv.cvtColor(frame, cv.COLOR_BGR2RGBA)
#         captured_image = Image.fromarray(opencv_image)
#         photo_image = ImageTk.PhotoImage(image=captured_image)
#         self.vid_label.photo_image = photo_image
#         self.vid_label.configure(image=photo_image)
#         self.vid_label.after(25, self.read_video)
#
# obj = Read()
# obj.guifream()
# mainloop()

import cv2
import pytesseract
import imutils

# Load the number plate detection model (e.g., YOLO)
net = cv2.dnn.readNet("C:/Users/rakes/Desktop/yolov3.weights", "C:/Users/rakes/Desktop/yolov3.cfg")
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

# Initialize video capture
cap = cv2.VideoCapture("Videos/car.mp4")

# Configure Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Number plate detection
    height, width, channels = frame.shape
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    class_ids = []
    confidences = []
    plates = []

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = center_x - w / 2
                y = center_y - h / 2

                class_ids.append(class_id)
                confidences.append(float(confidence))
                plates.append(frame[int(y):int(y+h), int(x):int(x+w)])

    # Text extraction from detected plates using Tesseract
    for plate in plates:
        gray_plate = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray_plate)
        print("Detected Number Plate:", text)

    # Display the video with bounding boxes (optional)
    cv2.imshow("Number Plate Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
