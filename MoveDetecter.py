import cv2

cap = cv2.VideoCapture(0)   # 기본 카메라

cap.set(3,300)  # 창 세팅
cap.set(4,200)

ret, prev_frame = cap.read()  # 첫 영상 읽음

while True:
    ret, frame = cap.read() # 웹캠 읽기
   
    if ret: # 정상 읽기 일때만
        f = cv2.absdiff(prev_frame, frame)  # 배경영상과 현재 프레임 영상의 차이를 구함
        f = cv2.flip(f, 1)      # 좌우 반전 (1 : 좌우, 0 : 상하)
        cv2.imshow('img', f)    # 영상을 윈도우에 출력
        prev_frame = frame
    
    k = cv2.waitKey(1)
    if k == 27: break   # ESC

cap.relase()
cv2.destroyAllWindows()