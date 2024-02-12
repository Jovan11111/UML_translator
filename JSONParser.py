import json
from class_definitions import *


# Definition of the Utility class JSONParser that parses and prints the json data from .mdj file
class JSONParser:
    # Static method that opens the mdj file
    @staticmethod
    def open_mdj(path):
        with open(path, "r") as file:
            return json.load(file)

    # Static method that parses the json file
    @staticmethod
    def extract_classes(json_data):
        # List used to hold all classes
        classes = []
        for modelElement in json_data["ownedElements"]:
            # Looking for UMLModels
            if modelElement["_type"] == "UMLModel":
                for packageElement in modelElement["ownedElements"]:
                    # Looking for packages
                    if packageElement["_type"] == "UMLPackage":
                        # Holds package name
                        package = packageElement["name"]
                        for classElement in packageElement["ownedElements"]:
                            # Looking for classes
                            if classElement["_type"] == "UMLClass":
                                # Holds class attributes
                                attributes = []
                                # Holds class operations
                                operations = []
                                # Holds parent class / False if there is no parent
                                extended = False
                                # Holds boolean value on if class is abstract
                                abstractClass = False

                                if classElement.get("isAbstract", False):
                                    abstractClass = True

                                # Looking for parent class
                                for oel in classElement.get("ownedElements", []):
                                    # Looking for generalization symbol
                                    if oel["_type"] == "UMLGeneralization":
                                        # Target holds id of the parent class
                                        extended = oel["target"]["$ref"]
                                        for oel1 in packageElement["ownedElements"]:
                                            # Looking for the class that has the same id as the target
                                            if oel1["_type"] == "UMLClass" and oel1["_id"] == extended:
                                                extended = oel1["name"]
                                                break

                                # Parsing attributes and encapsulating them
                                for attribute in classElement.get("attributes", []):
                                    staticAttribute = False
                                    if attribute.get("isStatic", False):
                                        staticAttribute = True
                                    attributes.append(
                                        Attribute(attribute["name"], attribute["type"], attribute.get("visibility"),
                                                  staticAttribute))
                                # Parsing operations and encapsulating them
                                for operation in classElement.get("operations", []):
                                    abstractOperation = False
                                    staticOperation = False
                                    parameters = []
                                    ret = ""
                                    retExists = False
                                    if operation.get("isAbstract", False):
                                        abstractOperation = True
                                    if operation.get("isStatic", False):
                                        staticOperation = True
                                    for parameter in operation.get("parameters", []):
                                        if parameter.get("direction") == "return":
                                            ret = parameter["type"]
                                            retExists = True
                                        else:
                                            parameters.append(Parameter(parameter["name"], parameter["type"]))
                                    # If there is no return parameter in parameters, then the return type is void
                                    if not retExists:
                                        ret = "void"
                                    operations.append(
                                        Operation(operation["name"], parameters, ret, operation.get("visibility"),
                                                  abstractOperation, staticOperation))

                                # Adding a class to the list
                                classes.append(Class(classElement["name"], attributes, operations, extended, package,
                                                     abstractClass))
        return classes

    # Static method that prints the extracted classes
    @staticmethod
    def printParsedJSON(extracted_classes):
        for cls in extracted_classes:
            print(f"Class: {cls.name} extends {cls.extended}")
            print("Attributes:")
            for attr in cls.attributes:
                print(f"- {attr.visibility} {attr.name}: {attr.type_}")
            print("Operations:")
            for op in cls.operations:
                parameters_str = ', '.join([f'{p.name}: {p.type_}' for p in op.parameters])
                print(f"- {op.visibility} {op.name}({parameters_str}) -> {op.return_type}")
            print()
