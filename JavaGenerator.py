import os
from CodeGenerator import CodeGenerator


# Definition the JavaGenerator class used as Concrete Strategy that implements a method generate_code
class JavaGenerator(CodeGenerator):
    def generate_code(self, classes):
        for cls in classes:
            # Correct path to the class
            directory_path = f"java_project/{cls.package}"

            # If it's the first class in that package, make the package dir
            if not os.path.exists(directory_path):
                os.makedirs(directory_path)

            # Full file name
            file_name = f"{directory_path}/{cls.name}.java"
            with open(file_name, "w") as file:
                # First line tells to which packet the class belongs to
                java_code = f"package {cls.package}; \n\n"
                # Class is considered to always be public
                java_code += "public "
                # If class is abstract, it need to have the keyword
                if cls.isAbstract:
                    java_code += "abstract "
                # Name of the class
                java_code += f"class {cls.name}"
                # If class has a parent, write that class is extended
                if cls.extended:
                    java_code += f" extends {cls.extended}"
                java_code += " {\n"

                for attr in cls.attributes:
                    # If attribute is static, this will be "static"
                    staticAttribute = ""
                    if attr.isStatic:
                        staticAttribute = "static "
                    # If visibility of the attribute is package, it doesn't need to be written in the declaration
                    # Write the attribute declaration in the correct form
                    if attr.visibility == "package":
                        java_code += f"\t{attr.type_} {staticAttribute}{attr.name};\n"
                    else:
                        java_code += f"\t{attr.visibility} {staticAttribute}{attr.type_} {attr.name};\n"

                for op in cls.operations:
                    parameters_str = ', '.join([f'{p.type_} {p.name}' for p in op.parameters])
                    # If operation is static, this will be "static"
                    staticOperation = ""
                    if op.isStatic:
                        staticOperation = "static "
                    # If operation is abstract, thiss will be "abstract"
                    abstractOperation = ""
                    if op.isAbstract:
                        abstractOperation = "abstract "
                    # If visibility of the operation is package, it doesn't need to be written in the declaration
                    # Write the operation declaration in the correct form
                    if op.visibility == "package":
                        java_code += f"\t{staticOperation}{abstractOperation}{op.return_type} {op.name}({parameters_str});\n"
                    else:
                        java_code += f"\t{op.visibility} {staticOperation}{abstractOperation}{op.return_type} {op.name}({parameters_str}) "
                        java_code += "{\n\t\t// Add method implementation\n\t}\n"

                java_code += "}\n\n"
                # Write everything to java file
                file.write(java_code)
