import cv2

cv2.namedWindow("video")
cv2.namedWindow("ir")
video = cv2.VideoCapture(0)
ir = cv2.VideoCapture(2)

if video.isOpened(): # try to get the first frame
    rval, frame = video.read()
else:
    rval = False

while rval:
    cv2.imshow("ir", frame)
    rval, frame = video.read()
    cv2.imshow("video", frame)
    rval, frame = ir.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cv2.destroyWindow("video")
cv2.destroyWindow("ir")

def get_frame(camera=0):
    pass


