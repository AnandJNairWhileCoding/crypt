# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Anand Jayaraj\Desktop\crypt.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import random
import pyperclip
a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '+', '_', '/', ',', '.', '<', '>', '?', ';', "'", ':', '"', '}', '[', ']', '{', ' ', '|','\n']
b=['57734', '98739', '99905', '91755', '67426', '32459', '73387', '52354', '90248', '53178', '34190', '66704', '36193', '15670', '33237', '30452', '74849', '69367', '51985', '78908', '38705', '48433', '15210', '14455', '41569', '78375', '13082', '15012', '57868', '73396', '47099', '30759', '36175', '99745', '75871', '51624', '70343', '89323', '80075', '20858', '71014', '82124', '21621', '12777', '80291', '58437', '56261', '70174', '28539', '91376', '53931', '69025', '94242', '36659', '74272', '66010', '22364', '37362', '94540', '76465', '14755', '15623', '78842', '79694', '84690', '91564', '65776', '13340', '40008', '28299', '46175', '78439', '94904', '22731', '89723', '47882', '64384', '54338', '52146', '71717', '28468', '68702', '12444', '81271', '58746', '55888', '97947', '35343', '80668', '31176', '76930', '46984', '98068', '78105', '41656', '11452', '34516', '68136', '13411', '85390', '11483','00000']


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(620, 325)
        self.message = ''
        self.input_text_field = QtWidgets.QPlainTextEdit(Form)
        self.input_text_field.setGeometry(QtCore.QRect(10, 80, 291, 151))
        self.input_text_field.setObjectName("input_text_field")
        self.heading = QtWidgets.QLabel(Form)
        self.heading.setGeometry(QtCore.QRect(10, 10, 601, 31))
        self.heading.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.heading.setObjectName("heading")
        self.input_label = QtWidgets.QLabel(Form)
        self.input_label.setGeometry(QtCore.QRect(20, 50, 41, 21))
        self.input_label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.input_label.setObjectName("input_label")
        self.output_label = QtWidgets.QLabel(Form)
        self.output_label.setGeometry(QtCore.QRect(550, 50, 51, 21))
        self.output_label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.output_label.setObjectName("output_label")
        self.output_text_field = QtWidgets.QPlainTextEdit(Form)
        self.output_text_field.setGeometry(QtCore.QRect(320, 80, 291, 151))
        self.output_text_field.setObjectName("output_text_field")
        self.encrypt_button = QtWidgets.QPushButton(Form)
        self.encrypt_button.setGeometry(QtCore.QRect(10, 240, 75, 23))
        self.encrypt_button.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 9pt \"MS Shell Dlg 2\";")
        self.encrypt_button.setObjectName("encrypt_button")
        self.encrypt_button.clicked.connect(self.encrypter)
        self.decrypt_button = QtWidgets.QPushButton(Form)
        self.decrypt_button.setGeometry(QtCore.QRect(10, 270, 75, 23))
        self.decrypt_button.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 9pt \"MS Shell Dlg 2\";")
        self.decrypt_button.setObjectName("decrypt_button")
        self.decrypt_button.clicked.connect(self.decrypter)
        self.copy_button = QtWidgets.QPushButton(Form)
        self.copy_button.setGeometry(QtCore.QRect(530, 240, 75, 23))
        self.copy_button.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 9pt \"MS Shell Dlg 2\";")
        self.copy_button.setObjectName("copy_button")
        self.copy_button.clicked.connect(self.copy)
        self.built_by_label = QtWidgets.QLabel(Form)
        self.built_by_label.setGeometry(QtCore.QRect(260, 300, 91, 21))
        self.built_by_label.setStyleSheet("\n"
"font: 7pt \"MS Shell Dlg 2\";")
        self.built_by_label.setObjectName("built_by_label")
        self.erase_button = QtWidgets.QPushButton(Form)
        self.erase_button.setGeometry(QtCore.QRect(530, 270, 75, 23))
        self.erase_button.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 9pt \"MS Shell Dlg 2\";")
        self.erase_button.setObjectName("erase_button")
        self.erase_button.clicked.connect(self.erase)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def messagefun(self,text):
        self.mes = QtWidgets.QMessageBox()
        self.mes.setIcon(self.mes.Warning)
        self.mes.setInformativeText(text)
        self.mes.show()
    def encrypter(self):
        c = self.input_text_field.toPlainText() 
        if c != '':
                rand=random.randint(0,9)
                enc=""
                for i in c:
                        if i in a:enc=enc+(str(b[(a.index(i))+rand])) 
                self.output_text_field.setPlainText(enc + str(rand))
        else:
                self.messagefun("Enter some message")

    def decrypter(self):
        q = self.input_text_field.toPlainText() 
        if q != '':
                try :
                        rand=int(q[-1])
                        dec = ""; temp1 = int(0); temp2 = int(5)
                        for _ in range(0,int(len(q)/5)):
                                dec = str(dec + a[(b.index(q[temp1:temp2]))-rand]); temp1 = temp2; temp2 = temp2 + 5                 
                        self.output_text_field.setPlainText(dec)
                except :
                        self.messagefun("please enter the proper encrypted message")        
        else:
                self.messagefun("Enter the encrypted messag")

    def erase(self):
        if self.output_text_field.toPlainText()==self.input_text_field.toPlainText()=="":    
                self.messagefun("There's nothing to erase !")        
        else:
                self.input_text_field.setPlainText('')
                self.output_text_field.setPlainText('')

    def copy(self):
        if self.output_text_field.toPlainText()=="":
                self.messagefun("There's nothing to copy !")    
        else :
                pyperclip.copy(self.output_text_field.toPlainText())            
   
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "crypt"))
        self.heading.setText(_translate("Form", "<html><head/><body><p align=\"center\">Encrypter / Decrypter</p></body></html>"))
        self.input_label.setText(_translate("Form", "Input :"))
        self.output_label.setText(_translate("Form", "Output :"))
        self.encrypt_button.setText(_translate("Form", "Encrypt"))
        self.decrypt_button.setText(_translate("Form", "Decrypt"))
        self.copy_button.setText(_translate("Form", "Copy"))
        self.built_by_label.setText(_translate("Form", "Built by: Anand J Nair"))
        self.erase_button.setText(_translate("Form", "Erase"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
