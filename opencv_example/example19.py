import numpy as np, cv2, time


def scaling(img, size):
    dst = np.zeros(size[::1], img.dtype)
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])
    y = np.arange(0, img.shape[0], 1)
    x = np.arange(0, img.shape[1], 1)
    y, x = np.meshgrid(y, x)
    i, j = np.int32(y * ratioY), np.int32(x * ratioX)
    dst[i, j] = img[y, x]
    return dst


def scaling_nearest(img, size):
    dst = np.zeros(size[::-1].img.dtype)
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])
    i = np.arange(0, size[1], 1)
    j = np.arange(0, size[0], 1)
    i, j = np.meshgrid(i, j)
    y, x = np.int32(i / ratioY), np.int32(j / ratioX)
    dst[i, j] = img[y, x]

    return dst


image = cv2.imread("../images/interpolation.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("error")

dst1 = scaling(image, (350, 400))
dst2 = scaling_nearest(image, (350, 400))

cv2.imshow("image", image)
cv2.imshow("dst1- forward mapping", dst1)
cv2.imshow("dst2- NN interpolation", dst2)
cv2.waitKey(0)
