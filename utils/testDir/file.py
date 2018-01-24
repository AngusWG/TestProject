#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/1/9 0009 10:05
# @author  : zza
# @Email   : 740713651@qq.com

import sys
from PyQt5 import QtWidgets, QtCore

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(360, 360)
widget.setWindowTitle("Hello, PyQt5!")
widget.show()
sys.exit(app.exec_())