# 파일 입출력

try:
    f = open('./data/readme.txt', mode='r', encoding='utf-8')   # 텍스트 파일 오픈
    f2 = open('./data/writeme.txt', mode='w', encoding='utf-8') # 작성 파일 오픈

    line = f.read() # readline()
    while line:
        print(line)
        f2.write(line)
        line = f.read()

    f2. write('추가 내용입니다.')
    f.close()   # 파일 닫기
    f2.close()
    print('파일 작성 완료!')
except Exception as e:  # 최상위 예외
    print('예외발생 : {0}'.format(e)) 