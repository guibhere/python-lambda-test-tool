import tkinter as tk
from tkinter import filedialog
import json
import os


class JsonFileManager:
    def __init__(self, root, text_box):
        self.root = root
        self.text_box = text_box

    def open_json_file(self):
        file_path = filedialog.askopenfilename(
            defaultextension=".json", filetypes=[("JSON Files", "*.json")])
        if file_path:
            with open(file_path, 'r') as file:
                json_text = file.read()
            self.text_box.delete("1.0", tk.END)
            self.text_box.insert(tk.END, json_text)

    def save_json_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json", filetypes=[("JSON Files", "*.json")])
        if file_path:
            json_text = self.text_box.get("1.0", tk.END)
            with open(file_path, 'w') as file:
                file.write(json_text)
                
    def open_json_file_selection(self,dir,file_name):
        file_path = os.path.join(dir,file_name)
        if file_path:
            with open(file_path, 'r') as file:
                json_text = file.read()
            self.text_box.delete("1.0", tk.END)
            self.text_box.insert(tk.END, json_text)


class DirectoryManager:
    def __init__(self, root, text_box,args):
        self.root = root
        self.text_box = text_box
        self.args = args

    def select_directory(self):
        file_path = filedialog.askopenfilename(
            defaultextension=".py", filetypes=[("Python lambda", "*.py")])
        return file_path
    
    def select_event_dir(self,combo_box):
        dir = filedialog.askdirectory()
        self.args[2] = dir
        self.set_combobox_value(combo_box,dir)

    def set_combobox_value(self,combo_box,dir):
        combo_box["values"]= self.list_json_files(dir)
        
    def list_json_files(self, dir):
        json_files = []
        for filename in os.listdir(dir):
            if filename.endswith(".json"):
                json_files.append(filename)
        return json_files
