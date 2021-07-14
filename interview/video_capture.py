import numpy as np
import cv2




class WebCam(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        #self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        #self.out = cv2.VideoWriter('output.avi',self.fourcc, 20.0, (640,480))


    def __del__(self):
        self.video.release()
        self.out.release()
        


    def capture(self):
        success, image = self.video.read()
        

        #out.write(image)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        frame_flip = cv2.flip(image, 1)
        ret , jpeg = cv2.imencode('.jpg', frame_flip)
        return jpeg.tobytes()

        

