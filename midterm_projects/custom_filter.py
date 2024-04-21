import cv2
import numpy as np

wave = 20
amp = 15

image = cv2.imread("../images/Lenna.png")
if image is None: raise Exception("영상 파일 읽기 오류")

rows, cols = image.shape[:2]
mapy, mapx = np.indices((rows, cols),dtype=np.float32)

sinx = mapx + amp * np.sin(mapy/wave)
cosy = mapy + amp * np.cos(mapx/wave)

image_sinx=cv2.remap(image, sinx, mapy, cv2.INTER_LINEAR)
image_cosy=cv2.remap(image, mapx, cosy, cv2.INTER_LINEAR)

image_both=cv2.remap(image, sinx, cosy, cv2.INTER_LINEAR, \
                    None, cv2.BORDER_REPLICATE)

cv2.imshow('image', image_both)
cv2.waitKey()
cv2.destroyAllWindows()