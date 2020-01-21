# Class name does not use proper naming conventions
# See: https://www.python.org/dev/peps/pep-0008/#class-names
class playerunit:
    hp = 0
    
    def __init__(self, hpval):
        self.hp = hpval
    
    # The indentation here makes it hard to distinguish between arguments 
    # and the method code.
    # See: https://www.python.org/dev/peps/pep-0008/#indentation
    def example_function(
        var_one, var_two, var_three,
        var_four):
        print(var_two)