
import re
from operator import add, sub, mul, truediv
from stack_adt import Stack, EmptyStackError

def evaluate(expression):

    for c in expression:
        if not c.isdigit() and not c.isspace() and c not in '(){}[]+-*/':
            return 

    tokens = re.compile('(\d+|\(|\)|{|}|\[|\]|\+|-|\*|/)').findall(expression)

    try:
        paranthesis = {')':'(', ']':'[', '}':'{'}

        stack = Stack()
        

        for token in tokens:
            try:
                token = int(token)
            except ValueError:
                pass

            if token not in paranthesis:
                stack.push(token)
            else:
                try:
                    arg1= stack.pop()
                    operator = stack.pop()
                    arg2 = stack.pop()
                    opening_paranthesis = stack.pop()

                    if opening_paranthesis != paranthesis[token]:
                        return 
                    stack.push({'+':add, '-':sub, '*':mul, '/':truediv}[operator](arg1, arg2))
                except EmptyStackError:
                    return

        if stack.is_empty():
            return

        value = stack.pop()

        if not stack.is_empty():
            return

        return value
    except ZeroDivisionError:
        return
            

        
            

    
