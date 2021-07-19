## QT5 사용자 윈도우 구성 예제
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtGui,QtWidgets,uic
from PyQt5.QtWidgets import *


# window 클래스 선언
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./ui/mainWindow01.ui', self)

        #ui에 있는 위젯하고 연결하는 시그널 처리(컨트롤 이벤트 처리)
        self.BtnStart.clicked.connect(self.BtnStart_Clicked)
        self.BtnStop.clicked.connect(self.BtnStop_Clicked)
    
    def BtnStart_Clicked(self):
        print('시작했습니다.')
        self.LblResult.setText('시작했습니다.')

    def BtnStop_Clicked(self):
        print('종료했습니다.')
        self.LblResult.setText('종료했습니다.')

app = QApplication(sys.argv)

win = MyWindow()
win.show()
app.exec_()