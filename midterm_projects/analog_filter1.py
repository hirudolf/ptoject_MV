import cv2
import numpy as np

def filter(image, mask):
    sharpened_img = cv2.filter2D(image, -1, mask)
    return sharpened_img
def tone_down(image, tone_down_level=50):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv[:, :, 2] -= tone_down_level
    toned_down_image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return toned_down_image

image = cv2.imread("../images/Lenna.png")
print(image.shape)
rows, cols = image.shape[:2]
if image is None:
    raise Exception("영상 파일 읽기 오류")

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

distorted = cv2.remap(image,mapx,mapy,cv2.INTER_LINEAR)
dst1 = tone_down(distorted, tone_down_level=50)

cv2.imshow('dst1', dst1)
cv2.waitKey(0)
cv2.destroyAllWindows()


