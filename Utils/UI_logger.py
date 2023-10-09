import tkinter as tk
import io
import sys


class OutputRedirector(io.TextIOBase):
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, string):
        self.text_widget.insert(tk.END, string)
        self.text_widget.see(tk.END)  # Scroll to the end


class OutputRedirectorQt(io.TextIOBase):
    def __init__(self, logger):
        self.logger = logger

    def write(self, string):
        self.logger.append(string)
