from g import data
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget

import i_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1373, 747)
        MainWindow.setStyleSheet(u"*{\n"
"border:none;\n"
"background-color:transparent;\n"
"background: transparent;\n"
"padding: 0;\n"
"margin: 0;\n"
"color: #fff;\n"
"}\n"
"\n"
"#centralwidget{\n"
"	background-image: url(:/newPrefix/6081504.jpg);\n"
"}\n"
"\n"
"#Title,#sub_title{\n"
"background-color:rgba(0, 0, 0,175);\n"
"}\n"
"#Body{\n"
"background-color:rgba(0, 0, 0,127);\n"
"}\n"
"\n"
"QPushButton{\n"
"text-align:left;\n"
"padding:5px 10px;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius:10px;}\n"
"\n"
"#home_btn{\n"
"border-left: 3px solid rgb(255, 0, 0);\n"
"font-weight: bold}\n"
"\n"
"QLineEdit{\n"
"border: 2px solid rgb(0, 251, 255);\n"
"border-radius: 20px;\n"
"color: #fff;\n"
"padding-left:20px;\n"
"padding-right:20px;\n"
"backgrounnd-color: rgb(34,36,44);\n"
"}\n"
"QLineEdit:hover{\n"
"border:2px solid rgb(255,0,0);}\n"
"QlineEdit:focus{\n"
"border: 2px solid rgb(251, 255, 0);\n"
"background-color:rgb(43,45,56);\n"
"}\n"
"\n"
"#register_btn{\n"
"background-color: rgb(0, 251, 255);\n"
"border-radius:10px;\n"
"color:"
                        " rgb(0,0,0);\n"
"}\n"
"\n"
"#register_btn:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(0, 0, 0, 255));\n"
"border-radius:10px;\n"
"color: rgb(255,0,0);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Title = QWidget(self.centralwidget)
        self.Title.setObjectName(u"Title")
        self.horizontalLayout_3 = QHBoxLayout(self.Title)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_6 = QFrame(self.Title)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamily(u"Revengeance")
        font.setPointSize(28)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)

        self.verticalLayout_3.addWidget(self.label_2)


        self.horizontalLayout_3.addWidget(self.frame_6, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.Title, 0, Qt.AlignTop)

        self.Body = QWidget(self.centralwidget)
        self.Body.setObjectName(u"Body")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Body.sizePolicy().hasHeightForWidth())
        self.Body.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.Body)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 9, 9, 9)
        self.left_menu = QCustomSlideMenu(self.Body)
        self.left_menu.setObjectName(u"left_menu")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.left_menu.sizePolicy().hasHeightForWidth())
        self.left_menu.setSizePolicy(sizePolicy2)
        self.left_menu.setMinimumSize(QSize(200, 0))
        self.left_menu.setCursor(QCursor(Qt.ArrowCursor))
        self.left_menu.setStyleSheet(u"*{\n"
"background-color:rgba(0, 0, 0,80);\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.left_menu)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 0, 0, 0)
        self.widget = QWidget(self.left_menu)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 5, 0, 0)
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.home_btn = QPushButton(self.frame)
        self.home_btn.setObjectName(u"home_btn")
        self.home_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.home_btn)

        self.Register_Student = QPushButton(self.frame)
        self.Register_Student.setObjectName(u"Register_Student")
        self.Register_Student.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.Register_Student)

        self.B2 = QPushButton(self.frame)
        self.B2.setObjectName(u"B2")
        self.B2.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.B2)


        self.verticalLayout_6.addWidget(self.frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(180, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.Help = QPushButton(self.frame_2)
        self.Help.setObjectName(u"Help")
        self.Help.setEnabled(True)
        self.Help.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.Help)

        self.Settings = QPushButton(self.frame_2)
        self.Settings.setObjectName(u"Settings")
        self.Settings.setEnabled(True)
        self.Settings.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.Settings)


        self.verticalLayout_6.addWidget(self.frame_2)


        self.verticalLayout_5.addWidget(self.widget)


        self.horizontalLayout.addWidget(self.left_menu)

        self.content = QWidget(self.Body)
        self.content.setObjectName(u"content")
        self.verticalLayout_4 = QVBoxLayout(self.content)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.main_pages = QCustomStackedWidget(self.content)
        self.main_pages.setObjectName(u"main_pages")
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.label = QLabel(self.Home)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(470, 190, 231, 131))
        font1 = QFont()
        font1.setFamily(u"Malachite")
        font1.setPointSize(50)
        self.label.setFont(font1)
        self.main_pages.addWidget(self.Home)
        self.B1_page = QWidget()
        self.B1_page.setObjectName(u"B1_page")
        self.verticalLayout_8 = QVBoxLayout(self.B1_page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.sub_title = QWidget(self.B1_page)
        self.sub_title.setObjectName(u"sub_title")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.sub_title.sizePolicy().hasHeightForWidth())
        self.sub_title.setSizePolicy(sizePolicy3)
        self.sub_title.setMinimumSize(QSize(0, 100))
        self.horizontalLayout_2 = QHBoxLayout(self.sub_title)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_10 = QLabel(self.sub_title)
        self.label_10.setObjectName(u"label_10")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy4)
        font2 = QFont()
        font2.setPointSize(27)
        self.label_10.setFont(font2)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_10)


        self.verticalLayout_8.addWidget(self.sub_title)

        self.widget_2 = QWidget(self.B1_page)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(650, 0))
        self.formLayout = QFormLayout(self.widget_2)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setContentsMargins(-1, 0, -1, 0)
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)
        self.label_4.setMinimumSize(QSize(225, 0))
        font3 = QFont()
        font3.setPointSize(25)
        self.label_4.setFont(font3)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.name = QLineEdit(self.widget_2)
        self.name.setObjectName(u"name")
        sizePolicy4.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy4)
        self.name.setMaximumSize(QSize(400, 50))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.name)

        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")
        sizePolicy4.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy4)
        self.label_7.setMinimumSize(QSize(225, 0))
        self.label_7.setFont(font3)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.id = QLineEdit(self.widget_2)
        self.id.setObjectName(u"id")
        sizePolicy4.setHeightForWidth(self.id.sizePolicy().hasHeightForWidth())
        self.id.setSizePolicy(sizePolicy4)
        self.id.setMaximumSize(QSize(16777215, 50))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.id)

        self.label_8 = QLabel(self.widget_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy4.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy4)
        self.label_8.setMinimumSize(QSize(225, 0))
        self.label_8.setFont(font3)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_8)

        self.gender = QLineEdit(self.widget_2)
        self.gender.setObjectName(u"gender")
        sizePolicy4.setHeightForWidth(self.gender.sizePolicy().hasHeightForWidth())
        self.gender.setSizePolicy(sizePolicy4)
        self.gender.setMaximumSize(QSize(16777215, 50))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.gender)

        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")
        sizePolicy4.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy4)
        self.label_9.setFont(font3)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_9)

        self.pno = QLineEdit(self.widget_2)
        self.pno.setObjectName(u"pno")
        sizePolicy4.setHeightForWidth(self.pno.sizePolicy().hasHeightForWidth())
        self.pno.setSizePolicy(sizePolicy4)
        self.pno.setMaximumSize(QSize(16777215, 50))

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.pno)


        self.verticalLayout_8.addWidget(self.widget_2, 0, Qt.AlignHCenter)

        self.widget_3 = QWidget(self.B1_page)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(16777215, 75))
        self.verticalLayout_9 = QVBoxLayout(self.widget_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.register_btn = QPushButton(self.widget_3)
        self.register_btn.setObjectName(u"register_btn")
        sizePolicy4.setHeightForWidth(self.register_btn.sizePolicy().hasHeightForWidth())
        self.register_btn.setSizePolicy(sizePolicy4)
        self.register_btn.setMaximumSize(QSize(125, 50))
        font4 = QFont()
        font4.setPointSize(18)
        self.register_btn.setFont(font4)
        self.register_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.register_btn.setLayoutDirection(Qt.LeftToRight)

        self.register_btn.clicked.connect(self.register)
        self.verticalLayout_9.addWidget(self.register_btn)


        self.verticalLayout_8.addWidget(self.widget_3, 0, Qt.AlignHCenter)

        self.main_pages.addWidget(self.B1_page)
        self.Setting_page = QWidget()
        self.Setting_page.setObjectName(u"Setting_page")
        self.label_5 = QLabel(self.Setting_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(430, 200, 281, 111))
        self.label_5.setFont(font1)
        self.main_pages.addWidget(self.Setting_page)
        self.Help_page = QWidget()
        self.Help_page.setObjectName(u"Help_page")
        self.label_6 = QLabel(self.Help_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(430, 180, 171, 121))
        self.label_6.setFont(font1)
        self.main_pages.addWidget(self.Help_page)
        self.B2_page = QWidget()
        self.B2_page.setObjectName(u"B2_page")
        self.label_3 = QLabel(self.B2_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(420, 180, 231, 121))
        self.label_3.setFont(font1)
        self.main_pages.addWidget(self.B2_page)

        self.verticalLayout_4.addWidget(self.main_pages)


        self.horizontalLayout.addWidget(self.content)


        self.verticalLayout.addWidget(self.Body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.main_pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def register(self):
        n=self.name.text()
        id_=int(self.id.text())
        ge=self.gender.text()
        phno=int(self.pno.text())
        data(n,id_,phno,ge)
        
        self.name.clear()
        self.id.clear()
        self.gender.clear()
        self.pno.clear()
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"FACE RECOGNITION ATTENDANCE SYSTEM", None))
        self.home_btn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.Register_Student.setText(QCoreApplication.translate("MainWindow", u"Register Student", None))
        self.B2.setText(QCoreApplication.translate("MainWindow", u"B2", None))
        self.Help.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.Settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"STUDENT DETAILS", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Student Name:", None))
        self.name.setText("")
        self.name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Student ID:", None))
        self.id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Id", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Gender:", None))
        self.gender.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Phone Number:", None))
        self.pno.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.register_btn.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"PAGE 3", None))
    # retranslateUi

