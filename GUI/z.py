# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pageEaKZIB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

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
        MainWindow.resize(2234, 1006)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(400, 50))
        MainWindow.setStyleSheet(u"*{\n"
"border:none;\n"
"background-color:transparent;\n"
"background: transparent;\n"
"padding: 0;\n"
"margin: 0;\n"
"color: #fff;\n"
"}\n"
"#centralwidget{\n"
"	border-image: url(:/newPrefix/2.JPG);\n"
"}\n"
"#widget_2,#a,#b,#c,#d,#a_2,#b_2,#c_2,#widget_7,#widget_9,#widget_10,#widget_11,#widget_13,#widget_15,#widget_18,#widget_19{\n"
"background-color: rgba(190,190,190,190);\n"
"}\n"
"\n"
"#Body{\n"
"background-color:rgba(0, 0, 0,80);;\n"
"}\n"
"QLabel{\n"
"color:rgb(0, 0, 0);\n"
"}\n"
"#label_2{\n"
"color:rgb(255,255,255)\n"
"}\n"
"QPushButton{\n"
"text-align:left;\n"
"padding:5px 10px;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius:10px;\n"
"background-color:rgba(0, 0, 0,80);\n"
"}\n"
"#home_btn{\n"
"border-left: 3px solid rgb(255, 0, 0);\n"
"font-weight: bold\n"
"}\n"
"QLineEdit,QDateEdit,QComboBox{\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"color: rgb(0, 0, 0);\n"
"padding-left:20px;\n"
"padding-right:20px;\n"
"backgrounnd-color: rgb(34,36,44);\n"
"}\n"
"QDateE"
                        "dit QAbstractItemView:enabled{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 30, 94);\n"
"selection-background-color: rgb(131, 131, 131);\n"
"alternate-background-color: rgb(0, 9, 67);\n"
"\n"
"font-size:15px;\n"
"width:100px;\n"
"icon-size:35px,35px;\n"
"}\n"
"QDateEdit:hover{\n"
"border:2px solid rgb(0,0,0);}\n"
"QComboBox:hover{\n"
"border:2px solid rgb(0,0,0);}\n"
"QLineEdit:hover{\n"
"border:2px solid rgb(0,0,0);}\n"
"QlineEdit:focus{\n"
"border: 2px solid rgb(251, 255, 0);\n"
"background-color:rgb(43,45,56);\n"
"}\n"
"#register_btn{\n"
"text-align:center;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"color: rgb(0,0,0);\n"
"}\n"
"#register_btn:hover{\n"
"text-align:center;\n"
"background-color: rgb(0,0,0);\n"
"border-radius:10px;\n"
"color: rgb(255,255,255);\n"
"}\n"
"#Display,#Delete,#Update,#logout,#la,#ra,#Update_attd,#Excel_1,#Excel_2,#Excel_3,#Excel_4,#Excel_5{\n"
"text-align:center;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:25px;\n"
"color: rgb"
                        "(0,0,0);\n"
"}\n"
"#Display:hover{\n"
"text-align:center;\n"
"background-color: rgb(0,0,0);\n"
"border-radius:25px;\n"
"color: rgb(255,255,255);\n"
"}\n"
"#Delete:hover{\n"
"text-align:center;\n"
"background-color: rgb(0,0,0);\n"
"border-radius:25px;\n"
"color: rgb(255,255,255);\n"
"}\n"
"#Update:hover{\n"
"text-align:center;\n"
"background-color: rgb(0,0,0);\n"
"border-radius:25px;\n"
"color: rgb(255,255,255);\n"
"}\n"
"#logout:hover{\n"
"text-align:center;\n"
"background-color: rgb(0,0,0);\n"
"border-radius:25px;\n"
"color: rgb(255,255,255);\n"
"}\n"
"#la:hover{\n"
"text-align:center;\n"
"background-color: rgb(0,0,0);\n"
"border-radius:25px;\n"
"color: rgb(255,255,255);\n"
"}\n"
"#ra:hover{\n"
"text-align:center;\n"
"background-color: rgb(0,0,0);\n"
"border-radius:25px;\n"
"color: rgb(255,255,255);\n"
"}\n"
"#Update_attd:hover{\n"
"text-align:center;\n"
"background-color: rgb(0,0,0);\n"
"border-radius:25px;\n"
"color: rgb(255,255,255);\n"
"}\n"
"#Excel_1:hover{\n"
"text-align:center;\n"
"background-color: rg"
                        "b(0,0,0);\n"
"border-radius:25px;\n"
"color: rgb(255,255,255);\n"
"}\n"
"#Excel_2:hover{\n"
"text-align:center;\n"
"background-color: rgb(0,0,0);\n"
"border-radius:25px;\n"
"color: rgb(255,255,255);\n"
"}\n"
"#Excel_3:hover{\n"
"text-align:center;\n"
"background-color: rgb(0,0,0);\n"
"border-radius:25px;\n"
"color: rgb(255,255,255);\n"
"}\n"
"#Excel_4:hover{\n"
"text-align:center;\n"
"background-color: rgb(0,0,0);\n"
"border-radius:25px;\n"
"color: rgb(255,255,255);\n"
"}\n"
"#Excel_5:hover{\n"
"text-align:center;\n"
"background-color: rgb(0,0,0);\n"
"border-radius:25px;\n"
"color: rgb(255,255,255);\n"
"}\n"
"#T_name,#T_Ph,#T_ID,#Cls_ID{\n"
"border:3px solid rgb(255,255, 255);\n"
"border-radius:25px;\n"
"background-color: rgb(184, 184, 184);}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Title = QWidget(self.centralwidget)
        self.Title.setObjectName(u"Title")
        self.horizontalLayout_3 = QHBoxLayout(self.Title)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_6 = QFrame(self.Title)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.horizontalLayout_3.addWidget(self.frame_6, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_2 = QLabel(self.Title)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamily(u"BlackChancery")
        font.setPointSize(45)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_2.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.logout = QPushButton(self.Title)
        self.logout.setObjectName(u"logout")
        self.logout.setMinimumSize(QSize(100, 50))
        font1 = QFont()
        font1.setFamily(u"white allies")
        font1.setPointSize(19)
        self.logout.setFont(font1)
        icon = QIcon()
        icon.addFile(u"l.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logout.setIcon(icon)
        self.logout.setIconSize(QSize(36, 36))

        self.horizontalLayout_3.addWidget(self.logout, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.Title)

        self.Body = QWidget(self.centralwidget)
        self.Body.setObjectName(u"Body")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Body.sizePolicy().hasHeightForWidth())
        self.Body.setSizePolicy(sizePolicy2)
        self.horizontalLayout = QHBoxLayout(self.Body)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 9, 9, 9)
        self.left_menu = QCustomSlideMenu(self.Body)
        self.left_menu.setObjectName(u"left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.left_menu.sizePolicy().hasHeightForWidth())
        self.left_menu.setSizePolicy(sizePolicy3)
        self.left_menu.setMinimumSize(QSize(200, 0))
        self.left_menu.setCursor(QCursor(Qt.ArrowCursor))
        self.left_menu.setStyleSheet(u"#left_menu{\n"
"background-color: rgba(180, 180, 180,127);\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.left_menu)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 0, 0, 0)
        self.widget = QWidget(self.left_menu)
        self.widget.setObjectName(u"widget")
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
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
        font2 = QFont()
        font2.setFamily(u"Maiandra GD")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.home_btn.setFont(font2)
        self.home_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.home_btn)

        self.Register_Student = QPushButton(self.frame)
        self.Register_Student.setObjectName(u"Register_Student")
        font3 = QFont()
        font3.setFamily(u"Maiandra GD")
        font3.setPointSize(12)
        self.Register_Student.setFont(font3)
        self.Register_Student.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.Register_Student)

        self.Class_Details = QPushButton(self.frame)
        self.Class_Details.setObjectName(u"Class_Details")
        self.Class_Details.setFont(font3)
        self.Class_Details.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.Class_Details)

        self.Attd_verify_Uptd = QPushButton(self.frame)
        self.Attd_verify_Uptd.setObjectName(u"Attd_verify_Uptd")
        self.Attd_verify_Uptd.setMinimumSize(QSize(0, 29))
        font4 = QFont()
        font4.setFamily(u"Maiandra GD")
        font4.setPointSize(10)
        self.Attd_verify_Uptd.setFont(font4)

        self.verticalLayout_7.addWidget(self.Attd_verify_Uptd)


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
        self.Help.setFont(font3)
        self.Help.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.Help)

        self.Settings = QPushButton(self.frame_2)
        self.Settings.setObjectName(u"Settings")
        self.Settings.setEnabled(True)
        self.Settings.setFont(font3)
        self.Settings.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.Settings)


        self.verticalLayout_6.addWidget(self.frame_2)


        self.verticalLayout_5.addWidget(self.widget)


        self.horizontalLayout.addWidget(self.left_menu)

        self.content = QWidget(self.Body)
        self.content.setObjectName(u"content")
        self.verticalLayout_4 = QVBoxLayout(self.content)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.main_pages = QCustomStackedWidget(self.content)
        self.main_pages.setObjectName(u"main_pages")
        font5 = QFont()
        font5.setPointSize(18)
        self.main_pages.setFont(font5)
        self.main_pages.setFrameShadow(QFrame.Sunken)
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.Home.setStyleSheet(u"")
        self.widget_3 = QWidget(self.Home)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(0, 0, 2031, 1501))
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy4)
        self.widget_3.setMinimumSize(QSize(1000, 1500))
        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(0, 0, 1831, 100))
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy5)
        self.widget_4.setMinimumSize(QSize(1000, 100))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setSpacing(9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.horizontalLayout_4.setContentsMargins(3, 3, -1, -1)
        self.T_name = QWidget(self.widget_4)
        self.T_name.setObjectName(u"T_name")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.T_name.sizePolicy().hasHeightForWidth())
        self.T_name.setSizePolicy(sizePolicy6)
        self.T_name.setMinimumSize(QSize(500, 0))
        self.T_name.setMaximumSize(QSize(300, 100))
        self.Tname = QLabel(self.T_name)
        self.Tname.setObjectName(u"Tname")
        self.Tname.setGeometry(QRect(10, 17, 481, 51))
        font6 = QFont()
        font6.setFamily(u"Maiandra GD")
        font6.setPointSize(20)
        self.Tname.setFont(font6)

        self.horizontalLayout_4.addWidget(self.T_name)

        self.T_ID = QWidget(self.widget_4)
        self.T_ID.setObjectName(u"T_ID")
        sizePolicy6.setHeightForWidth(self.T_ID.sizePolicy().hasHeightForWidth())
        self.T_ID.setSizePolicy(sizePolicy6)
        self.T_ID.setMinimumSize(QSize(300, 0))
        self.T_ID.setMaximumSize(QSize(300, 100))
        self.Tid = QLabel(self.T_ID)
        self.Tid.setObjectName(u"Tid")
        self.Tid.setGeometry(QRect(10, 17, 281, 51))
        self.Tid.setFont(font6)

        self.horizontalLayout_4.addWidget(self.T_ID)

        self.Cls_ID = QWidget(self.widget_4)
        self.Cls_ID.setObjectName(u"Cls_ID")
        sizePolicy6.setHeightForWidth(self.Cls_ID.sizePolicy().hasHeightForWidth())
        self.Cls_ID.setSizePolicy(sizePolicy6)
        self.Cls_ID.setMinimumSize(QSize(175, 0))
        self.Cls_ID.setMaximumSize(QSize(200, 100))
        self.Cid = QLabel(self.Cls_ID)
        self.Cid.setObjectName(u"Cid")
        self.Cid.setGeometry(QRect(10, 17, 351, 51))
        self.Cid.setFont(font6)

        self.horizontalLayout_4.addWidget(self.Cls_ID)

        self.T_Ph = QWidget(self.widget_4)
        self.T_Ph.setObjectName(u"T_Ph")
        sizePolicy6.setHeightForWidth(self.T_Ph.sizePolicy().hasHeightForWidth())
        self.T_Ph.setSizePolicy(sizePolicy6)
        self.T_Ph.setMinimumSize(QSize(375, 0))
        self.T_Ph.setMaximumSize(QSize(300, 100))
        self.TPh = QLabel(self.T_Ph)
        self.TPh.setObjectName(u"TPh")
        self.TPh.setGeometry(QRect(10, 17, 361, 51))
        self.TPh.setFont(font6)

        self.horizontalLayout_4.addWidget(self.T_Ph)

        self.widget_6 = QWidget(self.widget_3)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(0, 100, 1721, 800))
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setMinimumSize(QSize(0, 500))
        self.widget_6.setMaximumSize(QSize(16777215, 16777215))
        self.widget_6.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.widget_6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.a_2 = QWidget(self.widget_6)
        self.a_2.setObjectName(u"a_2")
        self.a_2.setMaximumSize(QSize(500, 16777215))
        self.calendar = QCalendarWidget(self.a_2)
        self.calendar.setObjectName(u"calendar")
        self.calendar.setGeometry(QRect(0, 0, 501, 351))
        font7 = QFont()
        font7.setFamily(u"Maiandra GD")
        self.calendar.setFont(font7)
        self.calendar.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 30, 94);\n"
"selection-background-color: rgb(131, 131, 131);\n"
"alternate-background-color: rgb(0, 9, 67);\n"
"\n"
"font-size:15px;\n"
"width:100px;\n"
"icon-size:35px,35px;")
        self.calendar.setFirstDayOfWeek(Qt.Sunday)
        self.calendar.setGridVisible(False)
        self.calendar.setHorizontalHeaderFormat(QCalendarWidget.ShortDayNames)
        self.calendar.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)

        self.gridLayout_2.addWidget(self.a_2, 0, 0, 1, 1)

        self.b_2 = QWidget(self.widget_6)
        self.b_2.setObjectName(u"b_2")
        self.b_2.setMaximumSize(QSize(16777215, 350))
        self.cls_attd = QTableWidget(self.b_2)
        if (self.cls_attd.columnCount() < 6):
            self.cls_attd.setColumnCount(6)
        self.cls_attd.setObjectName(u"cls_attd")
        self.cls_attd.setGeometry(QRect(80, 30, 1091, 251))
        font8 = QFont()
        font8.setFamily(u"Maiandra GD")
        font8.setPointSize(20)
        font8.setBold(False)
        font8.setItalic(False)
        font8.setWeight(50)
        self.cls_attd.setFont(font8)
        self.cls_attd.setStyleSheet(u"*{\n"
"color: rgb(0, 0, 0);\n"
"font: 20pt \"Maiandra GD\";}")
        self.cls_attd.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.cls_attd.setRowCount(0)
        self.cls_attd.setColumnCount(6)
        self.Tname_2 = QLabel(self.b_2)
        self.Tname_2.setObjectName(u"Tname_2")
        self.Tname_2.setGeometry(QRect(480, -10, 201, 51))
        font9 = QFont()
        font9.setFamily(u"Maiandra GD")
        font9.setPointSize(17)
        self.Tname_2.setFont(font9)
        self.Excel_1 = QPushButton(self.b_2)
        self.Excel_1.setObjectName(u"Excel_1")
        self.Excel_1.setGeometry(QRect(490, 300, 125, 50))
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.Excel_1.sizePolicy().hasHeightForWidth())
        self.Excel_1.setSizePolicy(sizePolicy7)
        self.Excel_1.setMaximumSize(QSize(125, 50))
        font10 = QFont()
        font10.setFamily(u"white allies")
        font10.setPointSize(13)
        self.Excel_1.setFont(font10)
        self.Excel_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.Excel_1.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_2.addWidget(self.b_2, 0, 1, 1, 1)

        self.d_2 = QWidget(self.widget_6)
        self.d_2.setObjectName(u"d_2")
        self.widget_7 = QWidget(self.d_2)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(0, 0, 821, 391))
        self.sub_attd = QTableWidget(self.widget_7)
        if (self.sub_attd.columnCount() < 7):
            self.sub_attd.setColumnCount(7)
        self.sub_attd.setObjectName(u"sub_attd")
        self.sub_attd.setGeometry(QRect(10, 60, 811, 271))
        font11 = QFont()
        font11.setFamily(u"Maiandra GD")
        font11.setPointSize(12)
        font11.setBold(False)
        font11.setItalic(False)
        font11.setWeight(50)
        self.sub_attd.setFont(font11)
        self.sub_attd.setStyleSheet(u"*{\n"
"color: rgb(0, 0, 0);\n"
"font: 12pt \"Maiandra GD\";}\n"
"")
        self.sub_attd.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.sub_attd.setRowCount(0)
        self.sub_attd.setColumnCount(7)
        self.subattd = QLabel(self.widget_7)
        self.subattd.setObjectName(u"subattd")
        self.subattd.setGeometry(QRect(250, 0, 291, 51))
        self.subattd.setFont(font9)
        self.Excel_2 = QPushButton(self.widget_7)
        self.Excel_2.setObjectName(u"Excel_2")
        self.Excel_2.setGeometry(QRect(320, 340, 125, 50))
        sizePolicy7.setHeightForWidth(self.Excel_2.sizePolicy().hasHeightForWidth())
        self.Excel_2.setSizePolicy(sizePolicy7)
        self.Excel_2.setMaximumSize(QSize(125, 50))
        self.Excel_2.setFont(font10)
        self.Excel_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.Excel_2.setLayoutDirection(Qt.LeftToRight)
        self.widget_9 = QWidget(self.d_2)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setGeometry(QRect(830, 0, 871, 391))
        self.date_attd = QTableWidget(self.widget_9)
        if (self.date_attd.columnCount() < 7):
            self.date_attd.setColumnCount(7)
        self.date_attd.setObjectName(u"date_attd")
        self.date_attd.setGeometry(QRect(20, 50, 881, 281))
        self.date_attd.setFont(font11)
        self.date_attd.setStyleSheet(u"*{\n"
"color: rgb(0, 0, 0);\n"
"font: 12pt \"Maiandra GD\";}\n"
"")
        self.date_attd.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.date_attd.setRowCount(0)
        self.date_attd.setColumnCount(7)
        self.Tname_4 = QLabel(self.widget_9)
        self.Tname_4.setObjectName(u"Tname_4")
        self.Tname_4.setGeometry(QRect(260, 0, 291, 51))
        self.Tname_4.setFont(font9)
        self.Excel_3 = QPushButton(self.widget_9)
        self.Excel_3.setObjectName(u"Excel_3")
        self.Excel_3.setGeometry(QRect(360, 340, 125, 50))
        sizePolicy7.setHeightForWidth(self.Excel_3.sizePolicy().hasHeightForWidth())
        self.Excel_3.setSizePolicy(sizePolicy7)
        self.Excel_3.setMaximumSize(QSize(125, 50))
        self.Excel_3.setFont(font10)
        self.Excel_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.Excel_3.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_2.addWidget(self.d_2, 1, 0, 1, 2)

        self.main_pages.addWidget(self.Home)
        self.Register_Student_Page = QWidget()
        self.Register_Student_Page.setObjectName(u"Register_Student_Page")
        self.verticalLayout_8 = QVBoxLayout(self.Register_Student_Page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_2 = QWidget(self.Register_Student_Page)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy8)
        self.widget_2.setMinimumSize(QSize(1000, 100))
        self.verticalLayout_9 = QVBoxLayout(self.widget_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.sub_title = QWidget(self.widget_2)
        self.sub_title.setObjectName(u"sub_title")
        self.sub_title.setMinimumSize(QSize(700, 0))
        self.sub_title.setMaximumSize(QSize(350, 16777215))
        self.formLayout = QFormLayout(self.sub_title)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.formLayout.setLabelAlignment(Qt.AlignCenter)
        self.formLayout.setFormAlignment(Qt.AlignCenter)
        self.formLayout.setHorizontalSpacing(3)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setContentsMargins(0, 0, -1, 0)
        self.label_10 = QLabel(self.sub_title)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMaximumSize(QSize(16777215, 50))
        font12 = QFont()
        font12.setFamily(u"Maiandra GD")
        font12.setPointSize(27)
        self.label_10.setFont(font12)
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_10)

        self.label_4 = QLabel(self.sub_title)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(200, 0))
        self.label_4.setMaximumSize(QSize(213, 16777215))
        font13 = QFont()
        font13.setFamily(u"Maiandra GD")
        font13.setPointSize(25)
        self.label_4.setFont(font13)
        self.label_4.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.name = QLineEdit(self.sub_title)
        self.name.setObjectName(u"name")
        sizePolicy.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy)
        self.name.setMaximumSize(QSize(16777215, 50))
        self.name.setFont(font6)
        self.name.setFrame(True)
        self.name.setCursorPosition(0)
        self.name.setClearButtonEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.name)

        self.label_7 = QLabel(self.sub_title)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QSize(225, 0))
        self.label_7.setFont(font13)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_7)

        self.id = QLineEdit(self.sub_title)
        self.id.setObjectName(u"id")
        sizePolicy.setHeightForWidth(self.id.sizePolicy().hasHeightForWidth())
        self.id.setSizePolicy(sizePolicy)
        self.id.setMaximumSize(QSize(16777215, 50))
        self.id.setFont(font6)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.id)

        self.label_8 = QLabel(self.sub_title)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QSize(225, 0))
        self.label_8.setFont(font13)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_8)

        self.comboBox = QComboBox(self.sub_title)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaximumSize(QSize(16777215, 50))
        self.comboBox.setFont(font13)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.comboBox)

        self.label_9 = QLabel(self.sub_title)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setFont(font13)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_9)

        self.pno = QLineEdit(self.sub_title)
        self.pno.setObjectName(u"pno")
        sizePolicy.setHeightForWidth(self.pno.sizePolicy().hasHeightForWidth())
        self.pno.setSizePolicy(sizePolicy)
        self.pno.setMaximumSize(QSize(16777215, 50))
        self.pno.setFont(font6)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.pno)

        self.label_6 = QLabel(self.sub_title)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(0, 0))
        self.label_6.setMaximumSize(QSize(400, 16777215))
        self.label_6.setFont(font13)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.dateEdit_2 = QDateEdit(self.sub_title)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setMaximumSize(QSize(16777215, 50))
        self.dateEdit_2.setFont(font13)
        self.dateEdit_2.setCurrentSection(QDateTimeEdit.DaySection)
        self.dateEdit_2.setCalendarPopup(True)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.dateEdit_2)

        self.label_5 = QLabel(self.sub_title)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(225, 0))
        self.label_5.setFont(font13)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_5)

        self.password = QLineEdit(self.sub_title)
        self.password.setObjectName(u"password")
        self.password.setMaximumSize(QSize(16777215, 50))
        self.password.setFont(font6)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.password)

        self.register_btn = QPushButton(self.sub_title)
        self.register_btn.setObjectName(u"register_btn")
        sizePolicy7.setHeightForWidth(self.register_btn.sizePolicy().hasHeightForWidth())
        self.register_btn.setSizePolicy(sizePolicy7)
        self.register_btn.setMaximumSize(QSize(125, 50))
        font14 = QFont()
        font14.setFamily(u"white allies")
        font14.setPointSize(24)
        self.register_btn.setFont(font14)
        self.register_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.register_btn.setLayoutDirection(Qt.LeftToRight)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.register_btn)

        self.label_11 = QLabel(self.sub_title)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 50))
        font15 = QFont()
        font15.setFamily(u"Maiandra GD")
        font15.setPointSize(14)
        self.label_11.setFont(font15)
        self.label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.label_11)

        self.iv = QLabel(self.sub_title)
        self.iv.setObjectName(u"iv")
        self.iv.setMaximumSize(QSize(16777215, 50))
        font16 = QFont()
        font16.setFamily(u"Maiandra GD")
        font16.setPointSize(16)
        self.iv.setFont(font16)
        self.iv.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(7, QFormLayout.SpanningRole, self.iv)


        self.verticalLayout_9.addWidget(self.sub_title, 0, Qt.AlignHCenter)


        self.verticalLayout_8.addWidget(self.widget_2)

        self.main_pages.addWidget(self.Register_Student_Page)
        self.Class_Details_Page = QWidget()
        self.Class_Details_Page.setObjectName(u"Class_Details_Page")
        sizePolicy.setHeightForWidth(self.Class_Details_Page.sizePolicy().hasHeightForWidth())
        self.Class_Details_Page.setSizePolicy(sizePolicy)
        self.widget_5 = QWidget(self.Class_Details_Page)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(25, 0, 1600, 850))
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setMinimumSize(QSize(0, 850))
        self.widget_5.setMaximumSize(QSize(16777215, 16777215))
        self.widget_5.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.widget_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.c = QWidget(self.widget_5)
        self.c.setObjectName(u"c")
        self.label_19 = QLabel(self.c)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(260, 20, 462, 50))
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setMaximumSize(QSize(16777215, 50))
        self.label_19.setFont(font12)
        self.label_19.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.tableWidget_2 = QTableWidget(self.c)
        if (self.tableWidget_2.columnCount() < 5):
            self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(120, 70, 561, 291))
        self.tableWidget_2.setStyleSheet(u"*{\n"
"color: rgb(0, 0, 0);\n"
"font: 15pt \"Maiandra GD\";}\n"
"")
        self.tableWidget_2.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setColumnCount(5)
        self.Excel_5 = QPushButton(self.c)
        self.Excel_5.setObjectName(u"Excel_5")
        self.Excel_5.setGeometry(QRect(300, 370, 125, 50))
        sizePolicy7.setHeightForWidth(self.Excel_5.sizePolicy().hasHeightForWidth())
        self.Excel_5.setSizePolicy(sizePolicy7)
        self.Excel_5.setMaximumSize(QSize(125, 50))
        self.Excel_5.setFont(font10)
        self.Excel_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.Excel_5.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.c, 1, 0, 1, 1)

        self.a = QWidget(self.widget_5)
        self.a.setObjectName(u"a")
        self.a.setMaximumSize(QSize(1600, 16777215))
        self.Display = QPushButton(self.a)
        self.Display.setObjectName(u"Display")
        self.Display.setGeometry(QRect(260, 10, 245, 50))
        sizePolicy9 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.Display.sizePolicy().hasHeightForWidth())
        self.Display.setSizePolicy(sizePolicy9)
        self.Display.setMinimumSize(QSize(245, 50))
        self.Display.setMaximumSize(QSize(100, 16777215))
        font17 = QFont()
        font17.setFamily(u"white allies")
        font17.setPointSize(16)
        font17.setBold(False)
        font17.setWeight(50)
        self.Display.setFont(font17)
        self.Display.setCursor(QCursor(Qt.PointingHandCursor))
        self.tableWidget = QTableWidget(self.a)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(170, 70, 561, 281))
        self.tableWidget.setStyleSheet(u"*{\n"
"color: rgb(0, 0, 0);\n"
"font: 15pt \"Maiandra GD\";}\n"
"")
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(4)
        self.Excel_4 = QPushButton(self.a)
        self.Excel_4.setObjectName(u"Excel_4")
        self.Excel_4.setGeometry(QRect(300, 370, 125, 50))
        sizePolicy7.setHeightForWidth(self.Excel_4.sizePolicy().hasHeightForWidth())
        self.Excel_4.setSizePolicy(sizePolicy7)
        self.Excel_4.setMaximumSize(QSize(125, 50))
        font18 = QFont()
        font18.setFamily(u"white allies")
        font18.setPointSize(12)
        self.Excel_4.setFont(font18)
        self.Excel_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.Excel_4.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.a, 0, 0, 1, 1)

        self.b = QWidget(self.widget_5)
        self.b.setObjectName(u"b")
        self.label_12 = QLabel(self.b)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(72, 130, 225, 50))
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QSize(225, 0))
        self.label_12.setFont(font13)
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.id_2 = QLineEdit(self.b)
        self.id_2.setObjectName(u"id_2")
        self.id_2.setGeometry(QRect(300, 130, 462, 50))
        sizePolicy.setHeightForWidth(self.id_2.sizePolicy().hasHeightForWidth())
        self.id_2.setSizePolicy(sizePolicy)
        self.id_2.setMaximumSize(QSize(16777215, 50))
        self.id_2.setFont(font6)
        self.label_13 = QLabel(self.b)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(72, 200, 225, 50))
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QSize(225, 0))
        font19 = QFont()
        font19.setFamily(u"Maiandra GD")
        font19.setPointSize(18)
        self.label_13.setFont(font19)
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.New_phno = QLineEdit(self.b)
        self.New_phno.setObjectName(u"New_phno")
        self.New_phno.setGeometry(QRect(300, 200, 462, 50))
        sizePolicy.setHeightForWidth(self.New_phno.sizePolicy().hasHeightForWidth())
        self.New_phno.setSizePolicy(sizePolicy)
        self.New_phno.setMaximumSize(QSize(16777215, 50))
        self.New_phno.setFont(font6)
        self.label_14 = QLabel(self.b)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(210, 30, 462, 50))
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMaximumSize(QSize(16777215, 50))
        self.label_14.setFont(font12)
        self.label_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Update = QPushButton(self.b)
        self.Update.setObjectName(u"Update")
        self.Update.setGeometry(QRect(310, 319, 200, 51))
        sizePolicy9.setHeightForWidth(self.Update.sizePolicy().hasHeightForWidth())
        self.Update.setSizePolicy(sizePolicy9)
        self.Update.setMinimumSize(QSize(0, 50))
        self.Update.setMaximumSize(QSize(200, 16777215))
        font20 = QFont()
        font20.setFamily(u"white allies")
        font20.setPointSize(22)
        self.Update.setFont(font20)
        self.Update.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_15 = QLabel(self.b)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(300, 260, 462, 50))
        self.label_15.setMaximumSize(QSize(16777215, 50))
        self.label_15.setFont(font15)
        self.label_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.b, 0, 1, 1, 1)

        self.d = QWidget(self.widget_5)
        self.d.setObjectName(u"d")
        self.label_16 = QLabel(self.d)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(180, 50, 462, 50))
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setMaximumSize(QSize(16777215, 50))
        self.label_16.setFont(font12)
        self.label_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_17 = QLabel(self.d)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(270, 230, 462, 50))
        self.label_17.setMaximumSize(QSize(16777215, 50))
        self.label_17.setFont(font15)
        self.label_17.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_18 = QLabel(self.d)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(42, 150, 225, 50))
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setMinimumSize(QSize(225, 0))
        self.label_18.setFont(font13)
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.id_3 = QLineEdit(self.d)
        self.id_3.setObjectName(u"id_3")
        self.id_3.setGeometry(QRect(270, 150, 462, 50))
        sizePolicy.setHeightForWidth(self.id_3.sizePolicy().hasHeightForWidth())
        self.id_3.setSizePolicy(sizePolicy)
        self.id_3.setMaximumSize(QSize(16777215, 50))
        self.id_3.setFont(font6)
        self.Delete = QPushButton(self.d)
        self.Delete.setObjectName(u"Delete")
        self.Delete.setGeometry(QRect(280, 299, 200, 51))
        sizePolicy9.setHeightForWidth(self.Delete.sizePolicy().hasHeightForWidth())
        self.Delete.setSizePolicy(sizePolicy9)
        self.Delete.setMinimumSize(QSize(0, 50))
        self.Delete.setMaximumSize(QSize(200, 16777215))
        font21 = QFont()
        font21.setFamily(u"white allies")
        font21.setPointSize(23)
        self.Delete.setFont(font21)
        self.Delete.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.d, 1, 1, 1, 1)

        self.main_pages.addWidget(self.Class_Details_Page)
        self.Attd_Verify_Uptd_page = QWidget()
        self.Attd_Verify_Uptd_page.setObjectName(u"Attd_Verify_Uptd_page")
        self.widget_8 = QWidget(self.Attd_Verify_Uptd_page)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(-1, -1, 1961, 861))
        self.widget_10 = QWidget(self.widget_8)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setGeometry(QRect(0, 0, 1951, 80))
        self.Attd_verify = QLabel(self.widget_10)
        self.Attd_verify.setObjectName(u"Attd_verify")
        self.Attd_verify.setGeometry(QRect(540, 20, 851, 41))
        font22 = QFont()
        font22.setFamily(u"Maiandra GD")
        font22.setPointSize(32)
        self.Attd_verify.setFont(font22)
        self.widget_11 = QWidget(self.widget_8)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setGeometry(QRect(0, 90, 981, 651))
        self.widget_12 = QWidget(self.widget_11)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setGeometry(QRect(10, 90, 951, 551))
        self.pic = QLabel(self.widget_12)
        self.pic.setObjectName(u"pic")
        self.pic.setGeometry(QRect(-4, 2, 951, 551))
        self.Cls_Visuals = QLabel(self.widget_11)
        self.Cls_Visuals.setObjectName(u"Cls_Visuals")
        self.Cls_Visuals.setGeometry(QRect(320, 30, 221, 31))
        self.Cls_Visuals.setFont(font13)
        self.filename = QLabel(self.widget_11)
        self.filename.setObjectName(u"filename")
        self.filename.setGeometry(QRect(550, 30, 221, 31))
        self.filename.setFont(font13)
        self.widget_13 = QWidget(self.widget_8)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setGeometry(QRect(0, 750, 981, 175))
        self.widget_13.setMinimumSize(QSize(981, 175))
        font23 = QFont()
        font23.setItalic(False)
        self.widget_13.setFont(font23)
        self.ra = QPushButton(self.widget_13)
        self.ra.setObjectName(u"ra")
        self.ra.setGeometry(QRect(620, 30, 150, 50))
        self.ra.setMinimumSize(QSize(150, 50))
        font24 = QFont()
        font24.setFamily(u"white allies")
        font24.setPointSize(25)
        font24.setBold(False)
        font24.setWeight(50)
        self.ra.setFont(font24)
        self.pic_cnt = QLabel(self.widget_13)
        self.pic_cnt.setObjectName(u"pic_cnt")
        self.pic_cnt.setGeometry(QRect(500, 50, 321, 20))
        font25 = QFont()
        font25.setFamily(u"Maiandra GD")
        font25.setPointSize(19)
        self.pic_cnt.setFont(font25)
        self.la = QPushButton(self.widget_13)
        self.la.setObjectName(u"la")
        self.la.setGeometry(QRect(280, 30, 150, 50))
        self.la.setMinimumSize(QSize(150, 50))
        font26 = QFont()
        font26.setFamily(u"white allies")
        font26.setPointSize(25)
        font26.setBold(False)
        font26.setItalic(False)
        font26.setWeight(50)
        self.la.setFont(font26)
        self.widget_15 = QWidget(self.widget_8)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setGeometry(QRect(990, 90, 941, 771))
        self.id_4 = QLineEdit(self.widget_15)
        self.id_4.setObjectName(u"id_4")
        self.id_4.setGeometry(QRect(228, 220, 311, 50))
        sizePolicy.setHeightForWidth(self.id_4.sizePolicy().hasHeightForWidth())
        self.id_4.setSizePolicy(sizePolicy)
        self.id_4.setMaximumSize(QSize(16777215, 50))
        self.id_4.setFont(font6)
        self.label_23 = QLabel(self.widget_15)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(200, 541, 462, 50))
        self.label_23.setMaximumSize(QSize(16777215, 50))
        self.label_23.setFont(font15)
        self.label_23.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Update_attd = QPushButton(self.widget_15)
        self.Update_attd.setObjectName(u"Update_attd")
        self.Update_attd.setGeometry(QRect(210, 600, 200, 51))
        sizePolicy9.setHeightForWidth(self.Update_attd.sizePolicy().hasHeightForWidth())
        self.Update_attd.setSizePolicy(sizePolicy9)
        self.Update_attd.setMinimumSize(QSize(0, 50))
        self.Update_attd.setMaximumSize(QSize(200, 16777215))
        font27 = QFont()
        font27.setFamily(u"white allies")
        font27.setPointSize(16)
        self.Update_attd.setFont(font27)
        self.Update_attd.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_20 = QLabel(self.widget_15)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(0, 220, 225, 50))
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setMinimumSize(QSize(225, 0))
        self.label_20.setFont(font13)
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_22 = QLabel(self.widget_15)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(30, 90, 531, 50))
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setMaximumSize(QSize(16777215, 50))
        self.label_22.setFont(font12)
        self.label_22.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.sub_menu = QComboBox(self.widget_15)
        self.sub_menu.setObjectName(u"sub_menu")
        self.sub_menu.setGeometry(QRect(230, 380, 311, 50))
        self.sub_menu.setFont(font6)
        self.sub_menu.setStyleSheet(u"")
        self.label_24 = QLabel(self.widget_15)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(-2, 381, 225, 50))
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setMinimumSize(QSize(225, 0))
        self.label_24.setFont(font13)
        self.label_24.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_25 = QLabel(self.widget_15)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(0, 470, 225, 50))
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        self.label_25.setMinimumSize(QSize(225, 0))
        self.label_25.setFont(font25)
        self.label_25.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_26 = QLabel(self.widget_15)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(0, 300, 225, 50))
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setMinimumSize(QSize(225, 0))
        self.label_26.setFont(font13)
        self.label_26.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dateEdit = QDateEdit(self.widget_15)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(230, 300, 311, 50))
        self.dateEdit.setFont(font7)
        self.dateEdit.setStyleSheet(u"font-size:20px;\n"
"")
        self.dateEdit.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.dateEdit.setCorrectionMode(QAbstractSpinBox.CorrectToPreviousValue)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QDate(2023, 3, 1))
        self.attd_status_menu = QComboBox(self.widget_15)
        self.attd_status_menu.setObjectName(u"attd_status_menu")
        self.attd_status_menu.setGeometry(QRect(230, 470, 311, 50))
        self.attd_status_menu.setFont(font6)
        self.attd_status_menu.setStyleSheet(u"")
        self.main_pages.addWidget(self.Attd_Verify_Uptd_page)
        self.Help_page = QWidget()
        self.Help_page.setObjectName(u"Help_page")
        self.widget_17 = QWidget(self.Help_page)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setGeometry(QRect(0, 0, 1931, 871))
        self.widget_19 = QWidget(self.widget_17)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setGeometry(QRect(250, 180, 1111, 471))
        self.widget_19.setStyleSheet(u"QPushButton{\n"
"text-align:left;\n"
"padding:5px 10px;\n"
"border-radius:50px;\n"
"background-color:rgb(255,255, 255);\n"
"color: rgb(0,0,0);\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"text-align:left;\n"
"background-color: rgb(0,0,0);\n"
"border-radius:25px;\n"
"color: rgb(255,255,255);\n"
"}")
        self.label_3 = QLabel(self.widget_19)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(460, 10, 311, 61))
        font28 = QFont()
        font28.setFamily(u"Maiandra GD")
        font28.setPointSize(36)
        self.label_3.setFont(font28)
        self.label_29 = QLabel(self.widget_19)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(20, 90, 251, 50))
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setMinimumSize(QSize(225, 0))
        self.label_29.setFont(font13)
        self.label_29.setAlignment(Qt.AlignCenter)
        self.label_30 = QLabel(self.widget_19)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(460, 90, 251, 50))
        sizePolicy.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy)
        self.label_30.setMinimumSize(QSize(225, 0))
        self.label_30.setFont(font13)
        self.label_30.setAlignment(Qt.AlignCenter)
        self.label_31 = QLabel(self.widget_19)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(850, 90, 251, 50))
        sizePolicy.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy)
        self.label_31.setMinimumSize(QSize(225, 0))
        self.label_31.setFont(font13)
        self.label_31.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.widget_19)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 140, 251, 101))
        font29 = QFont()
        font29.setFamily(u"Maiandra GD")
        font29.setPointSize(15)
        self.pushButton.setFont(font29)
        self.pushButton.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"call.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(45, 49))
        self.pushButton_2 = QPushButton(self.widget_19)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(20, 260, 251, 101))
        self.pushButton_2.setFont(font4)
        self.pushButton_2.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"m.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(42, 48))
        self.pushButton_3 = QPushButton(self.widget_19)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(460, 260, 251, 101))
        self.pushButton_3.setFont(font4)
        self.pushButton_3.setStyleSheet(u"")
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(42, 48))
        self.pushButton_5 = QPushButton(self.widget_19)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(850, 260, 251, 101))
        self.pushButton_5.setFont(font4)
        self.pushButton_5.setStyleSheet(u"")
        self.pushButton_5.setIcon(icon2)
        self.pushButton_5.setIconSize(QSize(42, 48))
        self.pushButton_4 = QPushButton(self.widget_19)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(460, 140, 251, 101))
        self.pushButton_4.setFont(font29)
        self.pushButton_4.setStyleSheet(u"")
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QSize(45, 49))
        self.pushButton_6 = QPushButton(self.widget_19)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(850, 140, 251, 101))
        self.pushButton_6.setFont(font29)
        self.pushButton_6.setStyleSheet(u"")
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setIconSize(QSize(45, 49))
        self.main_pages.addWidget(self.Help_page)
        self.Setting_page = QWidget()
        self.Setting_page.setObjectName(u"Setting_page")
        self.widget_16 = QWidget(self.Setting_page)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setGeometry(QRect(0, 10, 1931, 871))
        self.widget_18 = QWidget(self.widget_16)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setGeometry(QRect(260, 190, 1111, 471))
        self.label = QLabel(self.widget_18)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(520, 10, 311, 61))
        self.label.setFont(font28)
        self.label_21 = QLabel(self.widget_18)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(300, 130, 225, 50))
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setMinimumSize(QSize(225, 0))
        self.label_21.setFont(font13)
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sub_menu_2 = QComboBox(self.widget_18)
        self.sub_menu_2.setObjectName(u"sub_menu_2")
        self.sub_menu_2.setGeometry(QRect(550, 130, 311, 50))
        self.sub_menu_2.setFont(font6)
        self.sub_menu_2.setStyleSheet(u"")
        self.sub_menu_3 = QComboBox(self.widget_18)
        self.sub_menu_3.setObjectName(u"sub_menu_3")
        self.sub_menu_3.setGeometry(QRect(550, 200, 311, 50))
        self.sub_menu_3.setFont(font6)
        self.sub_menu_3.setStyleSheet(u"")
        self.label_27 = QLabel(self.widget_18)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(300, 200, 225, 50))
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        self.label_27.setMinimumSize(QSize(225, 0))
        self.label_27.setFont(font13)
        self.label_27.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sub_menu_4 = QComboBox(self.widget_18)
        self.sub_menu_4.setObjectName(u"sub_menu_4")
        self.sub_menu_4.setGeometry(QRect(550, 270, 311, 50))
        self.sub_menu_4.setFont(font6)
        self.sub_menu_4.setStyleSheet(u"")
        self.label_28 = QLabel(self.widget_18)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(244, 270, 281, 50))
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)
        self.label_28.setMinimumSize(QSize(225, 0))
        self.label_28.setFont(font13)
        self.label_28.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.main_pages.addWidget(self.Setting_page)

        self.verticalLayout_4.addWidget(self.main_pages)


        self.horizontalLayout.addWidget(self.content)

        self.widget_14 = QWidget(self.Body)
        self.widget_14.setObjectName(u"widget_14")

        self.horizontalLayout.addWidget(self.widget_14)


        self.verticalLayout.addWidget(self.Body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.main_pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Face Recognition Attendance System", None))
        self.logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.home_btn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.Register_Student.setText(QCoreApplication.translate("MainWindow", u"Register Student", None))
        self.Class_Details.setText(QCoreApplication.translate("MainWindow", u"Class Details", None))
        self.Attd_verify_Uptd.setText(QCoreApplication.translate("MainWindow", u"Attendance Verification and Updation", None))
        self.Help.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.Settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.Tname.setText(QCoreApplication.translate("MainWindow", u"Teacher Name: ABCDEFGHI", None))
        self.Tid.setText(QCoreApplication.translate("MainWindow", u"Teacher ID: xyz", None))
        self.Cid.setText(QCoreApplication.translate("MainWindow", u"Class ID: lmn", None))
        self.TPh.setText(QCoreApplication.translate("MainWindow", u" Phone Number: 0123456789", None))
        self.Tname_2.setText(QCoreApplication.translate("MainWindow", u"Class Attendance", None))
        self.Excel_1.setText(QCoreApplication.translate("MainWindow", u"Export to Excel", None))
        self.subattd.setText(QCoreApplication.translate("MainWindow", u"Subject-wise Attendance", None))
        self.Excel_2.setText(QCoreApplication.translate("MainWindow", u"Export to Excel", None))
        self.Tname_4.setText(QCoreApplication.translate("MainWindow", u"Attendance on 00/00/00", None))
        self.Excel_3.setText(QCoreApplication.translate("MainWindow", u"Export to Excel", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"STUDENT DETAILS", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Student Name:", None))
        self.name.setText("")
        self.name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Student ID:", None))
        self.id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Id", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Gender:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Phone Number:", None))
        self.pno.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"  Date Of Birth:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.register_btn.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Collecting Sample Photos", None))
        self.iv.setText(QCoreApplication.translate("MainWindow", u"Text", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"TIME TABLE", None))
        self.Excel_5.setText(QCoreApplication.translate("MainWindow", u"Export to Excel", None))
        self.Display.setText(QCoreApplication.translate("MainWindow", u"Display Student Details", None))
        self.Excel_4.setText(QCoreApplication.translate("MainWindow", u"Export to Excel", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Student ID:", None))
        self.id_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Id", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"New Phone Number", None))
        self.New_phno.setPlaceholderText(QCoreApplication.translate("MainWindow", u"New Phone Number", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"UPDATE STUDENT DETAILS", None))
        self.Update.setText(QCoreApplication.translate("MainWindow", u"Update Details", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Student Details Updated", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"DELETE STUDENT DETAILS", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Student Details Deleted", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Student ID:", None))
        self.id_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Id", None))
        self.Delete.setText(QCoreApplication.translate("MainWindow", u"Delete Details", None))
        self.Attd_verify.setText(QCoreApplication.translate("MainWindow", u"Attendance Verification & Updation", None))
        self.pic.setText("")
        self.Cls_Visuals.setText(QCoreApplication.translate("MainWindow", u"Class Visuals :-", None))
        self.filename.setText(QCoreApplication.translate("MainWindow", u"File_name", None))
        self.ra.setText(QCoreApplication.translate("MainWindow", u"Next ->", None))
        self.pic_cnt.setText(QCoreApplication.translate("MainWindow", u"1/3", None))
        self.la.setText(QCoreApplication.translate("MainWindow", u"<- Prev", None))
        self.id_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Id", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Student Attendance Updated", None))
        self.Update_attd.setText(QCoreApplication.translate("MainWindow", u"Update Attendance", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Student ID:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"UPDATE ATTENDANCE DETAILS", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Subject ID:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Attendance Status:", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Contact Us", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Alby Saji Luka", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Harisankar S.G.", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Vyshnav M.", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"+91 7736094476", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"albyluka02@gmail.com", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"harisankar4785@gmail.com", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"vyshnavmohan20@gmail.com", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"+91 6238574428", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"+91 7907745936", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Language:", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Theme:", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Background Image:", None))
    # retranslateUi

