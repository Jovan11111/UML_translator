# Definition of the class Parameter that is used to encapsulate operation parameters
class Parameter:
    def __init__(self, name, type_):
        # Parameter name
        self.name = name
        # Parameter type
        self.type_ = type_


# Definition of the class Attribute that is used to encapsulate class attributes
class Attribute:
    def __init__(self, name, type_, visibility, isstatic):
        # Attribute name
        self.name = name
        # Attribute type
        self.type_ = type_
        # Attribute visibility, default value is public
        if visibility:
            self.visibility = visibility
        else:
            self.visibility = "public"
        # Tells if attribute is static or not
        self.isStatic = isstatic


# Definition of the class Operation used to encapsulate class operations
class Operation:
    def __init__(self, name, parameters, return_type, visibility, isabstract, isstatic):
        # Operation name
        self.name = name
        # List of operation parameters
        self.parameters = parameters
        # Operation return type
        self.return_type = return_type
        # Operation visibility, default value is public
        if visibility:
            self.visibility = visibility
        else:
            self.visibility = "public"
        # Tells if the operation is abstract / pure virtual
        self.isAbstract = isabstract
        # tells if the operation is static
        self.isStatic = isstatic


# Definition of the class Class used to encapsulate classes on the diagram
class Class:
    def __init__(self, name, attributes, operations, extended, package, isabstract):
        # Class name
        self.name = name
        # List of class attributes
        self.attributes = attributes
        # List of class operations
        self.operations = operations
        # Contains the name of the parent class, None if class doesn't have a parent
        self.extended = extended
        # Contains the name of the package that contains the class
        self.package = package
        # Tells if the class is abstract
        self.isAbstract = isabstract
