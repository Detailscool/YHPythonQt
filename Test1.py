#!/usr/bin/python
# -*- coding:utf-8 -*-
# Test1.py
# Created by Henry on 2017/11/9
# Description :

# coding:utf-8

import sys
from PyQt5 import QtWidgets, QtCore

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(360, 360)
widget.setWindowTitle("Hello, PyQt5!")
widget.show()

sys.exit(app.exec_())