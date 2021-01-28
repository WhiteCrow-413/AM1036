import sys
import hash
import Exception

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

#! 변수명 통일 필요

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 윈도우 설정
        self.setGeometry(300, 300, 500, 600)  # x, y, w, h
        #self.setFixedSize(400, 400) # 크기고정
        self.setWindowTitle('HOMIN PROJECT')

        # Tab Set
        tabs = QTabWidget()
        tabs.addTab(self.Tab1(), 'NUM')
        tabs.addTab(self.Tab2(), 'HASH')
        tabs.addTab(self.Tab3(), 'DEFENDER')

        # QMainWindow 추가
        self.setCentralWidget(tabs)

    # 첫번째 탭 생성함수
    def Tab1(self):
        grid = QGridLayout()

        # 변수 선언 부분
        self.ck_box1 = QCheckBox('2진수', self)
        self.ck_box2 = QCheckBox('8진수', self)
        self.ck_box3 = QCheckBox('10진수', self)
        self.ck_box4 = QCheckBox('16진수', self)
        self.ck_box5 = QCheckBox('BASE64', self)
        self.ck_box6 = QCheckBox('URL(E)', self)
        self.ck_box7 = QCheckBox('URL(H)', self)
        self.ck_box8 = QCheckBox('ASCII', self)

        self.line1 = QLineEdit()
        self.line2 = QLineEdit()
        self.line3 = QLineEdit()
        self.line4 = QLineEdit()
        self.line5 = QLineEdit()
        self.line6 = QLineEdit()
        self.line7 = QLineEdit()
        self.line8 = QLineEdit()

        self.label_text = QLabel('INPUT DATA')
        self.input_box = QTextEdit(self)

        btn_incoding = QPushButton('INCODING', self)
        btn_decoding = QPushButton('DECODING', self)
        btn_reset = QPushButton('RESET', self)
        # 버튼 클릭 이벤트
        btn_incoding.clicked.connect(self.Incoding_Btn)
        btn_decoding.clicked.connect(self.Decoding_Btn)
        btn_reset.clicked.connect(self.Reset_Btn)

        self.ck_box1.toggle()
        self.ck_box2.toggle()
        self.ck_box3.toggle()
        self.ck_box4.toggle()
        self.ck_box5.toggle()
        self.ck_box6.toggle()
        self.ck_box7.toggle()
        self.ck_box8.toggle()

        self.ck_box1.stateChanged.connect(self.changeBox1)
        self.ck_box2.stateChanged.connect(self.changeBox2)
        self.ck_box3.stateChanged.connect(self.changeBox3)
        self.ck_box4.stateChanged.connect(self.changeBox4)
        self.ck_box5.stateChanged.connect(self.changeBox5)
        self.ck_box6.stateChanged.connect(self.changeBox6)
        self.ck_box7.stateChanged.connect(self.changeBox7)
        self.ck_box8.stateChanged.connect(self.changeBox8)

        # 실제 그리드 작업 부분
        grid.addWidget(self.ck_box1, 0,0)
        grid.addWidget(self.ck_box2, 1,0)
        grid.addWidget(self.ck_box3, 2,0)
        grid.addWidget(self.ck_box4, 3,0)
        grid.addWidget(self.ck_box5, 4,0)
        grid.addWidget(self.ck_box6, 5,0)
        grid.addWidget(self.ck_box7, 6,0)
        grid.addWidget(self.ck_box8, 7,0)

        grid.addWidget(self.line1, 0, 1, 1, 6)
        grid.addWidget(self.line2, 1, 1, 1, 6)
        grid.addWidget(self.line3, 2, 1, 1, 6)
        grid.addWidget(self.line4, 3, 1, 1, 6)
        grid.addWidget(self.line5, 4, 1, 1, 6)
        grid.addWidget(self.line6, 5, 1, 1, 6)
        grid.addWidget(self.line7, 6, 1, 1, 6)
        grid.addWidget(self.line8, 7, 1, 1, 6)

        grid.addWidget(self.label_text, 8, 0, 1, 0)
        grid.addWidget(self.input_box, 9, 0, 1, 7) # !왜 7인지 모르겠음

        grid.addWidget(btn_incoding, 10, 1)
        grid.addWidget(btn_decoding, 10, 2)
        grid.addWidget(btn_reset,10, 3)

        # 위젯에 레이아웃 추가하기
        tab = QWidget()
        tab.setLayout(grid)
        return tab
    
    def Incoding_Btn(self):
        hash.Bin_Number(self.input_box.toPlainText())
        self.line1.setText(hash.Bin_Number(self.input_box.toPlainText()))
        hash.Oct_Number(self.input_box.toPlainText())
        self.line2.setText(hash.Oct_Number(self.input_box.toPlainText()))
        # 3번 자리
        hash.Hex_Number(self.input_box.toPlainText())
        self.line4.setText(hash.Hex_Number(self.input_box.toPlainText()))
        hash.Base64_Encode(self.input_box.toPlainText())
        self.line5.setText(hash.Base64_Encode(self.input_box.toPlainText()))
        hash.Url_Encode_English(self.input_box.toPlainText())
        self.line6.setText(hash.Url_Encode_English(self.input_box.toPlainText()))
        hash.Url_Encode_Hangle(self.input_box.toPlainText())
        self.line7.setText(hash.Url_Encode_Hangle(self.input_box.toPlainText()))
        hash.Ascii_Encode(self.input_box.toPlainText())
        self.line8.setText(hash.Ascii_Encode(self.input_box.toPlainText()))
        
    def Decoding_Btn(self):
        hash.Base64_Decode(self.input_box.toPlainText())
        self.line5.setText(hash.Base64_Decode(self.input_box.toPlainText()))
        hash.Url_Decode_English(self.input_box.toPlainText())
        self.line6.setText(hash.Url_Decode_English(self.input_box.toPlainText()))
        hash.Url_Decode_Hangle(self.input_box.toPlainText())
        self.line7.setText(hash.Url_Decode_Hangle(self.input_box.toPlainText()))
        hash.Ascii_Decode(self.input_box.toPlainText())
        self.line8.setText(hash.Ascii_Decode(self.input_box.toPlainText()))

    #! 누를때 교차현상 수정(누르면 다 초기화되고 다시 체크박스 on되도록)
    def Reset_Btn(self):
        self.line1.setText("")
        self.line2.setText("")
        self.line3.setText("")
        self.line4.setText("")
        self.line5.setText("")
        self.line6.setText("")
        self.line7.setText("")
        self.line8.setText("")
        self.input_box.setText("")

    def changeBox1(self, state):
        if state == Qt.Checked:
            self.line1.setEchoMode(QLineEdit.Normal)
        else:
            self.line1.setEchoMode(QLineEdit.NoEcho)

    def changeBox2(self, state):
        if state == Qt.Checked:
            self.line2.setEchoMode(QLineEdit.Normal)
        else:
            self.line2.setEchoMode(QLineEdit.NoEcho)

    def changeBox3(self, state):
        if state == Qt.Checked:
            self.line3.setEchoMode(QLineEdit.Normal)
        else:
            self.line3.setEchoMode(QLineEdit.NoEcho)

    def changeBox4(self, state):
        if state == Qt.Checked:
            self.line4.setEchoMode(QLineEdit.Normal)
        else:
            self.line4.setEchoMode(QLineEdit.NoEcho)

    def changeBox5(self, state):
        if state == Qt.Checked:
            self.line5.setEchoMode(QLineEdit.Normal)
        else:
            self.line5.setEchoMode(QLineEdit.NoEcho)

    def changeBox6(self, state):
        if state == Qt.Checked:
            self.line6.setEchoMode(QLineEdit.Normal)
        else:
            self.line6.setEchoMode(QLineEdit.NoEcho)

    def changeBox7(self, state):
        if state == Qt.Checked:
            self.line7.setEchoMode(QLineEdit.Normal)
        else:
            self.line7.setEchoMode(QLineEdit.NoEcho)

    def changeBox8(self, state):
        if state == Qt.Checked:
            self.line8.setEchoMode(QLineEdit.Normal)
        else:
            self.line8.setEchoMode(QLineEdit.NoEcho)

    def Tab2(self):
        # 버튼 객체 만들기
        check1 = QCheckBox('체크버튼1', self)
        check2 = QCheckBox('체크버튼2', self)
        check3 = QCheckBox('체트버튼3', self)

        # 레이아웃 만들기
        vbox = QVBoxLayout()
        vbox.addWidget(check1)
        vbox.addWidget(check2)
        vbox.addWidget(check3)

        # 위젯에 레이아웃 추가하기
        tab = QWidget()
        tab.setLayout(vbox)
        return tab

    #! 영어 100%가능, 한글 불가능(UTF-8로 디코딩해줘야됨)
    def Tab3(self):
        grid = QGridLayout()

        # 변수 선언 부분
        self.label1 = QLabel('Extension', self)
        self.label2 = QLabel('Process', self)
        self.label3 = QLabel('Path', self)

        self.text_box1 = QTextEdit()
        self.text_box2 = QTextEdit()
        self.text_box3 = QTextEdit()
        self.ex_input_box = QTextEdit()

        btn_add_extension = QPushButton('+', self)
        btn_sub_extension = QPushButton('-', self)
        btn_add_process = QPushButton('+', self)
        btn_sub_process = QPushButton('-', self)
        btn_add_path = QPushButton('+', self)
        btn_sub_path = QPushButton('-', self)

        self.label1.setAlignment(Qt.AlignCenter)
        self.label2.setAlignment(Qt.AlignCenter)
        self.label3.setAlignment(Qt.AlignCenter)

        btn_add_extension.clicked.connect(self.btn_add1)
        btn_add_process.clicked.connect(self.btn_add2)
        btn_add_path.clicked.connect(self.btn_add3)
        btn_sub_extension.clicked.connect(self.btn_sub1)
        btn_sub_process.clicked.connect(self.btn_sub2)
        btn_sub_process.clicked.connect(self.btn_sub3)

        # 실제 그리드 작업 부분
        grid.addWidget(self.label1, 0, 0, 1, 2)
        grid.addWidget(self.label2, 0, 2, 1, 2)
        grid.addWidget(self.label3, 0, 4, 1, 2)

        grid.addWidget(self.text_box1, 1, 0, 1, 2)
        grid.addWidget(self.text_box2, 1, 2, 1, 2)
        grid.addWidget(self.text_box3, 1, 4, 1, 2)

        grid.addWidget(btn_add_extension, 2, 0)
        grid.addWidget(btn_sub_extension, 2, 1)
        grid.addWidget(btn_add_process, 2, 2)
        grid.addWidget(btn_sub_process, 2, 3)
        grid.addWidget(btn_add_path, 2, 4)
        grid.addWidget(btn_sub_path, 2, 5)

        grid.addWidget(self.ex_input_box, 3, 0, 1, 6)

        # 시작할 때 리스트업
        self.text_box1.setText(Exception.list_extension())
        self.text_box2.setText(Exception.list_process())
        self.text_box3.setText(Exception.list_path())

        # 위젯에 레이아웃 추가하기
        tab = QWidget()
        tab.setLayout(grid)
        return tab

    #! QTextBrowser으로 깔끔한 리스트 업 가능 + 추가로 옆에 '-'버튼을 만들어서 삭제하면 더 깔끔할 듯
    def btn_add1(self):
        Exception.AddExtension(self.ex_input_box.toPlainText())
        self.text_box1.setText(Exception.list_extension())

    def btn_add2(self):
        Exception.AddProcess(self.ex_input_box.toPlainText())
        self.text_box2.setText(Exception.list_process())

    def btn_add3(self):
        Exception.AddPath(self.ex_input_box.toPlainText())
        self.text_box3.setText(Exception.list_path())

    def btn_sub1(self):
        Exception.SubExtension(self.ex_input_box.toPlainText())
        self.text_box1.setText(Exception.list_extension())

    def btn_sub2(self):
        Exception.SubProcess(self.ex_input_box.toPlainText())
        self.text_box2.setText(Exception.list_process())

    #! 작동 안됨 왜지?
    def btn_sub3(self):
        Exception.SubPath(self.ex_input_box.toPlainText())
        self.text_box3.setText(Exception.list_path())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())