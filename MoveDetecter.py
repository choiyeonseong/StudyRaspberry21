import cv2
cap = cv2.VideoCapture(0)

cap.set(3,300)
cap.set(4,200)
prev_frame = None
ret, prev_frame=cap.read()  # 첫 영상 읽음

while True:
    ret, frame = cap.read()
    if ret: # 정상 읽기 일때만
        f = cv2.absdiff(prev_frame, frame)
        f = cv2.flip(f, 1)
        cv2.imshow('img', f)    # 영상을 윈도우에 출력
        prev_frame = frame
    k = cv2.waitKey(1)
    if k == 27: break   # ESC

cap.relase()
cv2.destroyAllWindows()