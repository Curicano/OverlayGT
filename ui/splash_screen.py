# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Storage X\About\Programirovanie\Python\Git\OverlayGT 2.0\ui\splash_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        SplashScreen.setObjectName("SplashScreen")
        SplashScreen.resize(300, 300)
        SplashScreen.setMinimumSize(QtCore.QSize(300, 300))
        SplashScreen.setMaximumSize(QtCore.QSize(300, 300))
        self.centralwidget = QtWidgets.QWidget(SplashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.vL = QtWidgets.QVBoxLayout(self.centralwidget)
        self.vL.setContentsMargins(10, 10, 10, 10)
        self.vL.setSpacing(0)
        self.vL.setObjectName("vL")
        self.f_container = QtWidgets.QFrame(self.centralwidget)
        self.f_container.setObjectName("f_container")
        self.vL_2 = QtWidgets.QVBoxLayout(self.f_container)
        self.vL_2.setContentsMargins(20, 20, 20, 20)
        self.vL_2.setSpacing(0)
        self.vL_2.setObjectName("vL_2")
        self.f_circle = QtWidgets.QFrame(self.f_container)
        self.f_circle.setStyleSheet("QFrame {\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgb(30, 30, 30);\n"
"    border-radius: 120px;\n"
"    font: 87 9pt \"Biennale Black\";\n"
"}")
        self.f_circle.setObjectName("f_circle")
        self.vL_3 = QtWidgets.QVBoxLayout(self.f_circle)
        self.vL_3.setContentsMargins(0, 0, 0, 0)
        self.vL_3.setSpacing(0)
        self.vL_3.setObjectName("vL_3")
        self.f_texts = QtWidgets.QFrame(self.f_circle)
        self.f_texts.setMaximumSize(QtCore.QSize(16777215, 180))
        self.f_texts.setStyleSheet("background: none")
        self.f_texts.setObjectName("f_texts")
        self.vL_4 = QtWidgets.QVBoxLayout(self.f_texts)
        self.vL_4.setContentsMargins(0, 20, 0, 0)
        self.vL_4.setSpacing(0)
        self.vL_4.setObjectName("vL_4")
        self.gL = QtWidgets.QGridLayout()
        self.gL.setSpacing(0)
        self.gL.setObjectName("gL")
        self.l_loading = QtWidgets.QLabel(self.f_texts)
        self.l_loading.setStyleSheet("color: rgb(255, 200, 200)")
        self.l_loading.setAlignment(QtCore.Qt.AlignCenter)
        self.l_loading.setObjectName("l_loading")
        self.gL.addWidget(self.l_loading, 3, 0, 1, 1)
        self.l_title = QtWidgets.QLabel(self.f_texts)
        self.l_title.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Biennale Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.l_title.setFont(font)
        self.l_title.setStyleSheet("color: rgb(255, 200, 200);\n"
"font-size: 12pt")
        self.l_title.setAlignment(QtCore.Qt.AlignCenter)
        self.l_title.setObjectName("l_title")
        self.gL.addWidget(self.l_title, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.f_texts)
        self.frame.setObjectName("frame")
        self.vL_5 = QtWidgets.QVBoxLayout(self.frame)
        self.vL_5.setContentsMargins(0, 0, 0, 0)
        self.vL_5.setSpacing(0)
        self.vL_5.setObjectName("vL_5")
        self.l_version = QtWidgets.QLabel(self.frame)
        self.l_version.setMinimumSize(QtCore.QSize(100, 22))
        self.l_version.setMaximumSize(QtCore.QSize(100, 22))
        self.l_version.setStyleSheet("QLabel {\n"
"    border: 1px solid transparent;\n"
"    border-radius: 10px;\n"
"    color: rgb(255, 200, 200);\n"
"    background: rgb(60, 60, 60)\n"
"}")
        self.l_version.setText("")
        self.l_version.setAlignment(QtCore.Qt.AlignCenter)
        self.l_version.setObjectName("l_version")
        self.vL_5.addWidget(self.l_version, 0, QtCore.Qt.AlignHCenter)
        self.gL.addWidget(self.frame, 2, 0, 1, 1)
        self.empty = QtWidgets.QFrame(self.f_texts)
        self.empty.setMinimumSize(QtCore.QSize(0, 80))
        self.empty.setObjectName("empty")
        self.gL.addWidget(self.empty, 1, 0, 1, 1)
        self.vL_4.addLayout(self.gL)
        self.vL_3.addWidget(self.f_texts)
        self.vL_2.addWidget(self.f_circle)
        self.vL.addWidget(self.f_container)
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)
        QtCore.QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen):
        _translate = QtCore.QCoreApplication.translate
        self.l_loading.setText(_translate("SplashScreen", "Loading"))
        self.l_title.setText(_translate("SplashScreen", "OverlayGT"))
