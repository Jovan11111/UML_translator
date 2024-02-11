from abc import ABC, abstractmethod


class CodeGenerator(ABC):
    @abstractmethod
    def generate_code(self, classes):
        pass
