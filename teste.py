import json
import os
from PyQt5 import QtWidgets,QtCore,QtGui
from UI_functions import DirectoryManager,JsonFileManager
from PyQt5.QtWidgets import QFileDialog
from lambda_test_tool_ui import Ui_MainWindow
from UI_logger import OutputRedirectorQt
import lambda_teste_tool 
from dependency_installer import DependencyInstaller
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import HtmlFormatter

class ButtonFunctionality:
    def __init__(self,  ui: Ui_MainWindow,args):
        self.ui : Ui_MainWindow = ui
        self.dir_manager = DirectoryManager(app, None, "args")
        self.json_manager = JsonFileManager(None,None)
        self.args = args
        self.event_dir = args[2]

        self.ui.select_lambda_pushButton.clicked.connect(self.selecionar_lambda)
        self.ui.actionSelecionar_diretorio_de_eventos.triggered.connect(self.selecionar_diretorio_eventos)
        self.ui.evento_comboBox.activated.connect(self.selecionar_event_json)
        self.ui.actionSalvar_Json.triggered.connect(self.salvar_evento_json)
        self.ui.actionAbrir_Json.triggered.connect(self.carregar_evento_json)
        self.ui.invoke_lambda_pushButton.clicked.connect(self.invoke_lambda)
        self.ui.actionInstalar_dependencias_do_projeto_requirements_txt.triggered.connect(self.instalar_dependencias)

    def selecionar_lambda(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly  

        file_dialog = QFileDialog()
        file_dialog.setOptions(options)

        file_path,filter = file_dialog.getOpenFileName(None, "Selecione a lambda function", "", "Python Files (*.py)")
        self.ui.app_path_textEdit.setText(file_path)
        
    def selecionar_diretorio_eventos(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly  

        file_dialog = QFileDialog()
        file_dialog.setOptions(options)

        dir_path = file_dialog.getExistingDirectory(None, "Selecione o diretorio de eventos",  "")
        eventos = self.dir_manager.list_json_files(dir_path)
        self.ui.evento_comboBox.addItems(eventos)
        self.event_dir = dir_path
        
    def selecionar_event_json(self,index):
        selected_item = self.ui.evento_comboBox.itemText(index)
        evento = self.json_manager.read_json_file(dir=self.event_dir, file_name=selected_item)
        
        formatted_html = highlight(evento, JsonLexer(), HtmlFormatter())
        self.ui.evento_textEdit.setHtml(formatted_html)
        #self.ui.evento_textEdit.setPlainText(evento)
        
    def salvar_evento_json(self):
        try:
            json_data = self.ui.evento_textEdit.toPlainText()
            options = QFileDialog.Options()
            file_path, _ = QFileDialog.getSaveFileName(None,directory=self.event_dir ,   caption="Save JSON File", filter= "JSON Files (*.json);;All Files (*)", options=options)
            novo_evento = os.path.basename(file_path)
            if file_path:
                with open(file_path, 'w') as file:
                    file.write(json_data)
            eventos = self.dir_manager.list_json_files(self.event_dir)
            self.ui.evento_comboBox.clear()
            self.ui.evento_comboBox.addItems(eventos)
            index = self.ui.evento_comboBox.findText(novo_evento)
            if index != -1:
                self.ui.evento_comboBox.setCurrentIndex(index)
        except Exception as e:
            print(e)
    
    def carregar_evento_json(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly  

        file_dialog = QFileDialog()
        file_dialog.setOptions(options)

        file_path,filter = file_dialog.getOpenFileName(None,directory=self.event_dir ,caption="Selecione o evento .json",filter= "Json Files (*.json)")
        if file_path:
            with open(file_path, 'r') as file:
                json_text = file.read()
        self.ui.evento_textEdit.setPlainText(json_text)
        
    def invoke_lambda(self):
        try:
            json_data = self.ui.evento_textEdit.toPlainText()
            parsed_json = json.loads(json_data)

            params = []
            params.append(self.ui.app_path_textEdit.toPlainText().strip())
            params.append(self.ui.handler_name_textEdit.toPlainText().strip())
            params.append(json.dumps(parsed_json))
            params.append(args[3])
            params.append("ui")

            lambda_teste_tool.start(params)
        except Exception as e:
            print("Ocorreu um erro no parsing do json: ", str(e))
            
    def instalar_dependencias(self):
        dep_installer = DependencyInstaller(self.args[3] + "requirements.txt")
        dep_installer.InstalarDependenciasNovasRequirements()
            



def init(ui,args):
    dir_manager = DirectoryManager(app, None, args)
    ui.app_path_textEdit.setText(args[0])
    ui.handler_name_textEdit.setPlainText(args[1])
    ui.evento_comboBox.addItems(dir_manager.list_json_files(args[2]))
    
    
if __name__ == "__main__":
    import sys
    from lambda_test_tool_ui import Ui_MainWindow  # Import your generated UI class

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    args = sys.argv[1:]
    sys.stdout = OutputRedirectorQt(ui.logger_textBrowser)
    init(ui,args)
    functionality = ButtonFunctionality(ui,args)  # Create an instance of ButtonFunctionality
    
    MainWindow.show()
    sys.exit(app.exec_())