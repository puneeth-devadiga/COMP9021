

from operator import add, sub, mul, truediv

from stack_adt import Stack

def evaluate_postfix_expression(expression):

    stack = Stack()
    first_digit = False
    for e in expression:
        if e.isdigit():
            if first_digit == False:
                stack.push(int(e))
                first_digit = True
            else:
                stack.push(stack.pop()*10 +int(e))
        else:
            first_digit = False
            if e in '+-*/':
                arg_1 = stack.pop()
                arg_2 = stack.pop()
                stack.push({'+':add, '-':sub, '*':mul, '/': truediv}[e](arg_1, arg_2))

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


            
            
