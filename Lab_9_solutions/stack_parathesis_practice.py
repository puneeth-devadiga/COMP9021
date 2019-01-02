# Written by Eric Martin for COMP9021



'''
Uses the stack_adt module to evaluate an arithmetic expression
written in infix, fully parenthesised with parentheses, brackets and braces,
and built from natural numbers using the binary +, -, * and / operators.
'''


import re
from operator import add, sub, mul, truediv

from stack_adt import Stack, EmptyStackError


def evaluate(expression):

    if any(not (c.isdigit() or c.isspace() or c in '()[]{}+-*/') for c in expression):
        return
    # Tokens can be natural numbers, (, ), [, ], {, }, +, -, *, and /
    tokens = re.compile('(\d+|\(|\)|\[|\]|{|}|\+|-|\*|/)').findall(expression)
    
    #try:
    parentheses = {')': '(', ']': '[', '}': '{'}
    stack = Stack()
    for token in tokens:
        try:
            token = int(token)
        except ValueError:
            pass
        if token not in parentheses:
            stack.push(token)
        else:
            try:
                arg_2 = stack.pop()
                operator = stack.pop()
                arg_1 = stack.pop()
                opening_group_symbol = stack.pop()
                if parentheses[token] != opening_group_symbol:
                    return
                stack.push({'+': add, '-': sub, '*': mul, '/': truediv}[operator](arg_1, arg_2))
            except EmptyStackError:
                return
    if stack.is_empty():
        return
    value = stack.pop()
    if not stack.is_empty():
        return
    return value
    #except ZeroDivisionError:
        #return
