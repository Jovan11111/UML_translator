from JSONParser import JSONParser
from JavaGenerator import JavaGenerator
from CppGenerator import CppGenerator
from Translator import Translator

if __name__ == '__main__':

    # Create an instance of the Translator
    translator = Translator(JSONParser(), JavaGenerator())

    # Translate UML file to Java
    translator.translate("test.mdj")

    # Switch to C++ code generation
    translator.set_code_generator(CppGenerator())

    # Translate UML file to C++
    translator.translate("test.mdj")
