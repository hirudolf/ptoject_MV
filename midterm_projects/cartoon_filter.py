import cv2
import numpy as np


def cartoon_filter(image, ksize=5, sketch_intensity=0.5, color_intensity=0.5, clusters=8):
    pixels = image.reshape((-1, 3))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, labels, centers = cv2.kmeans(pixels.astype(np.float32), clusters, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(centers)
    res = centers[labels.flatten()]

    result_image = res.reshape((image.shape))

    gray = cv2.cvtColor(result_image, cv2.COLOR_BGR2GRAY)

    edges = cv2.medianBlur(gray, ksize)

    edges = cv2.adaptiveThreshold(edges, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    color = cv2.bilateralFilter(result_image, 9, 300, 300)
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    cartoon = cv2.addWeighted(color, color_intensity, cartoon, sketch_intensity, 0)

    return cartoon


image = cv2.imread("../images/Lenna.png")
if image is None:
    raise Exception("영상 파일 읽기 오류")

# 색상 단순화 및 카툰 필터 적용
cartoon_image = cartoon_filter(image, ksize=5, sketch_intensity=0.5, color_intensity=0.5, clusters=8)

cv2.imshow('Cartoon Filter', cartoon_image)
cv2.waitKey(0)
cv2.destroyAllWindows()