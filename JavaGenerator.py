import os
from CodeGenerator import CodeGenerator


class JavaGenerator(CodeGenerator):
    def generate_code(self, classes):
        for cls in classes:
            directory_path = f"java_project/{cls.package}"

            if not os.path.exists(directory_path):
                os.makedirs(directory_path)

            file_name = f"{directory_path}/{cls.name}.java"
            with open(file_name, "w") as file:
                java_code = f"package {cls.package}; \n\n"
                java_code += "public "
                if cls.isAbstract:
                    java_code += "abstract "
                java_code += f"class {cls.name}"
                if cls.extended:
                    java_code += f" extends {cls.extended}"
                java_code += " {\n"
                for attr in cls.attributes:
                    staticAttribute = ""
                    if attr.isStatic:
                        staticAttribute = "static"
                    if attr.visibility == "package":
                        java_code += f"\t{attr.type_} {staticAttribute} {attr.name};\n"
                    else:
                        java_code += f"\t{attr.visibility} {staticAttribute} {attr.type_} {attr.name};\n"
                for op in cls.operations:
                    parameters_str = ', '.join([f'{p.type_} {p.name}' for p in op.parameters])
                    staticOperation = ""
                    if op.isStatic:
                        staticOperation = "static"
                    if op.isAbstract:
                        java_code += f"\t{op.visibility} {staticOperation} abstract {op.return_type} {op.name}({parameters_str});\n"
                    else:
                        java_code += f"\t{op.visibility} {staticOperation} {op.return_type} {op.name}({parameters_str}) "
                        java_code += "{\n\t\t// Add method implementation\n\t}\n"

                java_code += "}\n\n"
                file.write(java_code)
