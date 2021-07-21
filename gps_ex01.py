import serial   # 시리얼 통신 모듈

# def get_GPS_info(buffer):


# 초기화
tag_info = 'GNGGA, '    # 위치 NMEA, GPGGA
ser = serial.Serial('/dev/ttyS0', baudrate = 9600)  # 시리얼 객체 생성

# 무한루프
try:
    while True:
        if ser.readable():
            res = ser.readline()    # GPS 데이터 한줄읽기
            try:
                rec_data = res.decode()[:len(res)-1]
                # print(rec_data)
                tag_available = rec_data.find(tag_info)
                if(tag_available > 0):
                    buffer = rec_data.split(tag_info, 1)[1]
                    print(buffer)
            except:
                pass
except KeyboardInterrupt:
    print('GPS 종료!!')
