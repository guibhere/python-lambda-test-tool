import os
from PyQt5.QtWidgets import QFileDialog


class File_Helper:
    def __init__(self):
        self.file_dialog = QFileDialog()

    def selecionar_lambda(self):
        file_path, filter = self.file_dialog.getOpenFileName(
            None, "Selecione a lambda function", "", "Python Files (*.py)"
        )
        return file_path

    def selecionar_diretorio(self):
        dir = self.file_dialog.getExistingDirectory(
            None, "Selecione o diretorio de eventos", ""
        )
        return dir

    def salvar_json(self, dir, data):
        save_path, _ = self.file_dialog.getSaveFileName(
            None,
            directory=dir,
            caption="Save JSON File",
            filter="JSON Files (*.json);;All Files (*)",
        )
        file_name = os.path.basename(save_path)

        if save_path:
            with open(save_path, "w") as file:
                file.write(data)

        return file_name

    def list_json_files(self, dir):
        try:
            json_files = []
            for filename in os.listdir(dir):
                if filename.endswith(".json"):
                    json_files.append(filename)
            return json_files
        except Exception as e:
            print("Não foi possivel encontrar o diretorio")
            return json_files

    def read_file(self, dir, file_name):
        file_path = os.path.join(dir, file_name)
        if file_path:
            with open(file_path, "r") as file:
                json_text = file.read()
        return json_text

    def carregar_json_file(self, dir):
        file_path, filter = self.file_dialog.getOpenFileName(
            None,
            directory=dir,
            caption="Selecione o evento .json",
            filter="Json Files (*.json)",
        )
        return self.read_file("", file_path)

    def carregar_requirements_file(self):
        file_path, filter = self.file_dialog.getOpenFileName(
            None,
            caption="Selecione o arquivo requirements",
            filter="Requirements (*.txt)",
        )
        return self.read_file("", file_path)
