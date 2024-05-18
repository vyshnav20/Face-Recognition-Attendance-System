import random
from PyQt5 import QtCore, QtGui, QtWidgets
from w import code_4
from g import phone,updt_pass

class Ui_Mainwindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1776, 870)
        MainWindow.setStyleSheet("*{\n"
"border:none;\n"
"background-color:transparent;\n"
"background: transparent;\n"
"padding: 0;\n"
"margin: 0;\n"
"color: #fff;\n"
"}\n"
"#TeacherStudent{\n"
"border: solid 10px grey;\n"
"background-color: rgba(180, 180, 180,50);\n"
"color:rgb(0,0,0)\n"
"}\n"
"#centralwidget{\n"
"    border-image: url(:/newPrefix/6.JPG);\n"
"}\n"
"#main{\n"
"border: solid 10px grey;\n"
"background-color: rgba(180, 180, 180,200);\n"
"color:rgb(0,0,0)\n"
"}\n"
"QLabel{\n"
"color:rgb(0, 0, 0);\n"
"}\n"
"QLineEdit{\n"
"border: 2px solid rgb(255,255,255);\n"
"border-radius: 20px;\n"
"color: rgb(0, 0, 0);\n"
"padding-left:20px;\n"
"padding-right:20px;\n"
"backgrounnd-color: rgb(34,36,44);\n"
"}\n"
"QLineEdit:hover{\n"
"border:2px solid rgb(0,0,0);}\n"
"QlineEdit:focus{\n"
"border: 2px solid rgb(251, 255, 0);\n"
"background-color:rgb(43,45,56);\n"
"}\n"
"QRadioButton{\n"
"border:1px solid rgb(255,255,255);\n"
"border-radius:60px;}\n"
"QRadioButton:checked{\n"
"border:1px solid rgb(0, 0, 0);\n"
"border-radius:60px;}\n"
"#verify,#Up_p,#otp{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:25px;\n"
"color: rgb(0,0,0);\n"
"}\n"
"#otp:hover{\n"
"background-color: rgb(0,0,0);\n"
"border-radius:25px;\n"
"color: rgb(255,255,255);\n"
"}\n"
"#verify:hover{\n"
"background-color: rgb(0,0,0);\n"
"border-radius:25px;\n"
"color: rgb(255,255,255);\n"
"}\n"
"#Up_p:hover{\n"
"background-color: rgb(0,0,0);\n"
"border-radius:25px;\n"
"color: rgb(255,255,255);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Title = QtWidgets.QWidget(self.centralwidget)
        self.Title.setObjectName("Title")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Title)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.Title)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("BlackChancery")
        font.setPointSize(45)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_2.addWidget(self.frame_5, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.Title)
        self.Body = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Body.sizePolicy().hasHeightForWidth())
        self.Body.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Habisa")
        self.Body.setFont(font)
        self.Body.setObjectName("Body")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Body)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Login = QtWidgets.QWidget(self.Body)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Login.sizePolicy().hasHeightForWidth())
        self.Login.setSizePolicy(sizePolicy)
        self.Login.setObjectName("Login")
        self.main = QtWidgets.QWidget(self.Login)
        self.main.setGeometry(QtCore.QRect(590, 0, 761, 771))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy)
        self.main.setObjectName("main")
        self.verify = QtWidgets.QPushButton(self.main)
        self.verify.setGeometry(QtCore.QRect(300, 390, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Bananas Personal Use")
        font.setPointSize(38)
        font.setBold(False)
        font.setWeight(50)
        self.verify.setFont(font)
        self.verify.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.verify.setIcon(icon)
        self.verify.setIconSize(QtCore.QSize(100, 50))
        self.verify.setObjectName("verify")
        self.frame_6 = QtWidgets.QFrame(self.main)
        self.frame_6.setGeometry(QtCore.QRect(40, 80, 691, 191))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.frame_8 = QtWidgets.QFrame(self.frame_6)
        self.frame_8.setGeometry(QtCore.QRect(10, 10, 211, 131))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.frame_9 = QtWidgets.QFrame(self.frame_6)
        self.frame_9.setGeometry(QtCore.QRect(120, 10, 501, 101))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_9)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 40, 271, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("")
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.frame_9)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.ip_2 = QtWidgets.QLabel(self.frame_6)
        self.ip_2.setGeometry(QtCore.QRect(210, 120, 461, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ip_2.setFont(font)
        self.ip_2.setObjectName("ip_2")
        self.otp = QtWidgets.QPushButton(self.frame_6)
        self.otp.setGeometry(QtCore.QRect(240, 100, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Bananas Personal Use")
        font.setPointSize(38)
        font.setBold(False)
        font.setWeight(50)
        self.otp.setFont(font)
        self.otp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.otp.setIcon(icon)
        self.otp.setIconSize(QtCore.QSize(100, 50))
        self.otp.setObjectName("otp")
        self.frame_7 = QtWidgets.QFrame(self.main)
        self.frame_7.setGeometry(QtCore.QRect(40, 270, 781, 141))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.frame_11 = QtWidgets.QFrame(self.frame_7)
        self.frame_11.setGeometry(QtCore.QRect(-100, 10, 841, 151))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame_11)
        self.plainTextEdit.setGeometry(QtCore.QRect(170, 0, 671, 41))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("color:rgb(0,0,0);\n"
"")
        self.plainTextEdit.setFrameShape(QtWidgets.QFrame.Box)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_11)
        self.lineEdit_3.setGeometry(QtCore.QRect(370, 50, 271, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("")
        self.lineEdit_3.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_3.setClearButtonEnabled(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.ip = QtWidgets.QLabel(self.main)
        self.ip.setGeometry(QtCore.QRect(320, 450, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ip.setFont(font)
        self.ip.setObjectName("ip")
        self.up = QtWidgets.QWidget(self.main)
        self.up.setGeometry(QtCore.QRect(120, 530, 571, 191))
        self.up.setObjectName("up")
        self.Up_p = QtWidgets.QPushButton(self.up)
        self.Up_p.setGeometry(QtCore.QRect(180, 110, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Bananas Personal Use")
        font.setPointSize(38)
        font.setBold(False)
        font.setWeight(50)
        self.Up_p.setFont(font)
        self.Up_p.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Up_p.setIcon(icon)
        self.Up_p.setIconSize(QtCore.QSize(100, 50))
        self.Up_p.setObjectName("Up_p")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.up)
        self.lineEdit_4.setGeometry(QtCore.QRect(270, 50, 271, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("")
        self.lineEdit_4.setClearButtonEnabled(False)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(self.up)
        self.label_4.setGeometry(QtCore.QRect(20, 50, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.main)
        self.label_5.setGeometry(QtCore.QRect(189, 20, 442, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Serif")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.Login)
        self.verticalLayout.addWidget(self.Body)
        MainWindow.setCentralWidget(self.centralwidget)
        self.ip.setHidden(True)
        self.ip_2.setHidden(True)
        self.up.hide()
        c= random.randrange(1000, 10000)
        self.verify.clicked.connect(lambda: self.v(c))
        self.Up_p.clicked.connect(self.uptd)
        self.otp.clicked.connect(lambda: self.code4(c))
        self.retranslateUi(MainWindow)
        self.plainTextEdit.setHidden(True)
        self.lineEdit_3.setHidden(True)
        self.verify.setHidden(True)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def code4(self,c):
        
        ph=phone(self.lineEdit_2.text())
        if not ph:
            self.ip_2.setHidden(False)
        else:
            self.ip_2.setHidden(True)
            code_4(ph[0][0],c)
            self.plainTextEdit.setHidden(False)
            self.lineEdit_3.setHidden(False)
            self.verify.setHidden(False)

    def uptd(self):
        new_pass=self.lineEdit_4.text()
        updt_pass(self.lineEdit_2.text(),new_pass)
        
    
    def v(self,c):
        if(self.lineEdit_3.text()==str(c)):
            self.ip.setHidden(True)
            self.up.setVisible(True)
        else:
            self.ip.setHidden(False)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Face Recognition Attendance System"))
        self.label.setText(_translate("MainWindow", "Face Recognition Attendance System"))
        self.verify.setText(_translate("MainWindow", "Verify"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Username"))
        self.label_3.setText(_translate("MainWindow", "Username:"))
        self.ip_2.setText(_translate("MainWindow", "Enter a valid Username!!"))
        self.otp.setText(_translate("MainWindow", "Send OTP"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "Enter 4 digit code sent to your registered phone numbers\' WhtasApp "))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "4-Digit Code"))
        self.ip.setText(_translate("MainWindow", "Incorrect Code!!"))
        self.Up_p.setText(_translate("MainWindow", "Update Password"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "New Password"))
        self.label_4.setText(_translate("MainWindow", "New Password:"))
        self.label_5.setText(_translate("MainWindow", "Forgot Password!!!"))
import i_rc