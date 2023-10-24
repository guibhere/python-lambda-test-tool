from PyQt5 import QtCore, QtGui, QtWidgets
import os
from src.Ui.lambda_test_tool_ui import Ui_MainWindow
import ctypes

myappid = u'python-lambda-test-tool' 
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class Ui_MainWindowExtensions(Ui_MainWindow):
    def __init__(self, MainWindow: QtWidgets.QMainWindow):
        self.setupUi(MainWindow)
        self.set_icon(MainWindow)

    def set_icon(self, MainWindow):
        current_file_path = os.path.abspath(__file__)
        current_folder_path = os.path.dirname(current_file_path)
        current_folder_path, _ = os.path.split(current_folder_path)
        path = os.path.join(current_folder_path, "images\icon.png")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(128, 128))
