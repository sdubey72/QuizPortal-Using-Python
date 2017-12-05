# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Quiz.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QuizWindow(object):
    def setupUi(self, QuizWindow):
        QuizWindow.setObjectName("QuizWindow")
        QuizWindow.setWindowModality(QtCore.Qt.NonModal)
        QuizWindow.resize(830, 701)
        self.centralwidget = QtWidgets.QWidget(QuizWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.rBtn_option3 = QtWidgets.QRadioButton(self.centralwidget)
        self.rBtn_option3.setGeometry(QtCore.QRect(150, 430, 511, 41))
        self.rBtn_option3.setObjectName("rBtn_option3")
        self.rBtn_option4 = QtWidgets.QRadioButton(self.centralwidget)
        self.rBtn_option4.setGeometry(QtCore.QRect(150, 500, 501, 41))
        self.rBtn_option4.setObjectName("rBtn_option4")
        self.btn_next_ques = QtWidgets.QPushButton(self.centralwidget)
        self.btn_next_ques.setGeometry(QtCore.QRect(440, 620, 161, 41))
        self.btn_next_ques.setObjectName("btn_next_ques")
        self.rBtn_option2 = QtWidgets.QRadioButton(self.centralwidget)
        self.rBtn_option2.setGeometry(QtCore.QRect(150, 360, 511, 41))
        self.rBtn_option2.setObjectName("rBtn_option2")
        self.rBtn_option1 = QtWidgets.QRadioButton(self.centralwidget)
        self.rBtn_option1.setGeometry(QtCore.QRect(150, 290, 501, 31))
        self.rBtn_option1.setObjectName("rBtn_option1")
        self.input_question = QtWidgets.QTextEdit(self.centralwidget)
        self.input_question.setGeometry(QtCore.QRect(10, 10, 811, 261))
        self.input_question.setFrameShape(QtWidgets.QFrame.Box)
        self.input_question.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.input_question.setObjectName("input_question")
        self.btn_prev_ques = QtWidgets.QPushButton(self.centralwidget)
        self.btn_prev_ques.setGeometry(QtCore.QRect(140, 620, 161, 41))
        self.btn_prev_ques.setObjectName("btn_prev_ques")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(330, 620, 81, 31))
        self.lcdNumber.setLineWidth(1)
        self.lcdNumber.setMidLineWidth(1)
        self.lcdNumber.setDigitCount(4)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setObjectName("lcdNumber")
        QuizWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(QuizWindow)
        QtCore.QMetaObject.connectSlotsByName(QuizWindow)
        QuizWindow.setTabOrder(self.input_question, self.rBtn_option1)
        QuizWindow.setTabOrder(self.rBtn_option1, self.rBtn_option2)
        QuizWindow.setTabOrder(self.rBtn_option2, self.rBtn_option3)
        QuizWindow.setTabOrder(self.rBtn_option3, self.rBtn_option4)
        QuizWindow.setTabOrder(self.rBtn_option4, self.btn_next_ques)
        QuizWindow.setTabOrder(self.btn_next_ques, self.btn_prev_ques)

    def retranslateUi(self, QuizWindow):
        _translate = QtCore.QCoreApplication.translate
        QuizWindow.setWindowTitle(_translate("QuizWindow", "Quiz"))
        self.rBtn_option3.setText(_translate("QuizWindow", "RadioButton"))
        self.rBtn_option4.setText(_translate("QuizWindow", "RadioButton"))
        self.btn_next_ques.setText(_translate("QuizWindow", "Next >>"))
        self.rBtn_option2.setText(_translate("QuizWindow", "RadioButton"))
        self.rBtn_option1.setText(_translate("QuizWindow", "RadioButton"))
        self.input_question.setPlaceholderText(_translate("QuizWindow", "Question"))
        self.btn_prev_ques.setText(_translate("QuizWindow", "<< Previous"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QuizWindow = QtWidgets.QMainWindow()
    ui = Ui_QuizWindow()
    ui.setupUi(QuizWindow)
    QuizWindow.show()
    sys.exit(app.exec_())

