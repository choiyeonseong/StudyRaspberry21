import cv2

# 기본 opencv 소스 - 비디오
cam = cv2.VideoCapture(0)   #  기본 카메라
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # 창 넓이
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # 창 높이

fourcc = cv2.VideoWriter_fourcc(*'XVID')    # XVID 비디오 코덱
is_record = False   # 녹화상태

while True:
    ret, frame = cam.read() # 웹캠 읽기

    if ret:
        cv2.imshow('Original Video', frame) # 카메라 영상 창에 띄움

        key = cv2.waitKey(1)
        if key == ord('q'): # q를 입력받으면
            break
        elif key == ord('c'): # c를 입력받으면
            cv2.imwrite('./capture/captured.jpg', frame)
            print('이미지 캡쳐 완료')
        elif key == ord('r') and is_record == False: # r을 입력하면 최초 레코딩 시작
            is_record = True
            video = cv2.VideoWriter('./capture/record.avi', fourcc, 20, (frame.shape[1], frame.shape[0]))
            print('녹화시작')
        elif key == ord('r') and is_record == True: # 녹화중
            is_record = False
            video.release()
            print('녹화 끝')

        if is_record == True:   # 현재화면 녹화
            video.write(frame)

cam.release()
cv2.destroyAllWindows()
