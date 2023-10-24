import io
import sys

class OutputRedirectorQt(io.TextIOBase):
    def __init__(self, logger):
        self.logger = logger
        self.terminal = sys.stdout
        self.terminal_logger = True

    def write(self, string):
        if(self.terminal_logger):
            self.terminal.write(string)
        self.logger.append(string)
