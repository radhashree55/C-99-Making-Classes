class Calculator(object):
    def __init__(self, number1, operation, number2):
        self.number1 = number1
        self.operation = operation
        self.number2 = number2

    def getSolution(self):
        if self.operation == "+":
            return self.number1 + self.number2
        elif self.operation == "-":
            return self.number1 - self.number2
        elif self.operation == "*":
            return self.number1 * self.number2
        elif self.operation == "/":
            return self.number1 / self.number2
        elif self.operation == "**":
            return self.number1 ** self.number2


equation1 = Calculator(10, "**", 9)

print(equation1.getSolution())
