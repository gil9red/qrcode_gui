#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


# TODO: rem *
import io

from PySide.QtGui import *
from PySide.QtCore import *

from qrcode import make as make_qrcode


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('qrcode_gui')

        self.input_text = QPlainTextEdit()
        self.input_text.textChanged.connect(self.input_text_changed)

        self.label_im_qrcode = QLabel()
        label_im_qrcode_scrollarea = QScrollArea()
        label_im_qrcode_scrollarea.setBackgroundRole(QPalette.Dark)
        label_im_qrcode_scrollarea.setWidgetResizable(True)
        label_im_qrcode_scrollarea.setWidget(self.label_im_qrcode)
        # TODO: not working align
        label_im_qrcode_scrollarea.setAlignment(Qt.AlignCenter)

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
        im = make_qrcode(text)

        b = io.BytesIO()
        im.save(b, 'png')
        data = b.getvalue()

        pixmap = QPixmap()
        pixmap.loadFromData(data)

        self.label_im_qrcode.setPixmap(pixmap)
