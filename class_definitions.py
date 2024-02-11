class Parameter:
    def __init__(self, name, type_):
        self.name = name
        self.type_ = type_


class Attribute:
    def __init__(self, name, type_, visibility, isstatic):
        self.name = name
        self.type_ = type_
        if visibility:
            self.visibility = visibility
        else:
            self.visibility = "public"
        self.isStatic = isstatic


class Operation:
    def __init__(self, name, parameters, return_type, visibility, isabstract, isstatic):
        self.name = name
        self.parameters = parameters
        self.return_type = return_type
        if visibility:
            self.visibility = visibility
        else:
            self.visibility = "public"
        self.isAbstract = isabstract
        self.isStatic = isstatic


class Class:
    def __init__(self, name, attributes, operations, extended, package, isabstract):
        self.name = name
        self.attributes = attributes
        self.operations = operations
        self.extended = extended
        self.package = package
        self.isAbstract = isabstract
