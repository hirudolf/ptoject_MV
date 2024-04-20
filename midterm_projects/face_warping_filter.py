import numpy as np, cv2
import dlib

def load_landmarks(image, predictor, detector):
    gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    if len(faces) > 0:
        landmarks = predictor(gray, faces[0])
        return np.array([[p.x, p.y] for p in landmarks.parts()], dtype=np.int32)
    return None

image = cv2.imread("../images/Lenna.png")
if image is None: raise Exception("영상 파일 읽기 오류")

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
landmarks = load_landmarks(image, predictor, detector)