# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 11:34:04 2020

@author: Kami
"""

import itertools
testdigits = range(1,10)
# Shunting-yard_algorithm
##https://en.wikipedia.org/wiki/Shunting-yard_algorithm
        
def op_prec(char):
    if char == '*' or char == '/':
        return 3
    else:
        return 2

def str_to_stack(exp):
    output = ''
    oper_stack = ''
    q_num = 0
    for char in exp:
        if char.isdigit() or char == '?':
            output += char
            if char == '?': q_num += 1
        elif char in ['+','-','*','/']:
            while(oper_stack and oper_stack[0] != '(' and
                  op_prec(oper_stack[0]) >= op_prec(char)):
                output += oper_stack[0]
                oper_stack = oper_stack[1:]
            oper_stack = char + oper_stack
        elif char == '(':
            oper_stack = char + oper_stack
        elif char == ')':
            while(oper_stack[0] != '('):
                output += oper_stack[0]
                oper_stack = oper_stack[1:]
            if oper_stack and oper_stack[0] == '(':
                oper_stack = oper_stack[1:]
    return (output + oper_stack, q_num)

def eval(stack, test):
    nums = test.copy()
    ans = []
    for char in stack:
        if char.isdigit():
            ans.append(int(char))
        elif char == '?':
            ans.append(nums.pop(0))
        elif char in ['+','-','*','/']:
            b = ans.pop()
            a = ans.pop()
            if char == '+': c = a + b
            elif char == '-': c = a - b
            elif char == '*': c = a * b
            elif char == '/': c = a / b
            ans.append(c)
    return ans[0]

def print_ans(exp, nums):
    temp_exp = exp
    while nums:
        temp_exp = temp_exp.replace('?',str(nums.pop(0)), 1)
    print(temp_exp)

print('PNG digit question solver\n ------Designed by Haoming Jin------')
print('All unknown numbers are 1-9 and don\'t repeat, allowed operators are +-*/()')
print('Acceptable formats examples: ?+?=9\t? + 1 = 9\t(1+?)/4 = 1.5\t 2+?*4 = 14\t?*?*?+?=295')
while (True):
    exp = input('Enter the equation, type unknown number as "?", type "exit" to quit:\n')
    if exp == 'exit': break
    exp = exp.replace(' ','')
    try:
        (ques,ans) = exp.split('=')
        ans = float(ans)
        (stack,q_num) = str_to_stack(ques)
        is_found = False
        print('Answer:')
        for test in itertools.permutations(testdigits, r = q_num):
            test = list(test)
            if eval(stack, test) == ans:
                is_found = True
                print_ans(exp, test)
        if not is_found:
            print('Not Found')
    except:
        print('Input Error')