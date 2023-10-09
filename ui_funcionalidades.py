import json
from Utils.file_helper import File_Helper
from Ui.lambda_test_tool_ui import Ui_MainWindow
import lambda_teste_tool
from Utils.dependency_installer import DependencyInstaller
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import HtmlFormatter

class UI_Funcionalidades:
    def __init__(self, ui: Ui_MainWindow, args):
        self.ui: Ui_MainWindow = ui
        self.file_helper = File_Helper()
        self.args = args
        self.event_dir = args[2]
        self.dep_dir = args[3]
        
        self.init_values()
        self.connect_actions()
        
    def init_values(self):
        self.ui.app_path_textEdit.setText(self.args[0])
        self.ui.handler_name_textEdit.setPlainText(self.args[1])
        self.ui.evento_comboBox.addItems(
            self.file_helper.list_json_files(self.event_dir)
        )
        self.ui.dep_path_TextEdit.setPlainText(self.dep_dir)

    def connect_actions(self):
        self.ui.select_lambda_pushButton.clicked.connect(self.selecionar_lambda)
        self.ui.actionSelecionar_diretorio_de_eventos.triggered.connect(
            self.selecionar_diretorio_eventos
        )
        self.ui.evento_comboBox.activated.connect(self.selecionar_event_json)
        self.ui.actionSalvar_Json.triggered.connect(self.salvar_evento_json)
        self.ui.actionAbrir_Json.triggered.connect(self.carregar_evento_json)
        self.ui.invoke_lambda_pushButton.clicked.connect(self.invoke_lambda)
        self.ui.actionInstalar_dependencias_do_projeto_requirements_txt.triggered.connect(
            self.instalar_dependencias
        )
        self.ui.select_dep_dir_pushButton.clicked.connect(
            self.selecionar_dir_raiz_dependencias
        )

    def selecionar_lambda(self):
        try:    
            file_path = self.file_helper.selecionar_lambda()
            self.ui.app_path_textEdit.setText(file_path)
        except Exception as e:
            print(str(e))
            

    def selecionar_diretorio_eventos(self):
        try:
            dir_path = self.file_helper.selecionar_diretorio()
            eventos = self.file_helper.list_json_files(dir_path)
            self.ui.evento_comboBox.clear()
            self.ui.evento_comboBox.addItems(eventos)
            self.event_dir = dir_path
        except Exception as e:
            print(str(e))

    def selecionar_event_json(self, index):
        try:
            selected_item = self.ui.evento_comboBox.itemText(index)
            evento = self.file_helper.read_file(dir=self.event_dir, file_name=selected_item)
            formatted_html = highlight(evento, JsonLexer(), HtmlFormatter())
            self.ui.evento_textEdit.setHtml(formatted_html)
        except Exception as e:
            print(str(e))

    def salvar_evento_json(self):
        try:
            json_data = self.ui.evento_textEdit.toPlainText()
            novo_evento = self.file_helper.salvar_json(self.event_dir, json_data)
            eventos = self.file_helper.list_json_files(self.event_dir)
            self.ui.evento_comboBox.clear()
            self.ui.evento_comboBox.addItems(eventos)
            index = self.ui.evento_comboBox.findText(novo_evento)
            if index != -1:
                self.ui.evento_comboBox.setCurrentIndex(index)
        except Exception as e:
            print(str(e))

    def carregar_evento_json(self):
        try:
            json_text = self.file_helper.carregar_json_file(self.event_dir)
            self.ui.evento_textEdit.setPlainText(json_text)
            formatted_html = highlight(json_text, JsonLexer(), HtmlFormatter())
            self.ui.evento_textEdit.setHtml(formatted_html)
        except Exception as e:
            print(str(e))

    def invoke_lambda(self):
        try:
            json_data = self.ui.evento_textEdit.toPlainText()
            parsed_json = json.loads(json_data)

            params = []
            params.append(self.ui.app_path_textEdit.toPlainText().strip())
            params.append(self.ui.handler_name_textEdit.toPlainText().strip())
            params.append(json.dumps(parsed_json))
            params.append(self.ui.dep_path_TextEdit.toPlainText().strip())
            params.append("ui")

            lambda_teste_tool.start(params)
        except Exception as e:
            print("Ocorreu um erro no parsing do json: ", str(e))

    def instalar_dependencias(self):
        try:
            dep_installer = DependencyInstaller(self.args[3] + "requirements.txt")
            dep_installer.InstalarDependenciasNovasRequirements()
        except Exception as e:
            print(str(e))

    def selecionar_dir_raiz_dependencias(self):
        try:
            dir_path = self.file_helper.selecionar_diretorio()
            self.ui.dep_path_TextEdit.setPlainText(dir_path)
            self.dep_dir = dir_path
        except Exception as e:
            print(str(e))
