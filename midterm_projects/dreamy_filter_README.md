# dreamy_filter
이 필터는 saturation 함수를 정의하여 hsv[:,:,1] += saturation으로 채도를 증가시켜주고
cv2.add 함수를 사용해 밝기를 높여주었습니다.
그 다음 입력 cv2.GaussianBlur를 사용하여 이미지를 부드럽게 만들어 몽환적인 효과를 주는 필터를 만들었습니다.

## 변경전
![img_1.png](img_1.png)
## 변경후
![img_2.png](img_2.png)