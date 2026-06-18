class Calculator:
    """
    Monitor a simply calculator
    """

    def add(self, a, b):

        return a + b 
    
    def subtract(self, a, b):

        return a - b 

    def multiply(self, a, b):

        return a*b 

    def divide(self, a, b):
        if b == 0:
            raise ValueError("b can't be 0")
        return a/b 

calculator = Calculator()

print(calculator.add(5,0))