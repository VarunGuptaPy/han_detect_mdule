# han_detect_mdule
this py file should be in your folder 📂 
first you have to write this line to work in my module #important 
tracker = HandDetector()
to detct your hand you have to type:
import handtrackingmodule as hr
import cv2
cap = cv2.VideoCapture(0)
while True:
    trackor= hr.HandDetector()
    success, img = cap.read()
    img = trackor.findhands(img)
    cv2.imshow("Video",img)
    cv2.waitKey()
to find position of all point type
import cv2
cap = cv2.VideoCapture(0)
detector = HandDetector()
    while True:
        success,img = cap.read()
        img = detector.findhands(img)
        list1 = detector.findPosition(img)
        print(list1)
        cv2.imshow("image", img)
        cv2.waitKey(1)
