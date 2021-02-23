# https://www.youtube.com/watch?v=yWWbLrV4PZ8
import sys
sys.stdin = open('input.txt', 'r')
# kmp 알고리즘
string = input()
j = 0
table = [0 for _ in range(len(string))]
for i in range(1, len(string)):
    while j>0 and string[i] != string[j]:
        j = table[j-1]
    if string[i] == string[j]:
        j += 1
        table[i] = j
print(table)