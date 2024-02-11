from CodeGenerator import CodeGenerator


class CppGenerator(CodeGenerator):
    def generate_code(self, classes):
        for cls in classes:
            # Write class declaration to header file
            header_file_name = f"cpp_project/{cls.name}.hpp"
            with open(header_file_name, "w") as header_file:
                header_code = f"#ifndef {cls.name.upper()}_HPP\n#define {cls.name.upper()}_HPP\n\n"
                header_code += f"class {cls.name}"
                if cls.extended:
                    header_code += f" : public {cls.extended}"
                header_code += " {\nprivate:\n"
                for attr in cls.attributes:
                    if attr.visibility == "private":
                        staticAttribute = ""
                        if attr.isStatic:
                            staticAttribute = "static "
                        header_code += f"\t{staticAttribute}{attr.type_} {attr.name};\n"
                for op in cls.operations:
                    if op.visibility == "private":
                        staticOperation = ""
                        if op.isStatic:
                            staticOperation = "static "
                        parameters_str = ", ".join([f"{p.type_} {p.name}" for p in op.parameters])
                        if op.isAbstract:
                            header_code += f"\t{staticOperation}{op.return_type} {op.name}({parameters_str}) = 0;\n"
                        else:
                            header_code += f"\t{staticOperation}{op.return_type} {op.name}({parameters_str});\n"
                header_code += "protected:\n"
                for attr in cls.attributes:
                    if attr.visibility == "protected":
                        staticAttribute = ""
                        if attr.isStatic:
                            staticAttribute = "static "
                        header_code += f"\t{staticAttribute}{attr.type_} {attr.name};\n"
                for op in cls.operations:
                    if op.visibility == "protected":
                        staticOperation = ""
                        if op.isStatic:
                            staticOperation = "static "
                        parameters_str = ", ".join([f"{p.type_} {p.name}" for p in op.parameters])
                        if op.isAbstract:
                            header_code += f"\t{staticOperation}{op.return_type} {op.name}({parameters_str}) = 0;\n"
                        else:
                            header_code += f"\t{staticOperation}{op.return_type} {op.name}({parameters_str});\n"
                header_code += "public:\n"
                for attr in cls.attributes:
                    if attr.visibility == "public" or attr.visibility == "package":
                        staticAttribute = ""
                        if attr.isStatic:
                            staticAttribute = "static "
                        header_code += f"\t{staticAttribute}{attr.type_} {attr.name};\n"
                for op in cls.operations:
                    if op.visibility == "public" or op.visibility == "package":
                        staticOperation = ""
                        if op.isStatic:
                            staticOperation = "static "
                        parameters_str = ', '.join([f'{p.type_} {p.name}' for p in op.parameters])
                        if op.isAbstract:
                            header_code += f"\t{staticOperation}{op.return_type} {op.name}({parameters_str}) = 0;\n"
                        else:
                            header_code += f"\t{staticOperation}{op.return_type} {op.name}({parameters_str});\n"

                header_code += "};\n\n#endif // "
                header_code += f"{cls.name.upper()}_HPP"
                header_file.write(header_code)

            # Write method implementations to source file
            source_file_name = f"cpp_project/{cls.name}.cpp"
            with open(source_file_name, "w") as source_file:
                source_code = f"#include \"{cls.name}.hpp\"\n\n"
                for op in cls.operations:
                    if not op.isAbstract:
                        staticOperation = ""
                        if op.isStatic:
                            staticOperation = "static "
                        parameters_str = ', '.join([f'{p.type_} {p.name}' for p in op.parameters])
                        source_code += f"{staticOperation}{op.return_type} {cls.name}::{op.name}({parameters_str}) "
                        source_code += "{\n\t// Add method implementation\n}\n\n"
                source_file.write(source_code)
