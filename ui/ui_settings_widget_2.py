# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Storage X\About\IT\Python\Git\OverlayGT 2.0\ui\settings_widget_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingsWidget(object):
    def setupUi(self, SettingsWidget):
        SettingsWidget.setObjectName("SettingsWidget")
        SettingsWidget.resize(371, 628)
        self.vL = QtWidgets.QVBoxLayout(SettingsWidget)
        self.vL.setContentsMargins(0, 0, 0, 0)
        self.vL.setSpacing(5)
        self.vL.setObjectName("vL")
        self.f_title = QtWidgets.QFrame(SettingsWidget)
        self.f_title.setMaximumSize(QtCore.QSize(16777215, 24))
        self.f_title.setObjectName("f_title")
        self.hL_2 = QtWidgets.QHBoxLayout(self.f_title)
        self.hL_2.setContentsMargins(3, 3, 3, 3)
        self.hL_2.setSpacing(10)
        self.hL_2.setObjectName("hL_2")
        self.l_icon_title = QtWidgets.QLabel(self.f_title)
        self.l_icon_title.setMinimumSize(QtCore.QSize(19, 19))
        self.l_icon_title.setMaximumSize(QtCore.QSize(19, 19))
        self.l_icon_title.setPixmap(QtGui.QPixmap(":/img/img_3.png"))
        self.l_icon_title.setScaledContents(True)
        self.l_icon_title.setObjectName("l_icon_title")
        self.hL_2.addWidget(self.l_icon_title)
        self.l_title = QtWidgets.QLabel(self.f_title)
        font = QtGui.QFont()
        font.setFamily("Biennale Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.l_title.setFont(font)
        self.l_title.setObjectName("l_title")
        self.hL_2.addWidget(self.l_title)
        self.btn_hide = QtWidgets.QPushButton(self.f_title)
        self.btn_hide.setMaximumSize(QtCore.QSize(19, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img_9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_hide.setIcon(icon)
        self.btn_hide.setIconSize(QtCore.QSize(20, 20))
        self.btn_hide.setObjectName("btn_hide")
        self.hL_2.addWidget(self.btn_hide)
        self.vL.addWidget(self.f_title)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(SettingsWidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.sA = QtWidgets.QScrollArea(self.groupBox)
        self.sA.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sA.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.sA.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.sA.setWidgetResizable(True)
        self.sA.setObjectName("sA")
        self.sAWC = QtWidgets.QWidget()
        self.sAWC.setGeometry(QtCore.QRect(0, 0, 339, 163))
        self.sAWC.setObjectName("sAWC")
        self.hL_4 = QtWidgets.QHBoxLayout(self.sAWC)
        self.hL_4.setContentsMargins(5, 5, 5, 5)
        self.hL_4.setSpacing(5)
        self.hL_4.setObjectName("hL_4")
        self.sA.setWidget(self.sAWC)
        self.horizontalLayout_4.addWidget(self.sA)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(SettingsWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.fL_2 = QtWidgets.QFormLayout(self.groupBox_2)
        self.fL_2.setContentsMargins(5, 5, 5, 5)
        self.fL_2.setSpacing(5)
        self.fL_2.setObjectName("fL_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setMinimumSize(QtCore.QSize(0, 25))
        self.label_3.setObjectName("label_3")
        self.fL_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.hL = QtWidgets.QHBoxLayout()
        self.hL.setSpacing(0)
        self.hL.setObjectName("hL")
        self.lE = QtWidgets.QLineEdit(self.groupBox_2)
        self.lE.setReadOnly(True)
        self.lE.setObjectName("lE")
        self.hL.addWidget(self.lE)
        self.tB = QtWidgets.QToolButton(self.groupBox_2)
        self.tB.setObjectName("tB")
        self.hL.addWidget(self.tB)
        self.fL_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.hL)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setMinimumSize(QtCore.QSize(0, 25))
        self.label_4.setObjectName("label_4")
        self.fL_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.hL_3 = QtWidgets.QHBoxLayout()
        self.hL_3.setObjectName("hL_3")
        self.hS = QtWidgets.QSlider(self.groupBox_2)
        self.hS.setMaximum(100)
        self.hS.setOrientation(QtCore.Qt.Horizontal)
        self.hS.setObjectName("hS")
        self.hL_3.addWidget(self.hS)
        self.l_num = QtWidgets.QLabel(self.groupBox_2)
        self.l_num.setMinimumSize(QtCore.QSize(20, 0))
        self.l_num.setMaximumSize(QtCore.QSize(20, 16777215))
        self.l_num.setAlignment(QtCore.Qt.AlignCenter)
        self.l_num.setObjectName("l_num")
        self.hL_3.addWidget(self.l_num)
        self.fL_2.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.hL_3)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(SettingsWidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_3)
        self.formLayout.setContentsMargins(5, 5, 5, 5)
        self.formLayout.setSpacing(5)
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setMinimumSize(QtCore.QSize(0, 25))
        self.label_5.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.kSE_mode_changer = QtWidgets.QKeySequenceEdit(self.groupBox_3)
        self.kSE_mode_changer.setObjectName("kSE_mode_changer")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.kSE_mode_changer)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.kSE_show_hide = QtWidgets.QKeySequenceEdit(self.groupBox_3)
        self.kSE_show_hide.setObjectName("kSE_show_hide")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.kSE_show_hide)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(SettingsWidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkB_5 = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkB_5.setMinimumSize(QtCore.QSize(0, 25))
        self.checkB_5.setObjectName("checkB_5")
        self.horizontalLayout.addWidget(self.checkB_5)
        self.checkB_4 = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkB_4.setMinimumSize(QtCore.QSize(0, 25))
        self.checkB_4.setObjectName("checkB_4")
        self.horizontalLayout.addWidget(self.checkB_4)
        self.checkB_3 = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkB_3.setMinimumSize(QtCore.QSize(0, 25))
        self.checkB_3.setObjectName("checkB_3")
        self.horizontalLayout.addWidget(self.checkB_3)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(SettingsWidget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkB = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkB.setStyleSheet("")
        self.checkB.setObjectName("checkB")
        self.horizontalLayout_2.addWidget(self.checkB)
        self.checkB_2 = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkB_2.setObjectName("checkB_2")
        self.horizontalLayout_2.addWidget(self.checkB_2)
        self.verticalLayout.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(SettingsWidget)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_check_upd = QtWidgets.QPushButton(self.groupBox_6)
        self.btn_check_upd.setObjectName("btn_check_upd")
        self.verticalLayout_2.addWidget(self.btn_check_upd)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox_6)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.l_last_check_upd_time = QtWidgets.QLabel(self.groupBox_6)
        self.l_last_check_upd_time.setObjectName("l_last_check_upd_time")
        self.horizontalLayout_3.addWidget(self.l_last_check_upd_time)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.groupBox_6)
        self.btn_save = QtWidgets.QPushButton(SettingsWidget)
        self.btn_save.setObjectName("btn_save")
        self.verticalLayout.addWidget(self.btn_save, 0, QtCore.Qt.AlignHCenter)
        self.vL.addLayout(self.verticalLayout)

        self.retranslateUi(SettingsWidget)
        QtCore.QMetaObject.connectSlotsByName(SettingsWidget)

    def retranslateUi(self, SettingsWidget):
        _translate = QtCore.QCoreApplication.translate
        self.l_title.setText(_translate("SettingsWidget", "Настройки"))
        self.groupBox.setTitle(_translate("SettingsWidget", "Темы"))
        self.groupBox_2.setTitle(_translate("SettingsWidget", "Фон"))
        self.label_3.setText(_translate("SettingsWidget", "Фон"))
        self.tB.setText(_translate("SettingsWidget", "..."))
        self.label_4.setText(_translate("SettingsWidget", "Blur эффект"))
        self.l_num.setText(_translate("SettingsWidget", "0"))
        self.groupBox_3.setTitle(_translate("SettingsWidget", "Горячие клавиши"))
        self.label_5.setText(_translate("SettingsWidget", "Режим заставки"))
        self.kSE_mode_changer.setKeySequence(_translate("SettingsWidget", "Alt+1"))
        self.label_6.setText(_translate("SettingsWidget", "Открыть/Закрыть"))
        self.kSE_show_hide.setKeySequence(_translate("SettingsWidget", "Alt+Ё"))
        self.groupBox_4.setTitle(_translate("SettingsWidget", "Интернет"))
        self.checkB_5.setText(_translate("SettingsWidget", "Download"))
        self.checkB_4.setText(_translate("SettingsWidget", "Ping"))
        self.checkB_3.setText(_translate("SettingsWidget", "Время работы ПК"))
        self.groupBox_5.setTitle(_translate("SettingsWidget", "Автозапуск"))
        self.checkB.setText(_translate("SettingsWidget", "Автоматически запускать с Windows"))
        self.checkB_2.setText(_translate("SettingsWidget", "Запускать свернутым"))
        self.groupBox_6.setTitle(_translate("SettingsWidget", "Обновления"))
        self.btn_check_upd.setText(_translate("SettingsWidget", "Проверить обновления"))
        self.label.setText(_translate("SettingsWidget", "Последняя проверка обновлений:"))
        self.l_last_check_upd_time.setText(_translate("SettingsWidget", "-"))
        self.btn_save.setText(_translate("SettingsWidget", "Сохранить"))
