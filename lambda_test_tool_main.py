import sys
from PyQt5 import QtWidgets
from Ui.lambda_test_tool_ui import Ui_MainWindow
from Utils.UI_logger import OutputRedirectorQt
from ui_funcionalidades import UI_Funcionalidades
 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    args = sys.argv[1:]
    sys.stdout = OutputRedirectorQt(ui.logger_textBrowser)
    functionality = UI_Funcionalidades(ui,args)  # Create an instance of ButtonFunctionality
    
    MainWindow.show()
    sys.exit(app.exec_())