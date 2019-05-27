import cv2
import face_recognition
import numpy as np
import threading
import time


def find_faces():
    global frame
    global last_filter
    while True:
        image = np.array(frame)
        last_filter = face_recognition.face_locations(image)
        # print(faces)
        # last_filter = gen_filters(image, faces)
        time.sleep(1)


def apply_filter(last_filter, frame):
    print(frame.shape)
    for face in last_filter:
        points = [(face[0], face[1]), (face[2], face[3])]
        for point in points:
            frame[point] = [255, 0, 0]
    return frame
        

if __name__ == '__main__':
    cv2.namedWindow("video")
    # cv2.namedWindow("ir")
    video = cv2.VideoCapture(0)
    ir = cv2.VideoCapture(2)
    last_filter = []
    filters = threading.Thread(target=find_faces)
    rval, frame = video.read()
    filters.start()
    while rval:
        # rval, frame = ir.read()
        # cv2.imshow("ir", frame)
        rval, frame = video.read()
        # print(frame)

        img = apply_filter(last_filter, frame)
        cv2.imshow("video", img)
        key = cv2.waitKey(20)
        if key == 27:  # exit on ESC
            break
    filters.join()
    cv2.destroyWindow("video")
    # cv2.destroyWindow("ir")
