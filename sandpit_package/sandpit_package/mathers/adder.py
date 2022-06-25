from sandpit_package.mathers.operation import Operation

class Adder(Operation):

    def _op_str(self):
        return "+"

    def result(self):
        return self.l + self.r

