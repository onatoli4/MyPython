"""
Этот файл должен содержать:
- Функцию calc(raw_expression).
- Любые вспомогательные функции.
"""

# -*- coding: utf-8 -*-

def action(a, b, symbol):
    if symbol == '+':
        return a+b
    elif symbol == '-':
        return a-b
    elif symbol == '*':
        return a*b
    elif symbol == '/':
        return a/b

def token(raw_string):
    if not raw_string: return None
    point = False
    number = ''
    output = []
    for i in raw_string:
        if i.isdigit():
            number += i
        elif i == '.':
            if point:
                return None
            number += i
            point = True
        elif i in '+-*/()':
            if number:
                output.append(number)
                number = ''
                point = False
            output.append(i)
        else:
            return None
    if number: output.append(number)
    return output

def postfix(token_list):
    if not token_list: return None
    prior = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    stack = []
    for i in token_list:
        if i == '(':
            stack.append(i)
        elif i == ')':
            while stack[-1] != '(':
                output.append(stack.pop())
                if not stack: return None
            stack.pop()
        elif i in '+-*/':
            if stack:
                while stack[-1] in '+-*/':
                    if prior[stack[-1]] >= prior[i]:
                        output.append(stack.pop())
                    else: break
                    if not stack: break
            stack.append(i)
        else:
            output.append(float(i))
    output += stack[::-1]
    return output

def result(postfix_list):
    if not postfix_list: return None
    if 0 <= len(postfix_list) <= 2: return None
    a, b = postfix_list[:2]
    if type(a) != float or type(b) != float: return None
    stack = []
    for i in postfix_list:
        if type(i) == float:
            stack.append(i)
        else:
            res = action(stack.pop(-2), stack.pop(), i)
            stack.append(res)
    return stack[0]

def calc(raw_expression):
    token_list = token(raw_expression)
    postfix_list = postfix(token_list)
    output = result(postfix_list)
    return output

if __name__ == "__main__":
    expressions = [
        "5*2-6/3+5-7-9*0",              # 6
        "2-(503*8)+1.0/7",            # -4021.85714286
#        "(1-2)*3",          # -3
#        "(1+(2/2))-(3-5)",  # 4
#        "1/2-1/2"           # 0
    ]

    for expr in expressions:
        print(f"{expr} = {calc(expr)}")
        




