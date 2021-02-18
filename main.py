import sys
import AM1036_Number
import AM1036_ASCII
import AM1036_Hash
import AM1036_Cersar
import AM1036_RSA
import AM1036_Exception

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Window Set
        self.setGeometry(300, 300, 500, 600)  # x, y, w, h
        self.setWindowTitle('AM 10:36')
        self.statusBar().showMessage('Copyright (C) 2021. integrity, PTTC All Rights Reserved')

        # Tab Set
        tabs = QTabWidget()
        tabs.addTab(self.Tab1(), 'NUM')
        tabs.addTab(self.Tab2(), 'ASCII')
        tabs.addTab(self.Tab3(), 'HASH')
        tabs.addTab(self.Tab4(), 'CERSAR')
        tabs.addTab(self.Tab5(), 'RSA')
        tabs.addTab(self.Tab6(), 'DEFENDER')

        # QMainWindow
        self.setCentralWidget(tabs)

######################################################################################################
    def Tab1(self):
        grid = QGridLayout()

        self.NUM_ckbox1 = QCheckBox('2진수', self)
        self.NUM_ckbox2 = QCheckBox('8진수', self)        
        self.NUM_ckbox3 = QCheckBox('10진수', self)
        self.NUM_ckbox4 = QCheckBox('16진수', self)
        self.NUM_ckbox1.toggle()
        self.NUM_ckbox2.toggle()
        self.NUM_ckbox3.toggle()
        self.NUM_ckbox4.toggle()
        self.NUM_ckbox1.stateChanged.connect(self.Num_CkBox1)
        self.NUM_ckbox2.stateChanged.connect(self.Num_CkBox2)
        self.NUM_ckbox3.stateChanged.connect(self.Num_CkBox3)
        self.NUM_ckbox4.stateChanged.connect(self.Num_CkBox4)

        self.NUM_line1 = QLineEdit()
        self.NUM_line2 = QLineEdit()
        self.NUM_line3 = QLineEdit()
        self.NUM_line4 = QLineEdit()

        self.NUM_labeltext = QLabel('INPUT DATA')
        self.NUM_inputbox = QTextEdit(self)

        NUM_btn_encoding = QPushButton('ENCODING',self)
        NUM_btn_reset = QPushButton('RESET', self)

        NUM_btn_encoding.clicked.connect(self.Num_Encoding_Btn)
        NUM_btn_reset.clicked.connect(self.Num_Reset_Btn)

        self.NUM_cb = QComboBox(self)
        self.NUM_cb.addItem('10진수')
        self.NUM_cb.addItem('2진수')
        self.NUM_cb.addItem('8진수')
        self.NUM_cb.addItem('16진수')
        self.NUM_cb.activated.connect(self.Num_Cb)

        # Grid Set
        grid.addWidget(self.NUM_ckbox1,0,0)
        grid.addWidget(self.NUM_ckbox2,1,0)
        grid.addWidget(self.NUM_ckbox3,2,0)
        grid.addWidget(self.NUM_ckbox4,3,0)
        grid.addWidget(self.NUM_cb, 5,0,1,6)
        grid.addWidget(self.NUM_labeltext,4,0)
        grid.addWidget(self.NUM_line1,0,1,1,5)
        grid.addWidget(self.NUM_line2,1,1,1,5)
        grid.addWidget(self.NUM_line3,2,1,1,5)
        grid.addWidget(self.NUM_line4,3,1,1,5)
        grid.addWidget(self.NUM_inputbox,6,0,1,6)
        grid.addWidget(NUM_btn_encoding,7,2)
        grid.addWidget(NUM_btn_reset,7,3)

        tab = QWidget()
        tab.setLayout(grid)
        return tab

    def Num_Encoding_Btn(self):
        if(self.NUM_cb.currentText() == '10진수'):
            self.NUM_line1.setText(AM1036_Number.Bin_Number_DEC(self.NUM_inputbox.toPlainText()))
            self.NUM_line2.setText(AM1036_Number.Oct_Number_DEC(self.NUM_inputbox.toPlainText()))
            self.NUM_line3.setText("")
            self.NUM_line4.setText(AM1036_Number.Hex_Number_DEC(self.NUM_inputbox.toPlainText()))

        elif(self.NUM_cb.currentText() == '2진수'):
            self.NUM_line1.setText("")
            self.NUM_line2.setText(AM1036_Number.Oct_Number_BIN(self.NUM_inputbox.toPlainText()))
            self.NUM_line3.setText(AM1036_Number.Dec_Number_BIN(self.NUM_inputbox.toPlainText()))
            self.NUM_line4.setText(AM1036_Number.Hex_Number_BIN(self.NUM_inputbox.toPlainText()))
        
        elif(self.NUM_cb.currentText() == '8진수'):
            self.NUM_line1.setText(AM1036_Number.Bin_Number_OCT(self.NUM_inputbox.toPlainText()))
            self.NUM_line2.setText("")
            self.NUM_line3.setText(AM1036_Number.Dec_Number_OCT(self.NUM_inputbox.toPlainText()))
            self.NUM_line4.setText(AM1036_Number.Hex_Number_OCT(self.NUM_inputbox.toPlainText()))
        
        elif(self.NUM_cb.currentText() == '16진수'):
            self.NUM_line1.setText(AM1036_Number.Bin_Number_HEX(self.NUM_inputbox.toPlainText()))
            self.NUM_line2.setText(AM1036_Number.Oct_Number_HEX(self.NUM_inputbox.toPlainText()))
            self.NUM_line3.setText(AM1036_Number.Dec_Number_HEX(self.NUM_inputbox.toPlainText()))
            self.NUM_line4.setText("")

    def Num_Reset_Btn(self):
        self.NUM_line1.setText("")
        self.NUM_line2.setText("")
        self.NUM_line3.setText("")
        self.NUM_line4.setText("")
        self.NUM_inputbox.setText("")
        self.NUM_ckbox1.setChecked(True)
        self.NUM_ckbox2.setChecked(True)
        self.NUM_ckbox3.setChecked(True)
        self.NUM_ckbox4.setChecked(True)
        self.NUM_cb.setCurrentIndex(0)

    def Num_Cb(self):
        self.NUM_inputbox.setText("")

    def Num_CkBox1(self, state):
        if state == Qt.Checked:
            self.NUM_line1.setEchoMode(QLineEdit.Normal)
        else:
            self.NUM_line1.setEchoMode(QLineEdit.NoEcho)

    def Num_CkBox2(self, state):
        if state == Qt.Checked:
            self.NUM_line2.setEchoMode(QLineEdit.Normal)
        else:
            self.NUM_line2.setEchoMode(QLineEdit.NoEcho)

    def Num_CkBox3(self, state):
        if state == Qt.Checked:
            self.NUM_line3.setEchoMode(QLineEdit.Normal)
        else:
            self.NUM_line3.setEchoMode(QLineEdit.NoEcho)

    def Num_CkBox4(self, state):
        if state == Qt.Checked:
            self.NUM_line4.setEchoMode(QLineEdit.Normal)
        else:
            self.NUM_line4.setEchoMode(QLineEdit.NoEcho)

######################################################################################################
    def Tab2(self):
        grid = QGridLayout()

        self.ASC_label = QLabel('INPUT DATA')
        self.ASC_ckbox1 = QCheckBox('BASE64', self)
        self.ASC_ckbox2 = QCheckBox('URL(K)', self)
        self.ASC_ckbox3 = QCheckBox('URL(E)', self)
        self.ASC_ckbox4 = QCheckBox('ASCII', self)

        self.ASC_ckbox1.toggle()
        self.ASC_ckbox2.toggle()
        self.ASC_ckbox3.toggle()
        self.ASC_ckbox4.toggle()

        self.ASC_ckbox1.stateChanged.connect(self.ASCII_Ck_Box1)
        self.ASC_ckbox2.stateChanged.connect(self.ASCII_Ck_Box2)
        self.ASC_ckbox3.stateChanged.connect(self.ASCII_Ck_Box3)
        self.ASC_ckbox4.stateChanged.connect(self.ASCII_Ck_Box4)

        self.ASC_line1 = QLineEdit()
        self.ASC_line2 = QLineEdit()
        self.ASC_line3 = QLineEdit()
        self.ASC_line4 = QLineEdit()

        self.ASC_inputbox = QTextEdit()

        ASC_btn_encoding = QPushButton('ENCODING',self)
        ASC_btn_decoding = QPushButton('DECODING',self)
        ASC_btn_reset = QPushButton('RESET', self)
        
        ASC_btn_encoding.clicked.connect(self.ASCII_Encoding_Btn)
        ASC_btn_decoding.clicked.connect(self.ASCII_Decoding_Btn)
        ASC_btn_reset.clicked.connect(self.ASCII_Reset_Btn)

        # Grid Set
        grid.addWidget(self.ASC_ckbox1,0,0)
        grid.addWidget(self.ASC_ckbox2,1,0)
        grid.addWidget(self.ASC_ckbox3,2,0)
        grid.addWidget(self.ASC_ckbox4,3,0)
        grid.addWidget(self.ASC_label,4,0)

        grid.addWidget(self.ASC_line1,0,1,1,6)
        grid.addWidget(self.ASC_line2,1,1,1,6)
        grid.addWidget(self.ASC_line3,2,1,1,6)
        grid.addWidget(self.ASC_line4,3,1,1,6)

        grid.addWidget(self.ASC_inputbox,5,0,1,7)

        grid.addWidget(ASC_btn_encoding,6,2)
        grid.addWidget(ASC_btn_decoding,6,3)
        grid.addWidget(ASC_btn_reset,6,4)
        
        tab = QWidget()
        tab.setLayout(grid)
        return tab

    def ASCII_Encoding_Btn(self):
        self.ASC_line1.setText(AM1036_ASCII.Base64_Encode(self.ASC_inputbox.toPlainText()))
        self.ASC_line2.setText(AM1036_ASCII.Url_Encode_Hangle(self.ASC_inputbox.toPlainText()))
        self.ASC_line3.setText(AM1036_ASCII.Url_Encode_English(self.ASC_inputbox.toPlainText()))
        self.ASC_line4.setText(AM1036_ASCII.Ascii_Encode(self.ASC_inputbox.toPlainText()))

    def ASCII_Decoding_Btn(self):
        self.ASC_line1.setText(AM1036_ASCII.Base64_Decode(self.ASC_inputbox.toPlainText()))
        self.ASC_line2.setText(AM1036_ASCII.Url_Decode_Hangle(self.ASC_inputbox.toPlainText()))
        self.ASC_line3.setText(AM1036_ASCII.Url_Decode_English(self.ASC_inputbox.toPlainText()))            
        self.ASC_line4.setText(AM1036_ASCII.Ascii_Decode(self.ASC_inputbox.toPlainText()))

    def ASCII_Reset_Btn(self):
        self.ASC_line1.setText("")
        self.ASC_line2.setText("")
        self.ASC_line3.setText("")
        self.ASC_line4.setText("")
        self.ASC_inputbox.setText("")
        self.ASC_ckbox1.setChecked(True)
        self.ASC_ckbox2.setChecked(True)
        self.ASC_ckbox3.setChecked(True)
        self.ASC_ckbox4.setChecked(True)

    def ASCII_Ck_Box1(self, state):
        if state == Qt.Checked:
            self.ASC_line1.setEchoMode(QLineEdit.Normal)
        else:
            self.ASC_line1.setEchoMode(QLineEdit.NoEcho)

    def ASCII_Ck_Box2(self, state):
        if state == Qt.Checked:
            self.ASC_line2.setEchoMode(QLineEdit.Normal)
        else:
            self.ASC_line2.setEchoMode(QLineEdit.NoEcho)

    def ASCII_Ck_Box3(self, state):
        if state == Qt.Checked:
            self.ASC_line3.setEchoMode(QLineEdit.Normal)
        else:
            self.ASC_line3.setEchoMode(QLineEdit.NoEcho)

    def ASCII_Ck_Box4(self, state):
        if state == Qt.Checked:
            self.ASC_line4.setEchoMode(QLineEdit.Normal)
        else:
            self.ASC_line4.setEchoMode(QLineEdit.NoEcho)

######################################################################################################
    def Tab3(self):
        grid = QGridLayout()

        self.HASH_label = QLabel('INPUT DATA')
        
        #체크 박스
        self.HASH_ckbox1 = QCheckBox('MD5', self)
        self.HASH_ckbox2 = QCheckBox('SHA-1', self)
        self.HASH_ckbox3 = QCheckBox('SHA-256', self)
        self.HASH_ckbox4 = QCheckBox('SHA-512', self)

        self.HASH_ckbox1.toggle()
        self.HASH_ckbox2.toggle()
        self.HASH_ckbox3.toggle()
        self.HASH_ckbox4.toggle()

        self.HASH_ckbox1.stateChanged.connect(self.Hash_Ck_Box5)
        self.HASH_ckbox2.stateChanged.connect(self.Hash_Ck_Box6)
        self.HASH_ckbox3.stateChanged.connect(self.Hash_Ck_Box7)
        self.HASH_ckbox4.stateChanged.connect(self.Hash_Ck_Box8)

        self.HASH_cb = QComboBox(self)
        self.HASH_cb.addItem('TEXT')
        self.HASH_cb.addItem('FILE')
        self.HASH_cb.activated.connect(self.Hash_Cb)
        self.HASH_line1 = QLineEdit()
        self.HASH_line2 = QLineEdit()
        self.HASH_line3 = QLineEdit()
        self.HASH_line4 = QLineEdit()
        self.HASH_inputbox = QTextEdit()

        HASH_btn_encoding = QPushButton('ENCODING',self)
        HASH_btn_decoding = QPushButton('DECODING',self)
        HASH_btn_reset = QPushButton('RESET', self)
        HASH_btn_file = QPushButton('FILE', self)
        
        HASH_btn_encoding.clicked.connect(self.Hash_Encoding_Btn)
        HASH_btn_decoding.clicked.connect(self.Hash_Decoding_Btn)
        HASH_btn_reset.clicked.connect(self.Hash_Reset_Btn)
        HASH_btn_file.clicked.connect(self.Hash_File_Btn)

        # Grid Set
        grid.addWidget(self.HASH_ckbox1,0,0)
        grid.addWidget(self.HASH_ckbox2,1,0)
        grid.addWidget(self.HASH_ckbox3,2,0)
        grid.addWidget(self.HASH_ckbox4,3,0)
        grid.addWidget(self.HASH_line1,0,1,1,14)
        grid.addWidget(self.HASH_line2,1,1,1,14)
        grid.addWidget(self.HASH_line3,2,1,1,14)
        grid.addWidget(self.HASH_line4,3,1,1,14)
        grid.addWidget(self.HASH_label,4,0)
        grid.addWidget(self.HASH_inputbox,6,0,1,15)
        grid.addWidget(self.HASH_cb,7,2)
        grid.addWidget(HASH_btn_file,7,3)
        grid.addWidget(HASH_btn_encoding,7,4)
        grid.addWidget(HASH_btn_decoding,7,5)
        grid.addWidget(HASH_btn_reset,7,6)
        
        tab = QWidget()
        tab.setLayout(grid)
        return tab

    def Hash_Encoding_Btn(self):
        if(self.HASH_cb.currentText() == 'TEXT'):
            self.HASH_line1.setText(AM1036_Hash.MD5_Encode(self.HASH_inputbox.toPlainText()))
            self.HASH_line2.setText(AM1036_Hash.SHA1_Encode(self.HASH_inputbox.toPlainText()))
            self.HASH_line3.setText(AM1036_Hash.SHA256_Encode(self.HASH_inputbox.toPlainText()))
            self.HASH_line4.setText(AM1036_Hash.SHA512_Encode(self.HASH_inputbox.toPlainText()))
        else:
            self.HASH_line1.setText(AM1036_Hash.MD5_Encode_F(self.HASH_inputbox.toPlainText()))
            self.HASH_line2.setText(AM1036_Hash.SHA1_Encode_F(self.HASH_inputbox.toPlainText()))
            self.HASH_line3.setText(AM1036_Hash.SHA256_Encode_F(self.HASH_inputbox.toPlainText()))
            self.HASH_line4.setText(AM1036_Hash.SHA512_Encode_F(self.HASH_inputbox.toPlainText()))

    def Hash_Decoding_Btn(self):
        if(self.HASH_cb.currentText() == 'TEXT'):
            self.ASC_line1.setText(AM1036_Hash.Base64_Decode(self.HASH_inputbox.toPlainText()))
            self.ASC_line2.setText(AM1036_Hash.Url_Decode_Hangle(self.HASH_inputbox.toPlainText()))
            self.ASC_line3.setText(AM1036_Hash.Url_Decode_English(self.HASH_inputbox.toPlainText()))            
            self.ASC_line4.setText(AM1036_Hash.Ascii_Decode(self.HASH_inputbox.toPlainText()))
        else:
            self.HASH_line1.setText("")
            self.HASH_line2.setText("")
            self.HASH_line3.setText("")
            self.HASH_line4.setText("")

    def Hash_Reset_Btn(self):
        self.HASH_line1.setText("")
        self.HASH_line2.setText("")
        self.HASH_line3.setText("")
        self.HASH_line4.setText("")
        self.HASH_ckbox1.setChecked(True)
        self.HASH_ckbox2.setChecked(True)
        self.HASH_ckbox3.setChecked(True)
        self.HASH_ckbox4.setChecked(True)
        self.HASH_cb.setCurrentIndex(0)

    def Hash_File_Btn(self):
        if(self.HASH_cb.currentText() == 'FILE'):
            path = QFileDialog.getOpenFileName(self)

            self.HASH_inputbox.setText(path[0])
        else:
            msg = "'TEXT' -> 'FILE"
            title = "error"
            msg_box = QMessageBox(self)
            msg_box.question(self, title, msg, QMessageBox.Ok)

    def Hash_Cb(self):
        self.HASH_inputbox.setText("")
     
    def Hash_Ck_Box5(self, state):
        if state == Qt.Checked:
            self.HASH_line1.setEchoMode(QLineEdit.Normal)
        else:
            self.HASH_line1.setEchoMode(QLineEdit.NoEcho)

    def Hash_Ck_Box6(self, state):
        if state == Qt.Checked:
            self.HASH_line2.setEchoMode(QLineEdit.Normal)
        else:
            self.HASH_line2.setEchoMode(QLineEdit.NoEcho)

    def Hash_Ck_Box7(self, state):
        if state == Qt.Checked:
            self.HASH_line3.setEchoMode(QLineEdit.Normal)
        else:
            self.HASH_line3.setEchoMode(QLineEdit.NoEcho)

    def Hash_Ck_Box8(self, state):
        if state == Qt.Checked:
            self.HASH_line4.setEchoMode(QLineEdit.Normal)
        else:
            self.HASH_line4.setEchoMode(QLineEdit.NoEcho)

######################################################################################################
    def Tab4(self):
        grid = QGridLayout()
        
        self.CER_label1 = QLabel('INPUT DATA')
        self.CER_label2 = QLabel('RESULT DATA')
        self.CER_resultbox = QTextEdit()
        self.CER_inputbox = QTextEdit()

        CER_btn_encoding = QPushButton('ENCODING', self)
        CER_btn_encoding.clicked.connect(self.Ceasar_Encode)

        self.CER_spinbox = QSpinBox()
        self.CER_spinbox.setRange(-25,25)
        self.CER_spinbox.setSingleStep(1)

        # Grid Set
        grid.addWidget(self.CER_label1,0,0)
        grid.addWidget(self.CER_label2,0,2)
        grid.addWidget(self.CER_inputbox,1,0,1,2)
        grid.addWidget(self.CER_resultbox,1,2,1,2)
        grid.addWidget(self.CER_spinbox,2,1)
        grid.addWidget(CER_btn_encoding,2,2)

        tab = QWidget()
        tab.setLayout(grid)
        return tab

    def Ceasar_Encode(self):
        self.CER_resultbox.setText(AM1036_Cersar.Ceasar_Crypt(self.CER_inputbox.toPlainText(),self.CER_spinbox.value()))

######################################################################################################
    def Tab5(self):
        grid = QGridLayout()

        self.RSA_label1 = QLabel('DATA', self)
        self.RSA_label2 = QLabel('Private Key', self)
        self.RSA_label3 = QLabel('Public Key',self)
        self.RSA_label5 = QLabel('Input Data',self)
        self.RSA_label6 = QLabel('   Key Size :', self)
        
        self.RSA_databox = QTextEdit()
        self.RSA_prikeybox = QTextEdit()
        self.RSA_pubkeybox = QTextEdit()
        self.RSA_pathline = QLineEdit()
        self.RSA_inputdata = QTextEdit()

        RSA_btn_createkey = QPushButton('Create Key', self)
        RSA_btn_encoding = QPushButton('ENCODING', self)
        RSA_btn_decoding = QPushButton('DECODING', self)
        RSA_btn_path = QPushButton('PATH',self)

        RSA_btn_createkey.clicked.connect(self.RSA_CreateKey_Btn)
        RSA_btn_encoding.clicked.connect(self.RSA_Encoding_Btn)
        RSA_btn_decoding.clicked.connect(self.RSA_Decoding_Btn)
        RSA_btn_path.clicked.connect(self.RSA_Path_Btn)

        self.RSA_cb1 = QComboBox(self)
        self.RSA_cb1.addItem('RSA PKCS#1 v1.5')
        self.RSA_cb1.addItem('RSA PKCS#1 OAEP')

        self.RSA_cb2 = QComboBox(self)
        self.RSA_cb2.addItem('1024')
        self.RSA_cb2.addItem('512')
        self.RSA_cb2.addItem('2048')
        self.RSA_cb2.addItem('4096')

        self.RSA_cb1.activated.connect(self.RSA_Cb1)
        self.RSA_cb2.activated.connect(self.RSA_Cb2)

        # Grid Set
        grid.addWidget(self.RSA_cb1,0,0,1,7)
        grid.addWidget(self.RSA_label6,0,7)
        grid.addWidget(self.RSA_cb2,0,8)
        grid.addWidget(self.RSA_label1,1,0)
        grid.addWidget(self.RSA_databox,2,0,1,9)
        grid.addWidget(self.RSA_label2,3,0)
        grid.addWidget(self.RSA_label3,3,5)
        grid.addWidget(self.RSA_prikeybox,4,0,1,5)
        grid.addWidget(self.RSA_pubkeybox,4,5,1,4)
        grid.addWidget(self.RSA_label5,5,0)
        grid.addWidget(self.RSA_inputdata,6,0,1,9)
        grid.addWidget(RSA_btn_path,7,0)
        grid.addWidget(self.RSA_pathline,7,1,1,8)
        grid.addWidget(RSA_btn_createkey,8,3)
        grid.addWidget(RSA_btn_encoding,8,4)
        grid.addWidget(RSA_btn_decoding,8,5)

        tab = QWidget()
        tab.setLayout(grid)
        return tab

    def RSA_Encoding_Btn(self):
        if(self.RSA_cb1.currentText() == 'RSA PKCS#1 v1.5'):
            self.RSA_databox.setText(AM1036_RSA.RSA_PKCS1_v1_5_Encode(self.RSA_pathline.text(),self.RSA_inputdata.toPlainText()))
        
        elif(self.RSA_cb1.currentText() == 'RSA PKCS#1 OAEP'):
            self.RSA_databox.setText(AM1036_RSA.RSA_OAEP_Encode(self.RSA_pathline.text(),self.RSA_inputdata.toPlainText()))

    def RSA_Decoding_Btn(self):
        if(self.RSA_cb1.currentText() == 'RSA PKCS#1 v1.5'):
            self.RSA_databox.setText(AM1036_RSA.RSA_PKCS1_v1_5_Decode(self.RSA_pathline.text()))

        elif(self.RSA_cb1.currentText() == 'RSA PKCS#1 OAEP'):
            self.RSA_databox.setText(AM1036_RSA.RSA_OAEP_Decode(self.RSA_pathline.text()))

    def RSA_CreateKey_Btn(self):
        AM1036_RSA.Create_Key(self.RSA_pathline.text(),self.RSA_cb2.currentText())
        self.RSA_prikeybox.setText(AM1036_RSA.Read_Pri_Key(self.RSA_pathline.text()))
        self.RSA_pubkeybox.setText(AM1036_RSA.Read_Pub_Key(self.RSA_pathline.text()))
        QMessageBox.about(self, "createkey", "created!!!")

    def RSA_Path_Btn(self):
        path = QFileDialog.getExistingDirectory(self)
        self.RSA_pathline.setText(path+'\\')

    def RSA_Cb1(self):
        self.RSA_databox.setText("")
        self.RSA_inputdata.setText("")
        self.RSA_pathline.setText("")

    def RSA_Cb2(self):
        self.RSA_databox.setText("")
        self.RSA_inputdata.setText("")
        self.RSA_pathline.setText("")
        self.RSA_prikeybox.setText("")
        self.RSA_pubkeybox.setText("")

######################################################################################################
    def Tab6(self):
        grid = QGridLayout()

        self.EXC_label1 = QLabel('Extension', self)
        self.EXC_label2 = QLabel('Process', self)
        self.EXC_label3 = QLabel('Path', self)
        self.EXC_label4 = QLabel('Input Data', self)
        self.EXC_textbox1 = QTextEdit()
        self.EXC_textbox2 = QTextEdit()
        self.EXC_textbox3 = QTextEdit()
        self.EXC_input_box = QTextEdit()

        EXC_btn_add_extension = QPushButton('+', self)
        EXC_btn_sub_extension = QPushButton('-', self)
        EXC_btn_add_process = QPushButton('+', self)
        EXC_btn_sub_process = QPushButton('-', self)
        EXC_btn_add_path = QPushButton('+', self)
        EXC_btn_sub_path = QPushButton('-', self)

        self.EXC_label1.setAlignment(Qt.AlignCenter)
        self.EXC_label2.setAlignment(Qt.AlignCenter)
        self.EXC_label3.setAlignment(Qt.AlignCenter)

        EXC_btn_add_extension.clicked.connect(self.DEFEN_BtnAdd1)
        EXC_btn_add_process.clicked.connect(self.DEFEN_BtnAdd2)
        EXC_btn_add_path.clicked.connect(self.DEFEN_BtnAdd3)
        EXC_btn_sub_extension.clicked.connect(self.DEFEN_BtnSub1)
        EXC_btn_sub_process.clicked.connect(self.DEFEN_BtnSub2)
        EXC_btn_sub_process.clicked.connect(self.DEFEN_BtnSub3)

        # Grid Set
        grid.addWidget(self.EXC_label1,0,0,1,2)
        grid.addWidget(self.EXC_label2,0,2,1,2)
        grid.addWidget(self.EXC_label3,0,4,1,2)
        grid.addWidget(self.EXC_textbox1,1,0,1,2)
        grid.addWidget(self.EXC_textbox2,1,2,1,2)
        grid.addWidget(self.EXC_textbox3,1,4,1,2)
        grid.addWidget(EXC_btn_add_extension,2,0)
        grid.addWidget(EXC_btn_sub_extension,2,1)
        grid.addWidget(EXC_btn_add_process,2,2)
        grid.addWidget(EXC_btn_sub_process,2,3)
        grid.addWidget(EXC_btn_add_path,2,4)
        grid.addWidget(EXC_btn_sub_path,2,5)
        grid.addWidget(self.EXC_label4,3,0)
        grid.addWidget(self.EXC_input_box,4,0,1,6)

        self.EXC_textbox1.setText(AM1036_Exception.list_extension())
        self.EXC_textbox2.setText(AM1036_Exception.list_process())
        self.EXC_textbox3.setText(AM1036_Exception.list_path())

        tab = QWidget()
        tab.setLayout(grid)
        return tab

    def DEFEN_BtnAdd1(self):
        AM1036_Exception.AddExtension(self.EXC_input_box.toPlainText())
        self.EXC_textbox1.setText(AM1036_Exception.list_extension())

    def DEFEN_BtnAdd2(self):
        AM1036_Exception.AddProcess(self.EXC_input_box.toPlainText())
        self.EXC_textbox2.setText(AM1036_Exception.list_process())

    def DEFEN_BtnAdd3(self):
        AM1036_Exception.AddPath(self.EXC_input_box.toPlainText())
        self.EXC_textbox3.setText(AM1036_Exception.list_path())

    def DEFEN_BtnSub1(self):
        AM1036_Exception.SubExtension(self.EXC_input_box.toPlainText())
        self.EXC_textbox1.setText(AM1036_Exception.list_extension())

    def DEFEN_BtnSub2(self):
        AM1036_Exception.SubProcess(self.EXC_input_box.toPlainText())
        self.EXC_textbox2.setText(AM1036_Exception.list_process())

    def DEFEN_BtnSub3(self):
        AM1036_Exception.SubPath(self.EXC_input_box.toPlainText())
        self.EXC_textbox3.setText(AM1036_Exception.list_path())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())