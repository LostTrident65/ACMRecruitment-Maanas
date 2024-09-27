class Calculator:
    def __init__(self):
        self.operators = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide,
            '^': self.exponent,
        }

    # basic calculations
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Error: Division by zero")  # Error handling for division by zero
        return a / b

    # Advanced 
    def exponent(self, a, b):
        return a ** b
    
    def square_root(self, a):
        if a < 0:
            raise ValueError("Error: Square root of a negative number")
        return a ** 0.5

    # determine precedence of operators
    def precedence(self, operator):
        if operator in ('+', '-'):
            return 1
        if operator in ('*', '/'):
            return 2
        if operator == '^':
            return 3
        return 0

    # apply operator to two numbers
    def apply_operator(self, operators, values):
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        values.append(self.operators[operator](left, right))

    # evaluate expression with parentheses and operator precedence 
    def evaluate(self, expression):
        values = []  
        operators = []  
        i = 0

        while i < len(expression):
            if expression[i] == ' ':
                i += 1
                continue

            # Number handling 
            if expression[i].isdigit() or (expression[i] == '-' and (i == 0 or expression[i-1] in '()+-*/^')):
                num = ''
                while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                    num += expression[i]
                    i += 1
                values.append(float(num) if '.' in num else int(num))
                continue

            # handle left parenthesis
            elif expression[i] == '(':
                operators.append(expression[i])

            # handle right parenthesis
            elif expression[i] == ')':
                while operators and operators[-1] != '(':
                    self.apply_operator(operators, values)
                operators.pop()  

            # Handle operators
            elif expression[i] == '√':  # Square root handling
                i += 1  # Move past the √ symbol
                num = ''
                while i < len(expression) and expression[i].isdigit():
                    num += expression[i]
                    i += 1
                values.append(self.square_root(float(num)))

            else:
                while operators and self.precedence(operators[-1]) >= self.precedence(expression[i]):
                    self.apply_operator(operators, values)
                operators.append(expression[i])

            i += 1

        # Apply remaining operators
        while operators:
            self.apply_operator(operators, values)

        return values[0]

# Main program for user input
if __name__ == "__main__":
    calc = Calculator()

    while True:
        try:
            # Get user input for the expression
            expression = input("Enter a mathematical expression (or type 'exit' to quit): ")
            if expression.lower() == 'exit':
                break
            
            # Replace sqrt with √ symbol for square root and evaluate the expression
            expression = expression.replace("sqrt", "√")
            result = calc.evaluate(expression)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")
