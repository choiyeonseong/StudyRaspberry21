import cv2
import numpy as np

org = cv2.imread('./image/cat.jpg') # 이미지 로드
# org = cv2.imread('./image/cat.jpg', cv2.IMREAD_GRAYSCALE) # 그레이 스케일 이미지 로드
dst = cv2.resize(org, dsize=(640, 480))

center = [310,240] # x, y
color_red = (0, 0, 255) # red
color_blue = (255, 0, 0)    # blue

cv2.rectangle(dst, (100, 100), (500, 300), color_blue) # 사각형
cv2.circle(dst, tuple(center), 30, color_red)   # 원

cv2.imshow("dest", dst)   # 이미지 창 띄우기

cv2.waitKey(0)  # 키 대기
cv2.destroyAllWindows() # OpenCV 인스턴스 종료