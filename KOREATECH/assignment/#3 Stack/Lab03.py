class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)
        #return str(self.top)

    def __len__(self):
        return len(self.items)

    def __contains__(self, item):
        return item in self.items
    
    def __iter__(self):
        return iter(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise IndexError("Pop from an empty stack")

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        print(self.items)

    def find(self, item):
        return item in self.items

    def clear(self):
        self.items = []
        

class StackApplication:
    def __init__(self,stack):
        self.stack = stack

    def convertBase(self, num, base):
        stack = self.stack
        digits = "0123456789ABCDEF"
        
        while num > 0:
            remainder = num % base
            stack.push(digits[remainder])
            num //= base

        result = ""
        while not stack.isEmpty():
            result += stack.pop()

        return result

    def Infix2Postfix(self, expr):
        stack = self.stack
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        postfix = []

        for token in expr:
            if token.isalnum():
                postfix.append(token)
            elif token == '(':
                stack.push(token)
            elif token == ')':
                while not stack.isEmpty() and stack.peek() != '(':
                    postfix.append(stack.pop())
                stack.pop()  # Remove the '('
            else:
                while not stack.isEmpty() and stack.peek() != '(' and precedence.get(token, 0) <= precedence.get(stack.peek(), 0):
                    postfix.append(stack.pop())
                stack.push(token)

        while not stack.isEmpty():
            postfix.append(stack.pop())

        return ''.join(postfix)
    
    def Infix2Prefix(self, expr):
        stack = self.stack
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        prefix = []

        # Reverse the expression to make it easier to handle
        expr = expr[::-1]

        for token in expr:
            if token.isalnum():
                prefix.append(token)
            elif token == ')':
                stack.push(token)
            elif token == '(':
                while not stack.isEmpty() and stack.peek() != ')':
                    prefix.append(stack.pop())
                stack.pop()  # Remove the ')'
            else:
                while not stack.isEmpty() and stack.peek() != ')' and precedence.get(token, 0) <= precedence.get(stack.peek(), 0):
                    prefix.append(stack.pop())
                stack.push(token)

        while not stack.isEmpty():
            prefix.append(stack.pop())

        # Reverse the prefix expression to get the correct order
        prefix = prefix[::-1]

        return ''.join(prefix)    

    def evalPostfix(self, expr):
        stack = self.stack

        for token in expr:
            if token.isdigit():
                stack.push(int(token))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if token == '+':
                    stack.push(operand1 + operand2)
                elif token == '-':
                    stack.push(operand1 - operand2)
                elif token == '*':
                    stack.push(operand1 * operand2)
                elif token == '/':
                    stack.push(operand1 / operand2)

        return stack.pop()

    def checkBrackets(self, statement):
        stack = self.stack
        opening_brackets = "([{"
        closing_brackets = ")]}"

        for char in statement:
            if char in opening_brackets:
                stack.push(char)
            elif char in closing_brackets:
                if stack.isEmpty():
                    return False
                top = stack.pop()
                if opening_brackets.index(top) != closing_brackets.index(char):
                    return False

        return stack.isEmpty()

    