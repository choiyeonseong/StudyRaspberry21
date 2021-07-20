import cv2
import numpy as np  # C#의 리스트, 행렬이 포함되어있지 않아서 numpy 필요

# 이미지 로드 기본틀
## 이미지 흐리게 하기 (Blur)
org = cv2.imread('./image/cat.jpg', cv2.IMREAD_REDUCED_COLOR_2)
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)    # 흑백
blur = cv2.blur(org, (10,10))   # (2,2)보다 (10,10)이 더 흐릿
kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
sharp = cv2.filter2D(org,-1,kernel)

cv2.imshow('Original', org)  # 이미지를 새창에서 띄우기
cv2.imshow('Blur', blur)    # 블러 이미지
cv2.imshow('Sharp', sharp)  # 선명한 이미지

cv2.waitKey(0)  # 창에서 키 입력 대기
cv2.destroyAllWindows() # 메모리 해제

