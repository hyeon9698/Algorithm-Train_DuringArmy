# https://cotak.tistory.com/3
import sys
sys.stdin = open('input.txt', 'r')
class Trie:
    def __init__(self):
        self.root = {}
    def add(self, foods):
        cur = self.root
        for food in foods:
            if food not in cur:
                cur[food] = {}
            cur = cur[food]
        cur[0] = True
    def travel(self, level, cur):
        if 0 in cur:
            return
        cur_children = sorted(cur)
        for child in cur_children:
            print("--"*level + child)
            self.travel(level+1, cur[child])
n = int(input())
nest = Trie()
for _ in range(n):
    input_line = input().split()
    k = input_line[0]
    foods = input_line[1:]
    nest.add(foods)
nest.travel(0, nest.root)