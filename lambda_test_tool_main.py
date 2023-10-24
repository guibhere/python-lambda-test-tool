import sys
from PyQt5 import QtWidgets
from src.Extensions.MainWindowExtension import Ui_MainWindowExtensions
from src.Functions.ui_funcionalidades  import UI_Funcionalidades
from src.Functions.lambda_test_tool_invoke import Lambda_Test_Tool_Invoke
from PyQt5 import QtCore, QtWidgets

if __name__ == "__main__":
    args = sys.argv[1:]
    app = QtWidgets.QApplication(sys.argv)
    #app.setAttribute(QtCore.Qt.ApplicationAttribute.AA_DontUseNativeDialogs,True ) Verificar se vale a pena
    
    if(args[4] == 'debug'):
        lambda_invoke = Lambda_Test_Tool_Invoke()
        lambda_invoke.start(args)
        
    else:
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindowExtensions(MainWindow)
        functionality = UI_Funcionalidades(ui,args) 
        MainWindow.show()
        sys.exit(app.exec_())