class Contract(object):
    def __init__(self, name='', variables=[], assumptions=[], guarantees=[]):
        """Initialize a contract object"""
        self.name = name
        self.variables = variables
        self.assumptions = assumptions
        self.guarantees = guarantees

    def add_name(self, name):
        """Assigns the contract a name"""
        self.name = name[0]

    def add_variables(self, variables):
        """Assigns the contract variables"""
        self.variables = variables

    def add_assumptions(self, assumptions):
        """Assigns the contract assumptions"""
        self.assumptions = assumptions

    def add_guarantees(self, guarantees):
        """Assigns the contract guarantees"""
        self.guarantees = guarantees
