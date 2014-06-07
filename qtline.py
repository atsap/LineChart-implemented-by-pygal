# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\PortablePython\qtline.ui'
#
# Created: Fri Jun 06 15:29:53 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!
import os
import pygal

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(263, 87)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter = QtGui.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.le_title = QtGui.QLineEdit(self.widget)
        self.le_title.setObjectName(_fromUtf8("le_title"))
        self.horizontalLayout_2.addWidget(self.le_title)
        self.widget1 = QtGui.QWidget(self.splitter)
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btn_demo = QtGui.QPushButton(self.widget1)
        self.btn_demo.setObjectName(_fromUtf8("btn_demo"))
        self.horizontalLayout.addWidget(self.btn_demo)
        self.btn_py = QtGui.QPushButton(self.widget1)
        self.btn_py.setObjectName(_fromUtf8("btn_py"))
        self.horizontalLayout.addWidget(self.btn_py)
        #self.btn_specific = QtGui.QPushButton(self.widget1)
        #self.btn_specific.setObjectName(_fromUtf8("btn_specific"))
        #self.horizontalLayout.addWidget(self.btn_specific)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)


        self.retranslateUi(Form)

        def initpy():
            title_py = self.le_title.text()
            self.printpy(title_py)
            return


        QtCore.QObject.connect(self.btn_demo, QtCore.SIGNAL(_fromUtf8("clicked()")), self.printdemo)
        QtCore.QObject.connect(self.btn_py, QtCore.SIGNAL(_fromUtf8("clicked()")), initpy)
        #QtCore.QObject.connect(self.btn_specific, QtCore.SIGNAL(_fromUtf8("clicked()")), self.le_title.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)



    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Title:", None))
        self.le_title.setText(_translate("Form", "LineChart", None))
        self.btn_demo.setText(_translate("Form", "Demo", None))
        self.btn_py.setText(_translate("Form", "*_py", None))
        #self.btn_specific.setText(_translate("Form", "Specific...", None))

    #start of main code block

    def testbb(self,title):
        print title
        return

    def printdemo(self):  #Demo
        line_chart = pygal.Line()
        line_chart.title = 'Demo'
        line_chart.x_labels = map(str, range(2002, 2013))
        line_chart.add('Firefox', [None, None, 0, 16.6, 25, 31, 36.4, 45.5, 46.3, 42.8, 37.1])
        line_chart.add('Chrome', [None, None, None, None, None, None, 0, 3.9, 10.8, 23.8, 35.3])
        line_chart.add('IE', [85.8, 84.6, 84.7, 74.5, 66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
        line_chart.add('Others', [14.2, 15.4, 15.3, 8.9, 9, 10.4, 8.9, 5.8, 6.7, 6.8, 7.5])
        line_chart.render()
        line_chart.render_to_file('Demo.svg')
        line_chart.render_to_png("Demo.png")
        f = open('Demo.html', 'w')
        f.write(line_chart.render())
        f.close()
        return

    def getpylist(self):  # Get *_py file list
        flist = []
        my_path = os.path.dirname(os.path.abspath(__file__))
        print my_path
        for file in os.listdir(my_path):
            if file.endswith("_py.txt"):
                flist.append(file)
        return flist


    def getValue_(self,fn): # Get Dataset
        vv = []
        f = open(str(fn), 'r')
        v_ = filter(None, f.readline().split(','))
        v_ = filter(bool, v_)
        for i in v_:
            vv.append(float(i))
        return vv

    def xRange_(self, flist):
        my_path = os.path.dirname(os.path.abspath(__file__))
        xaxis = 0

        for file in flist:
            f=open(my_path+"\\"+file,'r')
            v_ = filter(None, f.readline().split(','))
            xaxis = max(xaxis,len(v_))
            print "xaxis=" + str(v_)
        return xaxis


    def printpy(self,title):  #Print file name end with _py
        line_chart = pygal.Line()
        line_chart.title = str(title) # this is fucking important...lineedit return QString!
        flist = self.getpylist()
        line_chart.x_labels = map(str, range(1, self.xRange_(flist)))
        for file in flist:
            line_chart.add(str(file).replace('_py.txt',''),   self.getValue_(str(file))) # set y-axis and value
            print self.getValue_(str(file))
        line_chart.render()
        line_chart.render_to_file('py.svg')
        line_chart.render_to_png("py.png")
        f=open('py.html','w')
        f.write(line_chart.render())
        f.close()
        return

        #end of main code block

#start


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


