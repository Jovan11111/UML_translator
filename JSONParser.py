import json
from class_definitions import *


class JSONParser:
    @staticmethod
    def open_mdj(path):
        with open(path, "r") as file:
            return json.load(file)

    @staticmethod
    def extract_classes(json_data):
        classes = []
        for modelElement in json_data["ownedElements"]:
            if modelElement["_type"] == "UMLModel":
                for packageElement in modelElement["ownedElements"]:
                    if packageElement["_type"] == "UMLPackage":
                        package = packageElement["name"]
                        for classElement in packageElement["ownedElements"]:
                            if classElement["_type"] == "UMLClass":
                                attributes = []
                                operations = []
                                extended = False
                                abstractClass = False

                                if classElement.get("isAbstract", False):
                                    abstractClass = True
                                for oel in classElement.get("ownedElements", []):
                                    if oel["_type"] == "UMLGeneralization":
                                        extended = oel["target"]["$ref"]
                                        for oel1 in packageElement["ownedElements"]:
                                            if oel1["_type"] == "UMLClass" and oel1["_id"] == extended:
                                                extended = oel1["name"]
                                                break

                                for attribute in classElement.get("attributes", []):
                                    staticAttribute = False
                                    if attribute.get("isStatic", False):
                                        staticAttribute = True
                                    attributes.append(
                                        Attribute(attribute["name"], attribute["type"], attribute.get("visibility"),
                                                  staticAttribute))
                                for operation in classElement.get("operations", []):
                                    abstractOperation = False
                                    staticOperation = False
                                    parameters = []
                                    ret = ""
                                    if operation.get("isAbstract", False):
                                        abstractOperation = True
                                    if operation.get("isStatic", False):
                                        staticOperation = True
                                    for parameter in operation.get("parameters", []):
                                        if parameter.get("direction") == "return":
                                            ret = parameter["type"]
                                        else:
                                            parameters.append(Parameter(parameter["name"], parameter["type"]))
                                    operations.append(

                                        Operation(operation["name"], parameters, ret, operation.get("visibility"),
                                                  abstractOperation, staticOperation))

                                classes.append(Class(classElement["name"], attributes, operations, extended, package,
                                                     abstractClass))
        return classes

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
