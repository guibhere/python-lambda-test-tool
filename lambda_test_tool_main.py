import sys
from PyQt5 import QtWidgets
from Extensions.MainWindowExtension import Ui_MainWindowExtensions
from Utils.UI_logger import OutputRedirectorQt
from ui_funcionalidades import UI_Funcionalidades
import lambda_teste_tool 

if __name__ == "__main__":
    args = sys.argv[1:]
    app = QtWidgets.QApplication(sys.argv)
    
    if(args[4] == 'debug'):
        lambda_teste_tool.start(args)
    else:
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindowExtensions(MainWindow)
        sys.stdout = OutputRedirectorQt(ui.logger_textBrowser)
        functionality = UI_Funcionalidades(ui,args) 
        MainWindow.show()
        sys.exit(app.exec_())