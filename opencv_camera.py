#before running this code in python install opencv by using pip
#run this in your command propt 
#"pip install opencv from internet"
#"use cmd prompt to instsllpackage"


import cv2
def capture():
    cap=cv2.VideoCapture(0)
    if not cap.isOpened():
        print("error web cam is not opened")
        exit()
    iscaptured,frame=cap.read()
    if iscaptured:
        return frame
    cap.release()
    cv2.destroyAllWindows()
capture()
