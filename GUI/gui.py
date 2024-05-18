from main2 import MainWind
from main import MainWindo
from x import Ui_Mainwindow
from PyQt5 import QtCore, QtGui, QtWidgets
from g import logint_db,tr_db,logins_db,st_db



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
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
"border-image: url(:/newPrefix/7.JPG);\n"
"}\n"
"#main{\n"
"border: solid 10px grey;\n"
"background-color: rgba(180, 180, 180,127);\n"
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
"#pushButton:hover{\n"
"color:rgb(255, 255, 255)\n"
"}\n"
"#pushButton{\n"
"color:rgb(0, 0, 0)\n"
"}\n"
"#login_btn{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:25px;\n"
"color: rgb(0,0,0);\n"
"}\n"
"#login_btn:hover{\n"
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
        self.TeacherStudent = QtWidgets.QWidget(self.Body)
        self.TeacherStudent.setMinimumSize(QtCore.QSize(450, 0))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        self.TeacherStudent.setFont(font)
        self.TeacherStudent.setObjectName("TeacherStudent")
        self.frame = QtWidgets.QFrame(self.TeacherStudent)
        self.frame.setGeometry(QtCore.QRect(0, -1, 1000, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(100, 30, 231, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Serif")
        font.setPointSize(30)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.radioButton = QtWidgets.QRadioButton(self.TeacherStudent)
        self.radioButton.setGeometry(QtCore.QRect(130, 120, 161, 191))
        self.radioButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/tr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButton.setIcon(icon)
        self.radioButton.setIconSize(QtCore.QSize(300, 300))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.TeacherStudent)
        self.radioButton_2.setGeometry(QtCore.QRect(130, 410, 161, 201))
        self.radioButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/st.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButton_2.setIcon(icon1)
        self.radioButton_2.setIconSize(QtCore.QSize(150, 350))
        self.radioButton_2.setCheckable(True)
        self.radioButton_2.setChecked(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.TeacherStudent, 0, QtCore.Qt.AlignLeft)
        self.Login = QtWidgets.QWidget(self.Body)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Login.sizePolicy().hasHeightForWidth())
        self.Login.setSizePolicy(sizePolicy)
        self.Login.setObjectName("Login")
        self.main = QtWidgets.QWidget(self.Login)
        self.main.setGeometry(QtCore.QRect(362, 152, 591, 481))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy)
        self.main.setObjectName("main")
        self.login_btn = QtWidgets.QPushButton(self.main)
        self.login_btn.setGeometry(QtCore.QRect(190, 270, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Bananas Personal Use")
        font.setPointSize(38)
        font.setBold(False)
        font.setWeight(50)
        self.login_btn.setFont(font)
        self.login_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.login_btn.setIcon(icon2)
        self.login_btn.setIconSize(QtCore.QSize(100, 50))
        self.login_btn.setObjectName("login_btn")
        self.frame_6 = QtWidgets.QFrame(self.main)
        self.frame_6.setGeometry(QtCore.QRect(20, 80, 511, 101))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.frame_8 = QtWidgets.QFrame(self.frame_6)
        self.frame_8.setGeometry(QtCore.QRect(10, 10, 211, 131))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.label_3 = QtWidgets.QLabel(self.frame_8)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(23)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.frame_9 = QtWidgets.QFrame(self.frame_6)
        self.frame_9.setGeometry(QtCore.QRect(140, 10, 371, 131))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_9)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 40, 271, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("")
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.frame_7 = QtWidgets.QFrame(self.main)
        self.frame_7.setGeometry(QtCore.QRect(20, 170, 501, 111))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.frame_10 = QtWidgets.QFrame(self.frame_7)
        self.frame_10.setGeometry(QtCore.QRect(20, 10, 201, 151))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.label_4 = QtWidgets.QLabel(self.frame_10)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 171, 50))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(23)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.frame_11 = QtWidgets.QFrame(self.frame_7)
        self.frame_11.setGeometry(QtCore.QRect(140, 10, 381, 151))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_11)
        self.lineEdit.setGeometry(QtCore.QRect(80, 20, 271, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.ip = QtWidgets.QLabel(self.main)
        self.ip.setGeometry(QtCore.QRect(150, 340, 411, 31))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(19)
        self.ip.setFont(font)
        self.ip.setObjectName("ip")
        self.frame_3 = QtWidgets.QFrame(self.main)
        self.frame_3.setGeometry(QtCore.QRect(60, 20, 451, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Noto Serif")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.pushButton = QtWidgets.QPushButton(self.main)
        self.pushButton.setGeometry(QtCore.QRect(200, 410, 201, 23))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(17)
        font.setUnderline(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.Login)
        self.verticalLayout.addWidget(self.Body)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.fp)
        self.login_btn.clicked.connect(self.login)
        self.ip.setHidden(True)
        self.radioButton.setChecked(True)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def fp(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_Mainwindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def login(self):
        username=int(self.lineEdit_2.text())
        password=self.lineEdit.text()
        if self.radioButton.isChecked():
            db_pass=logint_db(username)
            if not db_pass:
                self.ip.setHidden(False)
                self.lineEdit.clear()
                self.lineEdit_2.clear()

            elif(password!=db_pass[0][0]):
                self.ip.setHidden(False)
                self.lineEdit.clear()
                self.lineEdit_2.clear()
            else:
                self.window = MainWindo()
                self.tr_detail()
                
                MainWindow.hide()
                self.window.showMaximized()
        if self.radioButton_2.isChecked():
            db_pass=logins_db(username)
            if not db_pass:
                self.ip.setHidden(False)
                self.lineEdit.clear()
                self.lineEdit_2.clear()

            elif(password!=db_pass[0][0]):
                self.ip.setHidden(False)
                self.lineEdit.clear()
                self.lineEdit_2.clear()
            else:
                self.window = MainWind()
                self.st_detail()
                
                MainWindow.hide()
                self.window.showMaximized()

    def st_detail(self):
        result=st_db(self.lineEdit_2.text())
        self.window.ui.Tname.setText("Student Name: "+result[0][0])
        self.window.ui.Tid.setText("Student ID: "+str(result[0][1]))
        self.window.ui.TPh.setText("Phone Number: "+str(result[0][2]))
        self.window.ui.Cid.setText("Gender: "+result[0][3])
        
    
    def tr_detail(self):
        result=tr_db(self.lineEdit_2.text())
        
        self.window.ui.Tname.setText("Teacher Name:"+result[0][0])
        self.window.ui.Tid.setText("Teacher ID:"+str(result[0][1]))
        self.window.ui.TPh.setText("Phone Number:"+str(result[0][2]))
        self.window.ui.Cid.setText("Class ID:"+result[0][3])
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Face Recognition Attendance System"))
        self.label.setText(_translate("MainWindow", "Face Recognition Attendance System"))
        self.label_2.setText(_translate("MainWindow", "Select User"))
        self.login_btn.setText(_translate("MainWindow", "Login"))
        self.label_3.setText(_translate("MainWindow", "Username:"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Username"))
        self.label_4.setText(_translate("MainWindow", "Password:"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Password"))
        self.ip.setText(_translate("MainWindow", "Incorrect Username or Password!!"))
        self.label_5.setText(_translate("MainWindow", "Student/Teacher Login"))
        self.pushButton.setText(_translate("MainWindow", "Forgot Password?"))
import i_rc
import ctypes
if __name__ == "__main__":
    import sys
    myappid = 'fras'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    app = QtWidgets.QApplication(sys.argv)
    icon=QtGui.QIcon('icon.ico')
    app.setWindowIcon(icon)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    MainWindow.setWindowIcon(icon)
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())