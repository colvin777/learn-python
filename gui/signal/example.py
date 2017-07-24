#-*- coding:utf-8 -*-
'''
defined Signal
'''
__author__ = 'Tony Zhu'
import sys
from PyQt5.QtCore import pyqtSignal, QObject, Qt, pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication, QGroupBox, QPushButton, QLabel, QCheckBox, QSpinBox, QHBoxLayout, QComboBox, QGridLayout
 
 
class SignalEmit(QWidget):
    helpSignal = pyqtSignal(str)
    printSignal = pyqtSignal(list)
    #����һ�������ذ汾���źţ�������һ����int��str���Ͳ������źţ��Լ���str�������ź�
    previewSignal = pyqtSignal([int,str],[str])
    def __init__(self):
        super().__init__()        
        self.initUI()
 
 
    def initUI(self):           
 
        self.creatContorls("��ӡ���ƣ�")
        self.creatResult("���������")
 
        layout = QHBoxLayout()
        layout.addWidget(self.controlsGroup)
        layout.addWidget(self.resultGroup)
        self.setLayout(layout)
 
        self.helpSignal.connect(self.showHelpMessage)
        self.printSignal.connect(self.printPaper)
        self.previewSignal[str].connect(self.previewPaper)
        self.previewSignal[int,str].connect(self.previewPaperWithArgs)  
        self.printButton.clicked.connect(self.emitPrintSignal)
        self.previewButton.clicked.connect(self.emitPreviewSignal)
 
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('defined signal')
        self.show()
 
    def creatContorls(self,title):
        self.controlsGroup = QGroupBox(title)
        self.printButton = QPushButton("��ӡ")
        self.previewButton  = QPushButton("Ԥ��")
        numberLabel = QLabel("��ӡ������")
        pageLabel = QLabel("ֽ�����ͣ�")
        self.previewStatus = QCheckBox("ȫ��Ԥ��")
        self.numberSpinBox = QSpinBox()
        self.numberSpinBox.setRange(1, 100)
        self.styleCombo = QComboBox(self)
        self.styleCombo.addItem("A4")
        self.styleCombo.addItem("A5")
 
        controlsLayout = QGridLayout()
        controlsLayout.addWidget(numberLabel, 0, 0)
        controlsLayout.addWidget(self.numberSpinBox, 0, 1)
        controlsLayout.addWidget(pageLabel, 0, 2)
        controlsLayout.addWidget(self.styleCombo, 0, 3)
        controlsLayout.addWidget(self.printButton, 0, 4)
        controlsLayout.addWidget(self.previewStatus, 3, 0)
        controlsLayout.addWidget(self.previewButton, 3, 1)
        self.controlsGroup.setLayout(controlsLayout)
 
    def creatResult(self,title):
        self.resultGroup = QGroupBox(title)
        self.resultLabel = QLabel("")
        layout = QHBoxLayout()
        layout.addWidget(self.resultLabel)
        self.resultGroup.setLayout(layout)
 
    def emitPreviewSignal(self):
        if self.previewStatus.isChecked() == True:
            self.previewSignal[int,str].emit(1080," Full Screen")
        elif self.previewStatus.isChecked() == False:
            self.previewSignal[str].emit("Preview")
 
    def emitPrintSignal(self):
        pList = []
        pList.append(self.numberSpinBox.value ())
        pList.append(self.styleCombo.currentText())
        self.printSignal.emit(pList)
 
    def printPaper(self,list):
        self.resultLabel.setText("Print: "+"������"+ str(list[0]) +"  ֽ�ţ�"+str(list[1]))
 
    def previewPaperWithArgs(self,style,text):
        self.resultLabel.setText(str(style)+text)
 
    def previewPaper(self,text):
        self.resultLabel.setText(text)          
 
    def keyPressEvent(self, event):
 
        if event.key() == Qt.Key_F1:
            self.helpSignal.emit("help message")
 
    def showHelpMessage(self,message):
        self.resultLabel.setText(message)
        #self.statusBar().showMessage(message)
 
 
if __name__ == '__main__':
 
    app = QApplication(sys.argv)
    dispatch = SignalEmit()
    sys.exit(app.exec_())