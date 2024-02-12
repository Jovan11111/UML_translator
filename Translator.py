import os

class Translator:
    _instance = None  # Class attribute to hold the single instance

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, parser, code_generator):
        self.parser = parser
        self.code_generator = code_generator

    def set_code_generator(self, code_generator):
        self.code_generator = code_generator

    def translate(self, file_path):
        data = self.parser.open_mdj(file_path)
        classes = self.parser.extract_classes(data)
        self.code_generator.generate_code(classes)
