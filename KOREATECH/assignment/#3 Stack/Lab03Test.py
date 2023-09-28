from Lab03 import * 

def useStack():
    # Create an instance of the Stack class
    stack = Stack()

    # Test the push method
    for i in range (20):
        stack.push(i)
        
    print("")
    for i in stack:
        print(i)

    # Test the __str__ method
    print("Stack:", stack)

    # Test the size method
    print("Size:", len(stack))

    # Test the __contains__ method
    print("Is 3 in stack?", 3 in stack)

    # Test the pop method
    popped_item = stack.pop()
    print("Popped item:", popped_item)

    # Test the peek method
    top_item = stack.peek()
    print("Top item:", top_item)

    # Test the isEmpty method
    print("Is stack empty?", stack.isEmpty())

    # Test the display method
    stack.display()

    # Test the find method
    print("Is 2 in stack?", stack.find(2))

    # Test the clear method
    stack.clear()
    print("Stack after clearing:", stack)

def useStackApplication():
    
    odd = Stack()
    for i in range (20):
        odd.push(str(i))
    
    app = StackApplication(odd)

    # Testing convertBase method
    decimal_number = 42
    binary = app.convertBase(decimal_number, 2)
    octal = app.convertBase(decimal_number, 8)
    hexadecimal = app.convertBase(decimal_number, 16)

    print(f"Decimal: {decimal_number}")
    print(f"Binary: {binary}")
    print(f"Octal: {octal}")
    print(f"Hexadecimal: {hexadecimal}")

    # Testing Infix2Postfix method
    infix_expression = "2+(4+3*2+1)/3"
    postfix = app.Infix2Postfix(infix_expression)
    prefix = app.Infix2Prefix(infix_expression)
    print(f"Infix: {infix_expression}")
    print(f"Prefix: {prefix}")
    print(f"Postfix: {postfix}")

    # Testing evalPostfix method
    postfix_expression = "34+5*"
    result = app.evalPostfix(postfix_expression)
    print(f"Result of {postfix} is {result}")

    # Testing checkBrackets method
    statement = "{[()()]}"
    if app.checkBrackets(statement):
        print(f"The brackets in {statement} are balanced.")
    else:
        print(f"The brackets in {statement} are not balanced.")

if __name__ == "__main__":
    useStackApplication()
    # useStack()