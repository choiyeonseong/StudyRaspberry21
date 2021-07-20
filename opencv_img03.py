import cv2
import numpy as np  # C#의 리스트, 행렬이 포함되어있지 않아서 numpy 필요

# 이미지 로드 기본틀
org = cv2.imread('./image/cat.jpg')
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)    # 흑백

h, w, c = org.shape

cropped = gray[:, :int(w/2)] # 넓이 반 자르기
# cropped = gray[:int(h/2), :] # 높이 반 자르기

cv2.imshow('Original', org)  # 이미지를 새창에서 띄우기
cv2.imshow('Cropped', cropped)  # 반으로 자른 흑백 이미지

cv2.waitKey(0)  # 창에서 키 입력 대기
cv2.destroyAllWindows() # 메모리 해제

