import numpy as np, cv2

image = cv2.imread("../images/Lenna.png")
if image is None: raise Exception("영상 파일 읽기 오류")

mask = np.asarray([[0.272, 0.534, 0.131],
                   [0.349, 0.684, 0.168],
                   [0.393, 0.769, 0.189]], dtype=np.float32)
sepia_img = cv2.transform(image, mask)

cv2.imshow("sharpening_img", sepia_img)
cv2.waitKey(0)


import numpy as np
import cv2

def filter(image, mask):
    sharpened_img = cv2.filter2D(image, -1, mask)
    return sharpened_img

image = cv2.imread("../images/Lenna.png")
if image is None: raise Exception("영상 파일 읽기 오류")


mask = np.asarray([[0.272, 0.534, 0.131],
                   [0.349, 0.684, 0.168],
                   [0.393, 0.769, 0.189]], dtype=np.float32)
sepia_img = cv2.transform(image, mask)


data2 = [[-1, -1, -1],
         [-1, 9, -1],
         [-1, -1, -1]]
mask2 = np.array(data2, np.float32)


sharpened_img = filter(sepia_img, mask2)

cv2.imshow("image", image)
cv2.imshow("sharpened_img", sharpened_img)
cv2.waitKey(0)