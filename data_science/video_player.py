import cv2
filepath=r"C:\Users\91630\Downloads\istockphoto-1356315742-640_adpp_is.mp4"
video = cv2.VideoCapture(filepath)

while True:
    status, frame = video.read()
    if not status:
        break
    cv2.imshow("webcam 0",frame)    #displays a window with the webcam
    if cv2.waitKey(1) == ord('q'):  # if the key is q, the loop breaks
        break
video.release()                     # releases the webcam
cv2.destroyAllWindows()             # closes all windows