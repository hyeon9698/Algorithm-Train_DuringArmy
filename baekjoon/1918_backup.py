# 후위 표기식 postfix notation


# 반례 (A+B)*C-D
import sys
sys.stdin = open('input.txt', 'r')
expression = input()
expression = '(' + expression + ')'
stack = []
ans = []
final_ans = []
stack_finished = False
def process():
    pass
for i in range(len(expression)):
    stack.append(expression[i])
    if expression[i] == ')':
        stack.pop()
        tmp = []
        while True:
            now = stack.pop()
            if now != '(':
                tmp.append(now)
            else:
                for i in tmp:
                    if i == '*' or i == '/' or i == '+' or i == '-':
                        ans = [i] + ans
                    else:
                        ans = ans + [i]
                # print(ans[::-1])
                break
    # print(len(stack))
    if len(stack) == 1:
        stack_finished = True
        final_ans += ans[::-1]
        ans = []
    else:
        stack_finished = False
# final_ans += ans[::-1]
# print(ans)
# print(stack)
print(''.join(final_ans+ans[::-1]))