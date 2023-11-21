# FORWARD AND BACKWARD BUTTONS ON A BROWSER
class Stack:
    current_page = None
    def __init__(self):
        self.browser_page =[]

    def pages(self,page):
        self.browser_page.append(page)
        current_page = page
        # print(self.browser_page)

       
    def back(self):
        if len(self.browser_page) > 1:
            self.browser_page.pop()
        current_page = self.browser_page[-1]
        print(f'Your on the {current_page} page')
    

    
    def forward(self):
        current_page = self.browser_page[-1]
        print(f'You are now on page {current_page}')

    
Browser = Stack()

Browser.pages('Facebook')
Browser.pages('W3School.com')
Browser.pages('Instragram.com')
Browser.pages('Online compiler')
Browser.pages('Twitter.com')
print(' ')
Browser.back()
print(' ')
Browser.back()
print(' ')
Browser.forward()




# PREFIX AND POSTFIX EXPRESSIONS

import operator
def prefix(expression):
    stack = []
    operators = ['+', '-', '*', '/']
    expression = expression.split()

    for token in reversed(expression):
        if token.isdigit():
            stack.append(int(token))
        elif token in operators:
            operand1 = stack.pop()
            operand2 = stack.pop()
            result = perform(token, operand1, operand2)
            stack.append(result)

    return stack.pop()

def postfix(expression):
    stack = []
    operators = ['+', '-', '*', '/']

    for token in expression:
        if token.isdigit():
            stack.append(int(token))
        elif token in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = perform(token, operand1, operand2)
            stack.append(result)

    return stack.pop()

def perform(operator, operand1, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2

prefix_expression = "/ * 8 7 9"
postfix_expression = "4 8 + 9 *"

prefix_result = prefix(prefix_expression)
postfix_result = postfix(postfix_expression)

print("Prefix expression result:", prefix_result)
print("Postfix expression result:", postfix_result)

print(5//2)