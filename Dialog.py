import cbe1
import cbe2
import cbe3
import cbe4
import cbe5
import cbe6
import cbe7


from PyQt5.QtWidgets import (QMainWindow, QWidget, QApplication, QComboBox, QDialog,
QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
QVBoxLayout, QPlainTextEdit, QPushButton, QMessageBox, QFrame, QCheckBox, QStatusBar)
from PyQt5.QtGui import QIcon, QImage, QPixmap
#from PyQt5 import 
from latex2mathml import converter
from PyQt5.QtCore import pyqtSlot, QUrl, QUrlQuery

import sys
import PyQt5

from PyQt5.QtNetwork import *

from io import BytesIO
import sympy

class MainWidget(QWidget):
	
	def __init__(self):
		super().__init__()
		self.title = "CBE Solution Generator"
