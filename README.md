# UML to Code Translator
This project is a Python-based tool for translating UML (Unified Modeling Language) diagrams stored in .mdj (MagicDraw) files into Java and C++ code. It provides a convenient way to automate the process of generating code from UML diagrams, saving time and effort for developers.

## Features
- Parses .mdj files to extract UML diagrams using JSON parsing.
- Supports translation of UML class diagrams into Java and C++ code.
- Generates class files with attributes, methods, and inheritance relationships based on the UML diagrams.
- Supports both Java and C++ code generation from the same UML diagrams.

## Installation
Clone this repository to your local machine:
git clone https://github.com/Jovan11111/UML_translator.git

Navigate to the project directory:
cd UML_translator

## Usage
Prepare your UML diagrams in .mdj format using MagicDraw or any compatible tool, and save them in project directory(where test files are saved). From the default to the name of you file.
Ensure that your UML diagrams follow the required conventions for class structure, attributes, methods, and inheritance relationships.
Run the translator script with the path to your .mdj file:
python main.py

## Constraints
- All classes in .mdj files have to be in packages.
  
## Contributing
Contributions are welcome.



