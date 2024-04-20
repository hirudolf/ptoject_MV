import cv2
def saturation(image, saturation=0):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv[:,:,1] += saturation
    addimage = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return addimage

image = cv2.imread("../images/Lenna.png")
if image is None: raise Exception("영상 파일 읽기 오류")

dst1 = cv2.GaussianBlur(image, (0,0), 3)
dst2 = cv2.add(dst1,50)
dst3 = saturation(dst2, saturation=60)

cv2.imshow('dst1', dst3)
cv2.waitKey()
cv2.destroyAllWindows()

