import cv2
import numpy as np  # C#의 리스트, 행렬이 포함되어있지 않아서 numpy 필요

# 이미지 로드 기본틀
## 노이즈 추가
org = cv2.imread('./image/cat.jpg', cv2.IMREAD_REDUCED_COLOR_2)
h,w,c = org.shape
noise = np.uint8(np.random.normal(loc=0, scale=80,size=[h,w,c]))
noised_img = cv2.add(org, noise)    # 원본 이미지에 노이즈 추가

cv2.imshow('Original', org)  # 이미지를 새창에서 띄우기
cv2.imshow('Noise', noised_img) # 노이즈 이미지

cv2.waitKey(0)  # 창에서 키 입력 대기
cv2.destroyAllWindows() # 메모리 해제

