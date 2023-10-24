import subprocess
import os
from src.Utils.file_helper import File_Helper


class DependencyInstaller:
    def __init__(self, requirements):
        self.requirements = requirements
        self.file_helper = File_Helper()

    def InstalarDependenciasTester(self):
        subprocess.call(["pip", "install", "tkinter"])

    def InstalarDependenciasRequirements(self):
        subprocess.call(["pip", "install", "-r", "requirements.txt"])

    def InstalarDependenciasNovasRequirements(self):
        self.pacotes_instalados = self.ListaPacotes()
        print("Pacotes Instalados: ", self.pacotes_instalados)

        if os.path.exists(self.requirements):
            requirements = self.file_helper.read_file("", self.requirements)
        else:
            requirements = self.file_helper.carregar_requirements_file()
        pacotes = requirements.split("\n")
        for pacote in pacotes:
            if pacote.strip() not in self.pacotes_instalados:
                subprocess.call(["pip", "install", pacote])

    def ListaPacotes(self):
        return subprocess.check_output(["pip", "freeze"]).decode("utf-8").split("\n")
