# Written by Eric Martin for COMP9021



'''
Uses the stack_adt module to evaluate an arithmetic expression
written in infix, fully parenthesised with parentheses, brackets and braces,
and built from natural numbers using the binary +, -, * and / operators.
'''

import re
from stack_adt import Stack, EmptyStackError
from operator import add, sub, mul, truediv

def evaluate(expression):
	
    for c in expression:
        if not c.isdigit() and not c.isspace() and c not in '()[]{}+-*/':
            return 
    tokens = re.compile('(\d+|\(|\)|\[|\]|{|}|\+|-|\*|/)').findall(expression)

    try:
        paranthesis = {')':'(', '}':'{', '}':'['}

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
                    arg_1 = stack.pop()
                    operator = stack.pop()
                    arg_2 = stack.pop()
                    opening_paranthesis = stack.pop()
                    
                    if opening_paranthesis != paranthesis[token]:
                        return
                    stack.push({'+':add, '-':sub, '*': mul, '/':truediv}[operator](arg_1, arg_2))
                except EmptyStackError:
                    return 
        if stack.is_empty():
            return 

        value = stack.pop()

       

        return value
    except ZeroDivisionError:
        return 

