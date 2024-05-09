from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QLabel,QVBoxLayout,QWidget
import sys
from random import randint
class AnotherWindow(QWidget):
    """
        이 윈도우는 QWidget이고 만약 부모가 없다면 우리가 원하는대로 떠다니지 않는 것처럼 보인다
    """
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout
        self.label = QLabel()
        layout.addWidget(self.label)
        self.setLayout(layout)
    def updata_label(self):
        self.label.setText("Another window %d" %randint(0,100))

class TheOtherWindow(QWidget):
    """
        이 윈도우는 QWidget이고 만약 부모가 없다면 우리가 원하는대로 떠다니지 않는 것처럼 보인다
    """
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout
        self.label = QLabel()
        layout.addWidget(self.label)
        self.setLayout(layout)
    def updata_label(self):
        self.label.setText("The other window %d" %randint(0,100))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.cnt = 0
        self.w = None
        self.button = QPushButton("윈도우를 위해 눌러라")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)
    def show_new_window(self,checked):
        self.cnt+=1
        print(self.cnt)
        if self.cnt%3==0:
            self.w1.close()
            self.w2.update_label()#초기 라벨은 기본값이고 호출될때 라벨의 값을 변경함
            self.w2.show()
        else:
            self.w2.close()
            self.w1.update_label()
            self.w1.show()
app = QApplication(sys.argv)
w = MainWindow() #MainWindow 객체 생성시 생성자에서 2개의window ㄱ객체 생성
#멤버변수 cnt의 값이 3의 배수일 경우와 그렇지 않을 결우의 서로 다른 윈도우를 표시하고 다른 윈도우는 종료함
w.show()
app.exec()