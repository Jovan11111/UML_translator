from CodeGenerator import CodeGenerator


# Definition of the CppGenerator class used as ConcreteStrategy that implements a method generateCode
class CppGenerator(CodeGenerator):
    def generate_code(self, classes):
        for cls in classes:
            # Write class declaration to header file
            header_file_name = f"cpp_project/{cls.name}.hpp"
            with open(header_file_name, "w") as header_file:
                # Write ifndef statements at the beginning
                header_code = f"#ifndef {cls.name.upper()}_HPP\n#define {cls.name.upper()}_HPP\n\n"
                # Write the name of the class
                header_code += f"class {cls.name}"
                # If class is extended, add that it's extended
                if cls.extended:
                    header_code += f" : public {cls.extended}"

                # Write private section of the class first
                header_code += " {\nprivate:\n"
                # Write private attributes using writeAttributes function
                header_code += writeAttributes("private", cls)
                # Write private operations using writeOperations function
                header_code += writeOperations("private", cls)

                # Write the protected section
                header_code += "protected:\n"
                # Write protected attributes using writeAttributes function
                header_code += writeAttributes("protected", cls)
                # Write protected operations using writeOperations function
                header_code += writeOperations("protected", cls)

                # Write the public section
                header_code += "public:\n"
                # Write public attributes using writeAttributes function
                header_code += writeAttributes("public", cls)
                # As c++ doesn't have package visibility, these attributes will be public
                header_code += writeAttributes("package", cls)
                # Write public operations using writeOperations function
                header_code += writeOperations("public", cls)
                # As c++ doesn't have package visibility, these operations will be public
                header_code += writeOperations("package", cls)

                # Close the ifndef statements
                header_code += "};\n\n#endif // "
                header_code += f"{cls.name.upper()}_HPP"
                # Write the whole header code to the header file
                header_file.write(header_code)

            # Write method implementations to source file
            source_file_name = f"cpp_project/{cls.name}.cpp"
            with open(source_file_name, "w") as source_file:
                # Include the header file to the source file
                source_code = f"#include \"{cls.name}.hpp\"\n\n"
                for op in cls.operations:
                    # If class is abstract it doesn't need implementation
                    if not op.isAbstract:
                        staticOperation = ""
                        if op.isStatic:
                            staticOperation = "static "
                        parameters_str = ', '.join([f'{p.type_} {p.name}' for p in op.parameters])
                        source_code += f"{staticOperation}{op.return_type} {cls.name}::{op.name}({parameters_str}) "
                        source_code += "{\n\t// Add method implementation\n}\n\n"
                # Write the whole source code to the source file
                source_file.write(source_code)


def writeAttributes(visibility, cls):
    ret = ""
    for attr in cls.attributes:
        if attr.visibility == visibility:
            # If attribute is static, this string will be "static"
            staticAttribute = ""
            if attr.isStatic:
                staticAttribute = "static "
            # Write the attribute in the correct form
            ret += f"\t{staticAttribute}{attr.type_} {attr.name};\n"
    return ret


def writeOperations(visibility, cls):
    ret = ""
    for op in cls.operations:
        if op.visibility == visibility:
            # If operation is static, this string will be "static"
            staticOperation = ""
            if op.isStatic:
                staticOperation = "static "
            parameters_str = ", ".join([f"{p.type_} {p.name}" for p in op.parameters])
            # If operation is abstract, if has " = 0" at the end, otherwise not
            # Write the operation declaration in the correct form
            if op.isAbstract:
                ret += f"\t{staticOperation}{op.return_type} {op.name}({parameters_str}) = 0;\n"
            else:
                ret += f"\t{staticOperation}{op.return_type} {op.name}({parameters_str});\n"
    return ret
