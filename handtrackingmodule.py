import cv2
import mediapipe as mp
import time 
cap = cv2.VideoCapture(0)
class HandDetector():
    def __init__(self,mode=False,maxHands=2,detectionCon = 0.7,trackcon=0.5):
        self.mode= mode
        self.maxHands = maxHands
        self.detectionCon =detectionCon
        self.trackcon = trackcon
        self.mphands = mp.solutions.hands
        self.hands = self.mphands.Hands(self.mode,self.maxHands,self.detectionCon,self.trackcon)
        self.mpdraw = mp.solutions.drawing_utils
    def findhands(self,img,draw=True):

        imgrgb=  cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgrgb)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpdraw.draw_landmarks(img,handLms, self.mphands.HAND_CONNECTIONS)
        return img
    def findPosition(self,img,handNo=0, draw=True):
        list1 = []
        if self.results.multi_hand_landmarks:
            my_hand= self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(my_hand.landmark):
                h,w,c =img.shape
                cx,cy = int(lm.x*w), int(lm.y*h)
                list1.append([id, cx, cy])
        return list1
def main():
    cap = cv2.VideoCapture(0)
    detector = HandDetector()
    while True:
        success,img = cap.read()
        img = detector.findhands(img)
        list1 = detector.findPosition(img)
        print(list1)
        cv2.imshow("image", img)
        cv2.waitKey(1)
if __name__ == '__main__':
    main()