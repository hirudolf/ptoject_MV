# analog_filter
이 필터는 add_film_noise 함수를 정의하여 노이즈를 이미지에 추가합니다. 
그 다음 입력 hsv[:, :, 1] -= saturation로 채도를 감소시키고 
hsv[:, :, 2] -= brightness: 밝기를 감소시켜서 톤다운을 해 아날로그 카메라로
촬영한듯한 느낌을 주고 이미지의 특정좌표에 볼록왜곡을 추가해주었습니다.


## 변경전
![img_1.png](img_1.png)
## 변경후
![img_4.png](img_4.png)