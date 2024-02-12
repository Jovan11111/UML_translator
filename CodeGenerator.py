from abc import ABC, abstractmethod


# Abstract class CodeGenerator used as a AbstractStrategy with 1 method, generate code
class CodeGenerator(ABC):
    @abstractmethod
    def generate_code(self, classes):
        pass
