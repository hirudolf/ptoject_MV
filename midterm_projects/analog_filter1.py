import numpy as np
import cv2

def add_film_noise(image, strength=0.1):
    h, w, c = image.shape
    noise = np.random.randn(h, w, c) * strength * 255
    noisy_image = np.clip(image + noise, 0, 255).astype(np.uint8)
    return noisy_image

def tone_down(image, saturation=0, brightness=0):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV).astype(np.float32)
    hsv[:, :, 1] -= saturation
    hsv[:, :, 2] -= brightness
    return cv2.cvtColor(hsv.clip(0, 255).astype(np.uint8), cv2.COLOR_HSV2BGR)

image = cv2.imread("../images/Lenna.png")
if image is None: raise Exception("영상 파일 읽기 오류")

rows, cols = image.shape[:2]
exp = 1.5
scale = 1
mapy, mapx = np.indices((rows, cols),dtype=np.float32)
mapx = 2*mapx/(cols-1)-1
mapy = 2*mapy/(rows-1)-1
r, theta = cv2.cartToPolar(mapx, mapy)
r[r< scale] = r[r<scale] **exp
mapx, mapy = cv2.polarToCart(r, theta)
mapx = ((mapx + 1)*cols-1)/2
mapy = ((mapy + 1)*rows-1)/2

dst1 = cv2.remap(image,mapx,mapy,cv2.INTER_LINEAR)
dst2 = tone_down(dst1, saturation=30, brightness=30)
dst3 = add_film_noise(dst2, strength=0.1)

cv2.imshow('dst3', dst3)
cv2.waitKey(0)
cv2.destroyAllWindows()





