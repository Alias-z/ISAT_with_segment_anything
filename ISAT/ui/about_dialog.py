# Form implementation generated from reading ui file 'ISAT/ui\about_dialog.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(550, 240)
        Dialog.setMinimumSize(QtCore.QSize(0, 240))
        Dialog.setMaximumSize(QtCore.QSize(800, 300))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setMinimumSize(QtCore.QSize(0, 0))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_2 = QtWidgets.QWidget(parent=self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.widget_2)
        self.label.setMinimumSize(QtCore.QSize(180, 180))
        self.label.setMaximumSize(QtCore.QSize(180, 180))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icon/icons/ISAT11_100.svg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.widget_3 = QtWidgets.QWidget(parent=self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_version = QtWidgets.QLabel(parent=self.widget_3)
        self.label_version.setMinimumSize(QtCore.QSize(0, 25))
        self.label_version.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_version.setFont(font)
        self.label_version.setStatusTip("")
        self.label_version.setWhatsThis("")
        self.label_version.setAccessibleName("")
        self.label_version.setAccessibleDescription("")
        self.label_version.setAutoFillBackground(False)
        self.label_version.setText("V0.0.1")
        self.label_version.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_version.setOpenExternalLinks(False)
        self.label_version.setObjectName("label_version")
        self.verticalLayout_2.addWidget(self.label_version)
        self.label_5 = QtWidgets.QLabel(parent=self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setOpenExternalLinks(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.verticalLayout_3.addWidget(self.widget_2)
        self.widget_4 = QtWidgets.QWidget(parent=self.widget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_close = QtWidgets.QPushButton(parent=self.widget_4)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_close.setFont(font)
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout.addWidget(self.pushButton_close)
        self.verticalLayout_3.addWidget(self.widget_4)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "about"))
        self.label_3.setText(_translate("Dialog", "ISAT with Segment anything"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Open source on <a href=\"https://github.com/yatengLG/ISAT_with_segment_anything\"><span style=\" font-weight:600; text-decoration: underline; color:#0000ff;\">Github</span></a>.</p><p align=\"center\">Main contributor <a href=\"https://github.com/Alias-z\"><span style=\" font-weight:600; text-decoration: underline; color:#0000ff;\">Alias-z</span></a>.</p><p align=\"center\">ISAT Copyright (C) 2022 <a href=\"https://github.com/yatengLG\"><span style=\" text-decoration: underline; color:#0000ff;\">yatengLG</span></a>.</p></body></html>"))
        self.pushButton_close.setText(_translate("Dialog", "&Close"))
