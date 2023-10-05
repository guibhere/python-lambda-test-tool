import subprocess
import os
from tkinter import filedialog

class DependencyInstaller:
    def __init__(self,requirements):
        self.requirements = requirements
        
    def InstalarDependenciasTester(self):
        subprocess.call(['pip', 'install', 'tkinter'])
        
    def InstalarDependenciasRequirements(self):
        subprocess.call(['pip', 'install', '-r', 'requirements.txt'])
        
    def InstalarDependenciasNovasRequirements(self):
        self.pacotes_instalados = self.ListaPacotes()
        print("Pacotes Instalados: ",self.pacotes_instalados)
        if not os.path.exists(self.requirements):
            self.requirements = filedialog.askopenfilename(
                defaultextension=".txt", filetypes=[("Requirements", "*.txt")])
        with open(self.requirements, 'r') as f:
            pacotes = f.read().split('\n')
        for pacote in pacotes:
            if pacote.strip() not in self.pacotes_instalados:
                subprocess.call(['pip', 'install', pacote])
                
    def ListaPacotes(self):
        return subprocess.check_output(['pip', 'freeze']).decode('utf-8').split('\n')