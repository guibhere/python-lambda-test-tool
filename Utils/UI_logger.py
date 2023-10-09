import io


class OutputRedirectorQt(io.TextIOBase):
    def __init__(self, logger):
        self.logger = logger

    def write(self, string):
        self.logger.append(string)
