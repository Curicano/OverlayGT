# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Storage X\About\Programirovanie\Python\Git\OverlayGT 2.0\main\ui\widget_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TranslitWidget(object):
    def setupUi(self, TranslitWidget):
        TranslitWidget.setObjectName("TranslitWidget")
        TranslitWidget.resize(505, 255)
        self.btn_swap_lang = QtWidgets.QPushButton(TranslitWidget)
        self.btn_swap_lang.setGeometry(QtCore.QRect(240, 27, 25, 25))
        self.btn_swap_lang.setMinimumSize(QtCore.QSize(25, 25))
        self.btn_swap_lang.setMaximumSize(QtCore.QSize(25, 25))
        self.btn_swap_lang.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_swap_lang.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img_0.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_swap_lang.setIcon(icon)
        self.btn_swap_lang.setIconSize(QtCore.QSize(20, 20))
        self.btn_swap_lang.setObjectName("btn_swap_lang")
        self.l_from_lang = QtWidgets.QLabel(TranslitWidget)
        self.l_from_lang.setGeometry(QtCore.QRect(5, 27, 225, 18))
        self.l_from_lang.setAlignment(QtCore.Qt.AlignCenter)
        self.l_from_lang.setObjectName("l_from_lang")
        self.btn_translite = QtWidgets.QPushButton(TranslitWidget)
        self.btn_translite.setGeometry(QtCore.QRect(240, 137, 25, 25))
        self.btn_translite.setMinimumSize(QtCore.QSize(25, 25))
        self.btn_translite.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_translite.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/img_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_translite.setIcon(icon1)
        self.btn_translite.setIconSize(QtCore.QSize(20, 20))
        self.btn_translite.setObjectName("btn_translite")
        self.tE_2 = QtWidgets.QTextEdit(TranslitWidget)
        self.tE_2.setGeometry(QtCore.QRect(275, 52, 225, 198))
        self.tE_2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tE_2.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        self.tE_2.setReadOnly(True)
        self.tE_2.setObjectName("tE_2")
        self.l_to_lang = QtWidgets.QLabel(TranslitWidget)
        self.l_to_lang.setGeometry(QtCore.QRect(275, 27, 225, 18))
        self.l_to_lang.setAlignment(QtCore.Qt.AlignCenter)
        self.l_to_lang.setObjectName("l_to_lang")
        self.tE_1 = QtWidgets.QTextEdit(TranslitWidget)
        self.tE_1.setGeometry(QtCore.QRect(5, 52, 225, 198))
        self.tE_1.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tE_1.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        self.tE_1.setObjectName("tE_1")
        self.f_title = QtWidgets.QFrame(TranslitWidget)
        self.f_title.setGeometry(QtCore.QRect(0, 0, 505, 22))
        self.f_title.setObjectName("f_title")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.f_title)
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.l_icon_title = QtWidgets.QLabel(self.f_title)
        self.l_icon_title.setMaximumSize(QtCore.QSize(20, 16777215))
        self.l_icon_title.setPixmap(QtGui.QPixmap(":/img/img_1.png"))
        self.l_icon_title.setScaledContents(True)
        self.l_icon_title.setObjectName("l_icon_title")
        self.horizontalLayout.addWidget(self.l_icon_title)
        self.l_title = QtWidgets.QLabel(self.f_title)
        font = QtGui.QFont()
        font.setFamily("Biennale Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.l_title.setFont(font)
        self.l_title.setObjectName("l_title")
        self.horizontalLayout.addWidget(self.l_title)
        self.btn_hide = QtWidgets.QPushButton(self.f_title)
        self.btn_hide.setMinimumSize(QtCore.QSize(20, 20))
        self.btn_hide.setMaximumSize(QtCore.QSize(20, 20))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/img_9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_hide.setIcon(icon2)
        self.btn_hide.setIconSize(QtCore.QSize(20, 20))
        self.btn_hide.setObjectName("btn_hide")
        self.horizontalLayout.addWidget(self.btn_hide)
        self.action_1 = QtWidgets.QAction(TranslitWidget)
        self.action_1.setObjectName("action_1")
        self.action_2 = QtWidgets.QAction(TranslitWidget)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(TranslitWidget)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(TranslitWidget)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(TranslitWidget)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(TranslitWidget)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtWidgets.QAction(TranslitWidget)
        self.action_7.setObjectName("action_7")

        self.retranslateUi(TranslitWidget)
        self.btn_hide.clicked.connect(TranslitWidget.hide) # type: ignore
        self.tE_1.textChanged.connect(self.tE_2.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(TranslitWidget)

    def retranslateUi(self, TranslitWidget):
        _translate = QtCore.QCoreApplication.translate
        self.btn_swap_lang.setToolTip(_translate("TranslitWidget", "Смена языка"))
        self.l_from_lang.setText(_translate("TranslitWidget", "Русский"))
        self.btn_translite.setToolTip(_translate("TranslitWidget", "Перевод"))
        self.l_to_lang.setText(_translate("TranslitWidget", "Английский"))
        self.l_title.setText(_translate("TranslitWidget", " Переводчик"))
        self.action_1.setText(_translate("TranslitWidget", "Отменить действие"))
        self.action_1.setShortcut(_translate("TranslitWidget", "Ctrl+Z"))
        self.action_2.setText(_translate("TranslitWidget", "Повторить действие"))
        self.action_2.setShortcut(_translate("TranslitWidget", "Ctrl+Y"))
        self.action_3.setText(_translate("TranslitWidget", "Вырезать"))
        self.action_3.setShortcut(_translate("TranslitWidget", "Ctrl+X"))
        self.action_4.setText(_translate("TranslitWidget", "Копировать"))
        self.action_4.setShortcut(_translate("TranslitWidget", "Ctrl+C"))
        self.action_5.setText(_translate("TranslitWidget", "Вставить"))
        self.action_5.setShortcut(_translate("TranslitWidget", "Ctrl+V"))
        self.action_6.setText(_translate("TranslitWidget", "Удалить все"))
        self.action_6.setShortcut(_translate("TranslitWidget", "Del"))
        self.action_7.setText(_translate("TranslitWidget", "Выбрать все"))
        self.action_7.setShortcut(_translate("TranslitWidget", "Ctrl+A"))
