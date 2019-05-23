import cv2
import face_recognition
import numpy as np
import threading
import time


def face_filters():
    global frame
    global last_filter
    while True:
        image = np.array(frame)
        faces = face_recognition.face_locations(image)
        print(faces)
        last_filter = gen_filters(image, faces)
        time.sleep(1)


def gen_filters(image, boxes):
    return image


def combine_images(filter, img):
    return img


if __name__ == '__main__':
    cv2.namedWindow("video")
    # cv2.namedWindow("ir")
    video = cv2.VideoCapture(0)
    ir = cv2.VideoCapture(2)
    filters = threading.Thread(target=face_filters)
    rval, frame = video.read()
    filters.start()
    while rval:
        # rval, frame = ir.read()
        # cv2.imshow("ir", frame)
        rval, frame = video.read()
        if last_filter.any():
            img = combine_images(last_filter, frame)
        else:
            img = frame
        cv2.imshow("video", img)
        key = cv2.waitKey(20)
        if key == 27:  # exit on ESC
            break
    filters.join()
    cv2.destroyWindow("video")
    # cv2.destroyWindow("ir")


