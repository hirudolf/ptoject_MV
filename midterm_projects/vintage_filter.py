import numpy as np, cv2

def make_noise(std, image):
    noisy_image = image.copy()
    height, width, channels = noisy_image.shape
    for i in range(height):
        for j in range(width):
            for c in range(channels):
                noise = np.random.normal()
                set_noise = std * noise
                noisy_image[i][j][c] = noisy_image[i][j][c] + set_noise
    return noisy_image

image = cv2.imread("../images/Lenna.png")
if image is None: raise Exception("영상 읽기 오류")

blur = cv2.bilateralFilter(image,9,75,75)

std_dev = 15
noisy_image = make_noise(std_dev, image)

sepia_mask = np.asarray([[0.272, 0.534, 0.131],
                         [0.349, 0.684, 0.168],
                         [0.393, 0.769, 0.189]], dtype=np.float32)

sepia_img = cv2.transform(noisy_image, sepia_mask)

cv2.imshow("dst1",image)
cv2.imshow("blur Noisy Sepia", sepia_img.astype(np.uint8))
cv2.waitKey(0)
