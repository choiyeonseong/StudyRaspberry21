import cv2
import numpy as np
import datetime
from PIL import ImageFont, ImageDraw, Image

# 카메라 기본 틀
# 영상에 글자 출력
cap = cv2.VideoCapture(0)   # 번호 0부터 +1 웹캠 열기
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # 넓이와 높이 수동 설정
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 나눔고딕볼드 로드
font = ImageFont.truetype('./fonts/NanumGothicBold.ttf', 20)

# 무한루프 (q를 입력할때까지)
while True:
    ret, frame = cap.read() # 카메라 현재 영상 로드, frame에 저장, ret True/False
    h, _, _ = frame.shape   # width, channel은 불필요
    now = datetime.datetime.now()
    currDateTime = now.strftime('%Y-%m-%d %H:%M:%S')
    if ret != True: break   # ret이 False면 루프 탈출

    frame = Image.fromarray(frame)  # 글자 출력을 위해 변환
    draw = ImageDraw.Draw(frame)
    draw.text(xy=(10,(h - 40)), text='CCTV 녹화중 - {0}'.format(currDateTime), font=font, fill=(0,0,255))
    frame = np.array(frame) # 원상태 복귀

    cv2.imshow('RealTime CAM', frame)   # 로드한 영상을 창에 띄움
    if cv2.waitKey(1) == ord('q'): break    # q를 입력하면 루프 탈출

cap.release()   # 웹캠 해제
cv2.destroyAllWindows()