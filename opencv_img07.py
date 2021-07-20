import cv2
import numpy as np  # C#의 리스트, 행렬이 포함되어있지 않아서 numpy 필요

# 이미지 로드 기본틀
## 영상 둘레 표시 컨투어
org = cv2.imread('./image/cat.jpg')
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)

ret, bny = cv2.threshold(gray, 127, 225, 0)
cont, hirc = cv2.findContours(bny, cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(org, cont, -1,(255,0,0), 1)
cv2.imshow('Thr', bny)
cv2.imshow('Result', org)  # 이미지를 새창에서 띄우기

cv2.waitKey(0)  # 창에서 키 입력 대기
cv2.destroyAllWindows() # 메모리 해제

