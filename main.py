# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


try:
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *

except:
    try:
        from PyQt4.QtGui import *
        from PyQt4.QtCore import *

    except:
        from PySide.QtGui import *
        from PySide.QtCore import *


def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)
    import traceback
    text += ''.join(traceback.format_tb(tb))

    print(text)
    QMessageBox.critical(None, 'Error', text)
    quit()


import sys
sys.excepthook = log_uncaught_exceptions


from mainwindow import MainWindow


if __name__ == '__main__':
    app = QApplication([])

    mw = MainWindow()
    mw.resize(400, 600)
    mw.show()

    app.exec_()
