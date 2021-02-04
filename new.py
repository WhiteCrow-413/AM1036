from os import name, read
import sys
import hash
import crypt_1 #시저, 대칭, RSA 모듈(이름 변경 필요)
import Number
import multiprocessing as mp
import datetime
import time

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from multiprocessing import Process, Queue

#! 변수명 통일 필요

def producer(q):
    proc = mp.current_process()
    
    while True:
        now = datetime.datetime.now()
        data = str(now)
        q.put(data)
        time.sleep(1)



class Consumer(QThread):
    poped = pyqtSignal(str)

    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):
        while True:
            if not self.q.empty():
                data = q.get()
                self.poped.emit(data)



class MainWindow(QMainWindow):
    def __init__(self, q):
        super().__init__()
        
        # 윈도우 설정
        self.setGeometry(300, 300, 500, 600)  # x, y, w, h
        #self.setFixedSize(400, 400) # 크기고정
        self.setWindowTitle('HOMIN PROJECT')

        #멀티프로세싱 설정
        self.consumer = Consumer(q)
        self.consumer.poped.connect(self.Tab1)
        self.consumer.poped.connect(self.Tab2)
        #self.consumer.poped.connect(self.Tab3) -> 나중에 풀 것

        # Tab Set
        tabs = QTabWidget()
        tabs.addTab(self.Tab1(), 'NUM')
        tabs.addTab(self.Tab2(), 'HASH')
        tabs.addTab(self.Tab3(), 'CEASAR')
        tabs.addTab(self.Tab4(), 'RSA')
        #tabs.addTab(self.Tab5(), 'DEFENDER') -> 나중에 풀 것

        # QMainWindow 추가
        self.setCentralWidget(tabs)


##############################################################


    # 첫번째 탭 생성함수
    def Tab1(self):
        grid = QGridLayout()

        self.num_ck_box1 = QCheckBox('2진수', self)
        self.num_ck_box2 = QCheckBox('8진수', self)        
        self.num_ck_box3 = QCheckBox('10진수', self)
        self.num_ck_box4 = QCheckBox('16진수', self)

        self.num_ck_box1.toggle()
        self.num_ck_box2.toggle()
        self.num_ck_box3.toggle()
        self.num_ck_box4.toggle()

        self.num_ck_box1.stateChanged.connect(self.Num_Ck_Box1)
        self.num_ck_box2.stateChanged.connect(self.Num_Ck_Box2)
        self.num_ck_box3.stateChanged.connect(self.Num_Ck_Box3)
        self.num_ck_box4.stateChanged.connect(self.Num_Ck_Box4)

        
        #라인
        self.num_line1 = QLineEdit()
        self.num_line2 = QLineEdit()
        self.num_line3 = QLineEdit()
        self.num_line4 = QLineEdit()

        #입력 박스
        self.num_label_text = QLabel('INPUT DATA')
        self.num_input_box = QTextEdit(self)


        #버튼
        btn_num_incoding = QPushButton('INCODING',self)
        btn_num_reset = QPushButton('RESET', self)

        btn_num_incoding.clicked.connect(self.Num_Incoding_Btn)
        btn_num_reset.clicked.connect(self.Num_Reset_Btn)

        #콤보 박스 (입력 진수 선택)
        self.num_cb = QComboBox(self)
        self.num_cb.addItem('10진수')
        self.num_cb.addItem('2진수')
        self.num_cb.addItem('8진수')
        self.num_cb.addItem('16진수')

        self.num_cb.activated.connect(self.Num_Cb)

        #그리드
        grid.addWidget(self.num_cb, 0,0,1,7)

        grid.addWidget(self.num_ck_box1,1,0)
        grid.addWidget(self.num_line1,1,1,1,6)
        
        grid.addWidget(self.num_ck_box2,2,0)
        grid.addWidget(self.num_line2,2,1,1,6)

        grid.addWidget(self.num_ck_box3,3,0)
        grid.addWidget(self.num_line3,3,1,1,6)
        
        grid.addWidget(self.num_ck_box4,4,0)
        grid.addWidget(self.num_line4,4,1,1,6)

        grid.addWidget(self.num_label_text,5,0)
        grid.addWidget(self.num_input_box,6,0,1,7)

        grid.addWidget(btn_num_incoding,9,2)
        grid.addWidget(btn_num_reset,9,3)


        tab = QWidget()
        tab.setLayout(grid)
        return tab

    #넘버 인코딩 버튼
    def Num_Incoding_Btn(self):
        if(self.num_cb.currentText() == '10진수'):
            self.num_line1.setText(Number.Bin_Number_DEC(self.num_input_box.toPlainText()))
            self.num_line2.setText(Number.Oct_Number_DEC(self.num_input_box.toPlainText()))
            self.num_line3.setText("")
            self.num_line4.setText(Number.Hex_Number_DEC(self.num_input_box.toPlainText()))

        elif(self.num_cb.currentText() == '2진수'):
            self.num_line1.setText("")
            self.num_line2.setText(Number.Oct_Number_BIN(self.num_input_box.toPlainText()))
            self.num_line3.setText(Number.Dec_Number_BIN(self.num_input_box.toPlainText()))
            self.num_line4.setText(Number.Hex_Number_BIN(self.num_input_box.toPlainText()))
        
        elif(self.num_cb.currentText() == '8진수'):
            self.num_line1.setText(Number.Bin_Number_OCT(self.num_input_box.toPlainText()))
            self.num_line2.setText("")
            self.num_line3.setText(Number.Dec_Number_OCT(self.num_input_box.toPlainText()))
            self.num_line4.setText(Number.Hex_Number_OCT(self.num_input_box.toPlainText()))
        
        elif(self.num_cb.currentText() == '16진수'):
            self.num_line1.setText(Number.Bin_Number_HEX(self.num_input_box.toPlainText()))
            self.num_line2.setText(Number.Oct_Number_HEX(self.num_input_box.toPlainText()))
            self.num_line3.setText(Number.Dec_Number_HEX(self.num_input_box.toPlainText()))
            self.num_line4.setText("")


    #넘버 리셋 버튼 (체크 박스 모두 선택으로 변경 및 값 초기화)
    def Num_Reset_Btn(self):
        self.num_line1.setText("")
        self.num_line2.setText("")
        self.num_line3.setText("")
        self.num_line4.setText("")
        self.num_input_box.setText("")
        self.num_ck_box1.setChecked(True)
        self.num_ck_box2.setChecked(True)
        self.num_ck_box3.setChecked(True)
        self.num_ck_box4.setChecked(True)
        self.num_cb.setCurrentIndex(0)

    #콤보박스 이벤트
    def Num_Cb(self):
        self.num_input_box.setText("")

    #체크박스 체크 여부에 따른 라인처리
    def Num_Ck_Box1(self, state):
        if state == Qt.Checked:
            self.num_line1.setEchoMode(QLineEdit.Normal)
        else:
            self.num_line1.setEchoMode(QLineEdit.NoEcho)

    def Num_Ck_Box2(self, state):
        if state == Qt.Checked:
            self.num_line2.setEchoMode(QLineEdit.Normal)
        else:
            self.num_line2.setEchoMode(QLineEdit.NoEcho)

    def Num_Ck_Box3(self, state):
        if state == Qt.Checked:
            self.num_line3.setEchoMode(QLineEdit.Normal)
        else:
            self.num_line3.setEchoMode(QLineEdit.NoEcho)

    def Num_Ck_Box4(self, state):
        if state == Qt.Checked:
            self.num_line4.setEchoMode(QLineEdit.Normal)
        else:
            self.num_line4.setEchoMode(QLineEdit.NoEcho)


###################################################################


    #HASH       
    def Tab2(self):
        grid = QGridLayout()

        #라벨
        self.hash_label = QLabel('Input Data')
        
        #체크 박스
        self.hash_ck_box1 = QCheckBox('BASE64', self)
        self.hash_ck_box2 = QCheckBox('URL-K', self)
        self.hash_ck_box3 = QCheckBox('URL-E', self)
        self.hash_ck_box4 = QCheckBox('ASCII', self)
        self.hash_ck_box5 = QCheckBox('MD5', self)
        self.hash_ck_box6 = QCheckBox('SHA-1', self)
        self.hash_ck_box7 = QCheckBox('SHA-256', self)
        self.hash_ck_box8 = QCheckBox('SHA-512', self)

        self.hash_ck_box1.toggle()
        self.hash_ck_box2.toggle()
        self.hash_ck_box3.toggle()
        self.hash_ck_box4.toggle()
        self.hash_ck_box5.toggle()
        self.hash_ck_box6.toggle()
        self.hash_ck_box7.toggle()
        self.hash_ck_box8.toggle()

        self.hash_ck_box1.stateChanged.connect(self.Hash_Ck_Box1)
        self.hash_ck_box2.stateChanged.connect(self.Hash_Ck_Box2)
        self.hash_ck_box3.stateChanged.connect(self.Hash_Ck_Box3)
        self.hash_ck_box4.stateChanged.connect(self.Hash_Ck_Box4)
        self.hash_ck_box5.stateChanged.connect(self.Hash_Ck_Box5)
        self.hash_ck_box6.stateChanged.connect(self.Hash_Ck_Box6)
        self.hash_ck_box7.stateChanged.connect(self.Hash_Ck_Box7)
        self.hash_ck_box8.stateChanged.connect(self.Hash_Ck_Box8)


        #콤보박스
        self.hash_cb = QComboBox(self)
        self.hash_cb.addItem('text')
        self.hash_cb.addItem('file')

        self.hash_cb.activated.connect(self.Hash_Cb)


        #텍스트 라인
        self.hash_line1 = QLineEdit()
        self.hash_line2 = QLineEdit()
        self.hash_line3 = QLineEdit()
        self.hash_line4 = QLineEdit()
        self.hash_line5 = QLineEdit()
        self.hash_line6 = QLineEdit()
        self.hash_line7 = QLineEdit()
        self.hash_line8 = QLineEdit()

        #INPUT TEXT BOX
        self.hash_input_box = QTextEdit()

        #버튼
        btn_hash_encoding = QPushButton('encoding',self)
        btn_hash_decoding = QPushButton('decoding',self)
        btn_hash_reset = QPushButton('reset', self)
        btn_hash_file = QPushButton('file', self)
        
        btn_hash_encoding.clicked.connect(self.Hash_Encoding_Btn)
        btn_hash_decoding.clicked.connect(self.Hash_Decoding_Btn)
        btn_hash_reset.clicked.connect(self.Hash_Reset_Btn)
        btn_hash_file.clicked.connect(self.Hash_File_Btn)

        #그리드
        grid.addWidget(self.hash_ck_box1,0,0)
        grid.addWidget(self.hash_line1,0,1,1,6)

        grid.addWidget(self.hash_ck_box2,1,0)
        grid.addWidget(self.hash_line2,1,1,1,6)

        grid.addWidget(self.hash_ck_box3,2,0)
        grid.addWidget(self.hash_line3,2,1,1,6)

        grid.addWidget(self.hash_ck_box4,3,0)
        grid.addWidget(self.hash_line4,3,1,1,6)

        grid.addWidget(self.hash_ck_box5,4,0)
        grid.addWidget(self.hash_line5,4,1,1,6)
        
        grid.addWidget(self.hash_ck_box6,5,0)
        grid.addWidget(self.hash_line6,5,1,1,6)

        grid.addWidget(self.hash_ck_box7,6,0)
        grid.addWidget(self.hash_line7,6,1,1,6)

        grid.addWidget(self.hash_ck_box8,7,0)
        grid.addWidget(self.hash_line8,7,1,1,6)

        grid.addWidget(self.hash_label,8,0)
        grid.addWidget(self.hash_input_box,9,0,1,7)

        grid.addWidget(self.hash_cb,10,0)
        grid.addWidget(btn_hash_encoding,10,1)
        grid.addWidget(btn_hash_decoding,10,2)
        grid.addWidget(btn_hash_reset,10,3)
        grid.addWidget(btn_hash_file, 10, 4)
        

        # 위젯에 레이아웃 추가하기
        tab = QWidget()
        tab.setLayout(grid)
        return tab

    #인코딩 버튼 이벤트
    def Hash_Encoding_Btn(self):
        if(self.hash_cb.currentText() == 'text'):
            self.hash_line1.setText(hash.Base64_Encode(self.hash_input_box.toPlainText()))
            self.hash_line2.setText(hash.Url_Encode_Hangle(self.hash_input_box.toPlainText()))
            self.hash_line3.setText(hash.Url_Encode_English(self.hash_input_box.toPlainText()))
            self.hash_line4.setText(hash.Ascii_Encode(self.hash_input_box.toPlainText()))
            self.hash_line5.setText(hash.MD5_Encode(self.hash_input_box.toPlainText()))
            self.hash_line6.setText(hash.SHA1_Encode(self.hash_input_box.toPlainText()))
            self.hash_line7.setText(hash.SHA256_Encode(self.hash_input_box.toPlainText()))
            self.hash_line8.setText(hash.SHA512_Encode(self.hash_input_box.toPlainText()))
        else:
            self.hash_line1.setText("")
            self.hash_line2.setText("")
            self.hash_line3.setText("")
            self.hash_line4.setText("")
            self.hash_line5.setText(hash.MD5_Encode_F(self.hash_input_box.toPlainText()))
            self.hash_line6.setText(hash.SHA1_Encode_F(self.hash_input_box.toPlainText()))
            self.hash_line7.setText(hash.SHA256_Encode_F(self.hash_input_box.toPlainText()))
            self.hash_line8.setText(hash.SHA512_Encode_F(self.hash_input_box.toPlainText()))

    #디코딩 버튼 이벤트
    def Hash_Decoding_Btn(self):
        if(self.hash_cb.currentText() == 'text'):
            self.hash_line1.setText(hash.Base64_Decode(self.hash_input_box.toPlainText()))
            self.hash_line2.setText(hash.Url_Decode_Hangle(self.hash_input_box.toPlainText()))
            self.hash_line3.setText(hash.Url_Decode_English(self.hash_input_box.toPlainText()))            
            self.hash_line4.setText(hash.Ascii_Decode(self.hash_input_box.toPlainText()))
            self.hash_line5.setText("")
            self.hash_line6.setText("")
            self.hash_line7.setText("")
            self.hash_line8.setText("")
        else:
            self.hash_line1.setText("")
            self.hash_line2.setText("")
            self.hash_line3.setText("")
            self.hash_line4.setText("")
            self.hash_line5.setText("")
            self.hash_line6.setText("")
            self.hash_line7.setText("")
            self.hash_line8.setText("")


    #리셋 버튼 이벤트
    def Hash_Reset_Btn(self):
        self.hash_line1.setText("")
        self.hash_line2.setText("")
        self.hash_line3.setText("")
        self.hash_line4.setText("")
        self.hash_line5.setText("")
        self.hash_line6.setText("")
        self.hash_line7.setText("")
        self.hash_line8.setText("")
        self.hash_input_box.setText("")
        self.hash_ck_box1.setChecked(True)
        self.hash_ck_box2.setChecked(True)
        self.hash_ck_box3.setChecked(True)
        self.hash_ck_box4.setChecked(True)
        self.hash_ck_box5.setChecked(True)
        self.hash_ck_box6.setChecked(True)
        self.hash_ck_box7.setChecked(True)
        self.hash_ck_box8.setChecked(True)
        self.hash_cb.setCurrentIndex(0)
    
    #파일 불러오기 버튼
    def Hash_File_Btn(self):
        if(self.hash_cb.currentText() == 'file'):
            path = QFileDialog.getOpenFileName(self)

            self.hash_input_box.setText(path[0])
        else:
            msg = "'text' -> 'file"
            title = "error"
            msg_box = QMessageBox(self)
            msg_box.question(self, title, msg, QMessageBox.Ok)

    #콤보박스 변경 이벤트
    def Hash_Cb(self):
        self.hash_input_box.setText("")

        
    #체크박스 체크 여부에 따른 라인처리
    def Hash_Ck_Box1(self, state):
        if state == Qt.Checked:
            self.hash_line1.setEchoMode(QLineEdit.Normal)
        else:
            self.hash_line1.setEchoMode(QLineEdit.NoEcho)

    def Hash_Ck_Box2(self, state):
        if state == Qt.Checked:
            self.hash_line2.setEchoMode(QLineEdit.Normal)
        else:
            self.hash_line2.setEchoMode(QLineEdit.NoEcho)

    def Hash_Ck_Box3(self, state):
        if state == Qt.Checked:
            self.hash_line3.setEchoMode(QLineEdit.Normal)
        else:
            self.hash_line3.setEchoMode(QLineEdit.NoEcho)

    def Hash_Ck_Box4(self, state):
        if state == Qt.Checked:
            self.hash_line4.setEchoMode(QLineEdit.Normal)
        else:
            self.hash_line4.setEchoMode(QLineEdit.NoEcho)
        
    def Hash_Ck_Box5(self, state):
        if state == Qt.Checked:
            self.hash_line5.setEchoMode(QLineEdit.Normal)
        else:
            self.hash_line5.setEchoMode(QLineEdit.NoEcho)

    def Hash_Ck_Box6(self, state):
        if state == Qt.Checked:
            self.hash_line6.setEchoMode(QLineEdit.Normal)
        else:
            self.hash_line6.setEchoMode(QLineEdit.NoEcho)

    def Hash_Ck_Box7(self, state):
        if state == Qt.Checked:
            self.hash_line7.setEchoMode(QLineEdit.Normal)
        else:
            self.hash_line7.setEchoMode(QLineEdit.NoEcho)

    def Hash_Ck_Box8(self, state):
        if state == Qt.Checked:
            self.hash_line8.setEchoMode(QLineEdit.Normal)
        else:
            self.hash_line8.setEchoMode(QLineEdit.NoEcho)


##################################################################


    def Tab3(self):
        grid = QGridLayout()
        
        self.dump_label = QLabel(self)
        self.ceasar_text_box = QTextEdit()
        self.ceasar_input_line = QLineEdit()

        btn_ceasar_encoding = QPushButton('encoding', self)

        btn_ceasar_encoding.clicked.connect(self.Ceasar_encode)

        self.spinbox = QSpinBox()
        self.spinbox.setRange(-25,25)
        self.spinbox.setSingleStep(1)

        grid.addWidget(self.ceasar_text_box, 0,0,1,0)
        grid.addWidget(self.spinbox, 1, 0, 1,0)
        grid.addWidget(self.ceasar_input_line,2,0)
        grid.addWidget(btn_ceasar_encoding,2,1)

        

        tab = QWidget()
        tab.setLayout(grid)
        return tab

    #시저 암호 인코딩 버튼 이벤트
    def Ceasar_encode(self):
        self.ceasar_text_box.setText(crypt_1.Ceasar_Crypt(self.ceasar_input_line.text(),self.spinbox.value()))


###################################################################

    #호환 사이트 : https://8gwifi.org/rsafunctions.jsp
    #Tab4 RSA
    def Tab4(self):
        grid = QGridLayout()

        #라벨
        self.rsa_label1 = QLabel('data', self)
        self.rsa_label2 = QLabel('private key', self)
        self.rsa_label3 = QLabel('public key',self)
        self.rsa_label5 = QLabel('input data',self)
        self.rsa_label6 = QLabel('key size :', self)
        
        #텍스트박스
        self.rsa_textbox_data = QTextEdit()
        self.rsa_textbox_prikey = QTextEdit()
        self.rsa_textbox_pubkey = QTextEdit()
        self.rsa_textbox_path = QTextEdit()
        self.rsa_textbox_inputdata = QTextEdit()

        #푸쉬버튼
        btn_rsa_readme = QPushButton('readme', self)
        btn_rsa_createkey = QPushButton('create key', self)
        btn_rsa_encoding = QPushButton('encoding', self)
        btn_rsa_decoding = QPushButton('decoding', self)
        btn_rsa_path = QPushButton('path',self)

        btn_rsa_readme.clicked.connect(self.RSA_readme)
        btn_rsa_createkey.clicked.connect(self.RSA_createkey)
        btn_rsa_encoding.clicked.connect(self.RSA_encode)
        btn_rsa_decoding.clicked.connect(self.RSA_decode)
        btn_rsa_path.clicked.connect(self.RSA_Path_Btn)

        #콤보박스
        self.rsa_cb1 = QComboBox(self)
        self.rsa_cb1.addItem('RSA PKCS#1 v1.5')
        self.rsa_cb1.addItem('RSA PKCS#1 OAEP')

        self.rsa_cb2 = QComboBox(self)
        self.rsa_cb2.addItem('1024')
        self.rsa_cb2.addItem('512')
        self.rsa_cb2.addItem('2048')
        self.rsa_cb2.addItem('4096')

        self.rsa_cb1.activated.connect(self.RSA_Cb1)
        self.rsa_cb2.activated.connect(self.RSA_Cb2)

        
        #그리드
        grid.addWidget(self.rsa_cb1,0,0,1,6)
        grid.addWidget(self.rsa_label6,0,6,1,1)
        grid.addWidget(self.rsa_cb2,0,7,1,1)

        grid.addWidget(self.rsa_label1,1,0,1,8)
        grid.addWidget(self.rsa_textbox_data,2,0,1,8)

        grid.addWidget(self.rsa_label2,3,0,1,4)
        grid.addWidget(self.rsa_label3,3,4,1,4)
        grid.addWidget(self.rsa_textbox_prikey,4,0,1,4)
        grid.addWidget(self.rsa_textbox_pubkey,4,4,1,4)

        grid.addWidget(btn_rsa_path,5,0,1,4)
        grid.addWidget(self.rsa_label5,5,4,1,4)
        grid.addWidget(self.rsa_textbox_path,6,0,1,4)
        grid.addWidget(self.rsa_textbox_inputdata,6,4,1,4)

        grid.addWidget(btn_rsa_readme,7,0,1,2)
        grid.addWidget(btn_rsa_createkey,7,2,1,2)
        grid.addWidget(btn_rsa_encoding,7,4,1,2)
        grid.addWidget(btn_rsa_decoding,7,6,1,2)


        tab = QWidget()
        tab.setLayout(grid)
        return tab

    # RSA 인코딩 버튼 이벤트 
    def RSA_encode(self):
        if(self.rsa_cb1.currentText() == 'RSA PKCS#1 v1.5'):
            self.rsa_textbox_data.setText(crypt_1.RSA_PKCS1_v1_5_Encode(self.rsa_textbox_path.toPlainText(),self.rsa_textbox_inputdata.toPlainText()))
        
        elif(self.rsa_cb1.currentText() == 'RSA PKCS#1 OAEP'):
            self.rsa_textbox_data.setText(crypt_1.RSA_OAEP_Encode(self.rsa_textbox_path.toPlainText(),self.rsa_textbox_inputdata.toPlainText()))

    # RSA 디코딩 버튼 이벤트
    def RSA_decode(self):
        if(self.rsa_cb1.currentText() == 'RSA PKCS#1 v1.5'):
            self.rsa_textbox_data.setText(crypt_1.RSA_PKCS1_v1_5_Decode(self.rsa_textbox_path.toPlainText()))

        elif(self.rsa_cb1.currentText() == 'RSA PKCS#1 OAEP'):
            self.rsa_textbox_data.setText(crypt_1.RSA_OAEP_Decode(self.rsa_textbox_path.toPlainText()))

    #!RSA 키생성 버튼 이벤트 (메세지박스 크기 조절 필요! : 텍스트나 라벨의 크기를 조정한 후 메시지박스에 넣어야 함)
    def RSA_createkey(self):
        crypt_1.Create_Key(self.rsa_textbox_path.toPlainText(),self.rsa_cb2.currentText())
        self.rsa_textbox_prikey.setText(crypt_1.Read_Pri_Key(self.rsa_textbox_path.toPlainText()))
        self.rsa_textbox_pubkey.setText(crypt_1.Read_Pub_Key(self.rsa_textbox_path.toPlainText()))
        QMessageBox.about(self, "createkey", "created!!!")
        
        

    #!RSA readme 버튼 이벤트 (내용 변경 필요)
    def RSA_readme(self):
        msg = "주의사항: 뭐 써야하지???"
        title = "readme"
        msg_box = QMessageBox(self)
        msg_box.question(self, title, msg, QMessageBox.Ok)

    # 경로 이벤트 버튼
    def RSA_Path_Btn(self):
        path = QFileDialog.getExistingDirectory(self)
        self.rsa_textbox_path.setText(path+'\\')

    #콤보 박스 이벤트
    def RSA_Cb1(self):
        self.rsa_textbox_data.setText("")
        self.rsa_textbox_inputdata.setText("")
        self.rsa_textbox_path.setText("")

    def RSA_Cb2(self):
        self.rsa_textbox_data.setText("")
        self.rsa_textbox_inputdata.setText("")
        self.rsa_textbox_path.setText("")
        self.rsa_textbox_prikey.setText("")
        self.rsa_textbox_pubkey.setText("")


###################################################################


    #! 영어 100%가능, 한글 불가능(UTF-8로 디코딩해줘야됨)
    '''def Tab3(self):
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
        self.text_box3.setText(Exception.list_path())'''





if __name__ == '__main__':
    q = Queue()

    p = Process(name="producer", target=producer, args=(q, ), daemon=True)
    p.start()

    app = QApplication(sys.argv)
    mainWindow = MainWindow(q)
    mainWindow.show()
    sys.exit(app.exec_())