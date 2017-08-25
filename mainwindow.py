#!/usr/bin/env python
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

import qrcode


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('qrcode_gui')

        self.input_text = QPlainTextEdit()
        self.input_text.textChanged.connect(self.input_text_changed)

        self.label_im_qrcode = QLabel()
        self.label_im_qrcode.setAlignment(Qt.AlignCenter)

        label_im_qrcode_scrollarea = QScrollArea()
        label_im_qrcode_scrollarea.setBackgroundRole(QPalette.Dark)
        label_im_qrcode_scrollarea.setWidgetResizable(True)
        label_im_qrcode_scrollarea.setWidget(self.label_im_qrcode)

        self.button_save_as = QPushButton('Save as')
        self.button_save_as.clicked.connect(self.save_as)
        self.button_save_as.setShortcut('Ctrl+S')

        layout = QVBoxLayout()
        layout.addWidget(QLabel('Input text:'))
        layout.addWidget(self.input_text)
        layout.addWidget(self.button_save_as)
        text_input_widget = QWidget()
        text_input_widget.setLayout(layout)

        central_widget = QSplitter(Qt.Vertical)
        central_widget.addWidget(label_im_qrcode_scrollarea)
        central_widget.addWidget(text_input_widget)
        central_widget.setStretchFactor(0, 1)
        central_widget.setStretchFactor(1, 0)

        self.setCentralWidget(central_widget)

        text_input_widget.setFocus()

    def save_as(self):
        file_name = QFileDialog.getSaveFileName(self, "Save File", "qrcode_image", "Images (*.png *.xpm *.jpg)")[0]
        if file_name:
            self.label_im_qrcode.pixmap().save(file_name)

    def input_text_changed(self):
        text = self.input_text.toPlainText()
        img = qrcode.make(text)

        import io
        b = io.BytesIO()
        img.save(b, 'png')
        data = b.getvalue()

        pixmap = QPixmap()
        pixmap.loadFromData(data)

        self.label_im_qrcode.setPixmap(pixmap)
