# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contactUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1141, 740)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Dialog.setAutoFillBackground(False)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_2)
        self.scrollArea.setEnabled(True)
        self.scrollArea.setMinimumSize(QtCore.QSize(325, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(325, 150000))
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea.setMidLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 300, 12000))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 0, 300, 80))
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setText("")
        self.pushButton_2.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(220, 10, 72, 15))
        self.label.setObjectName("label")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.addWidget(self.scrollArea)
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_remark = QtWidgets.QLabel(self.frame)
        self.label_remark.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_remark.setFont(font)
        self.label_remark.setText("")
        self.label_remark.setObjectName("label_remark")
        self.horizontalLayout_3.addWidget(self.label_remark)
        self.btn_analysis = QtWidgets.QPushButton(self.frame)
        self.btn_analysis.setObjectName("btn_analysis")
        self.horizontalLayout_3.addWidget(self.btn_analysis)
        self.btn_emotion = QtWidgets.QPushButton(self.frame)
        self.btn_emotion.setObjectName("btn_emotion")
        self.horizontalLayout_3.addWidget(self.btn_emotion)
        self.btn_output = QtWidgets.QPushButton(self.frame)
        self.btn_output.setObjectName("btn_output")
        self.horizontalLayout_3.addWidget(self.btn_output)
        self.btn_back = QtWidgets.QPushButton(self.frame)
        self.btn_back.setObjectName("btn_back")
        self.horizontalLayout_3.addWidget(self.btn_back)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frame)
        self.horizontalLayout.addWidget(self.frame_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.btn_analysis.setText(_translate("Dialog", "统计信息"))
        self.btn_emotion.setText(_translate("Dialog", "情感分析"))
        self.btn_output.setText(_translate("Dialog", "导出聊天记录"))
        self.btn_back.setText(_translate("Dialog", "退出"))
