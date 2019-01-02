
from operator import add, sub, mul, truediv
from stack_adt import Stack, EmptyStackError

def evaluate_postfix_expression(expression):
    
    stack = Stack()
    in_number = False
    for e in expression:
        if e.isdigit():
            if in_number == False:
                stack.push(int(e))
                in_number = True
            else:
                stack.push(stack.pop() * 10 + int(e))
        else:
            in_number = False
            if e in '+-*/':
                arg_1 = stack.pop()
                arg_2 = stack.pop()
                stack.push({'+': add, '-': sub, '*': mul, '/': truediv}[e](arg_1, arg_2))

    if stack.is_empty():
        return
    value = stack.pop()
    if not stack.is_empty():
        return
    return value                    

print(evaluate_postfix_expression('213'))
print(evaluate_postfix_expression('213 2 +'))
print(evaluate_postfix_expression('213 2 + 7 8 - +'))
print(evaluate_postfix_expression('2 3 5 + *'))

