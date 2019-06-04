# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\python\test.1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from gui import url,vehicle_check,people_check,login,driver,close_driver
from PyQt5.QtWidgets import QMessageBox

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("信用数据查询V1.2")
        Dialog.resize(428, 490)
        #Dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        Dialog.setFixedSize(Dialog.width(), Dialog.height())
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(220, 260, 111, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 370, 111, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(9)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setPlaceholderText("车牌号")
        self.lineEdit.setGeometry(QtCore.QRect(52, 258, 141, 31))
        font = QtGui.QFont()
        #font.setFamily("黑体")
        font.setPointSize(9)   
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setPlaceholderText("司机姓名")
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 350, 141, 31))
        font = QtGui.QFont()
        #font.setFamily("黑体")
        font.setPointSize(9)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(190, 10, 54, 12))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(-10, 440, 461, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(-60, 20, 531, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.TextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.TextEdit.setGeometry(QtCore.QRect(10, 40, 411, 192))
        self.TextEdit.setObjectName("tableView")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setPlaceholderText("司机身份证号")
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 400, 141, 31))
        font = QtGui.QFont()
        #font.setFamily("黑体")
        font.setPointSize(9)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(0, 320, 500, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.get_vehicle)
        self.pushButton_2.clicked.connect(self.get_people)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "信用数据查询V1.2"))
        self.pushButton.setText(_translate("Dialog", "车辆信息提取"))
        self.pushButton_2.setText(_translate("Dialog", "司机信息提取"))
        self.label_3.setText(_translate("Dialog", "查询结果"))


  
    def get_vehicle(self,Dialog):
                self.TextEdit.clear()
                #login(url)
                text=self.lineEdit.text().strip()
                info=vehicle_check(text)
                if(type(info)==dict):
                    for k,v in info.items():
                        self.TextEdit.appendHtml(k+"<font color='blue'>"+"："+v+"</font>")
                else:
                    self.TextEdit.appendHtml(info)

    def get_people(self,Dialog):
                self.TextEdit.clear()
                name=self.lineEdit_2.text().strip()
                idno=self.lineEdit_3.text().strip()
                info=people_check(name,idno)
                #text=self.lineEdit_2.text()
                #info=people_check(name,idno)
                if(type(info)==dict):
                    for k,v in info.items():
                        self.TextEdit.appendHtml(k+"<font color='blue'>"+"："+v+"</font>")
                else:
                    self.TextEdit.appendHtml(info)

class MyWindow(QtWidgets.QMainWindow):
    def closeEvent(self,event):
        result = QMessageBox.question(self,"退出",
        "是否关闭？",QMessageBox.Yes| QMessageBox.No)
        event.ignore()

        if result == QMessageBox.Yes:
            close_driver(driver)
            event.accept()
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MyWindow()
    mainWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    ui = Ui_Dialog()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
