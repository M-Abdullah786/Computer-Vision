# Chapter 1 started

# Importing CV2 package
import cv2
print("Package Imported")
# Importing Image
img = cv2.imread("resources/mona_lisa.png")
cv2.imshow("Mona Lisa Image", img)
cv2.waitKey(0) # 0 means adding infinte delay

# for video
cap = cv2.VideoCapture("resources/test_video.mp4") #path
while True:
     success, vid = cap.read()
     cv2.imshow("test_video", vid)
     if cv2.waitKey(1) & 0xFF == ord('q'): # to break video press q
         break

# for webcam
webcam = cv2.VideoCapture(0) #path
webcam.set(3, 640)
webcam.set(4, 480)
webcam.set(10,100)
while True:
    success, vid = webcam.read()
    cv2.imshow("Webcam", vid)
    if cv2.waitKey(1) & 0xFF == ord('q'): # to break video press q
        break

# End of Chapter 1
