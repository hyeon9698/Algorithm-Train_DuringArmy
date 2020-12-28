import sys
sys.stdin = open('input.txt', 'r')
n, m = map(int, input().split())

team_mem = {}
mem_team = {}


for i in range(n):
    group_name = input()
    member_number = int(input())
    team_mem[group_name] = []
    for _ in range(member_number):
        name = input()
        team_mem[group_name].append(name)
        mem_team[name] = group_name

for _ in range(m):
    x_input = input()
    x_number = int(input())
    if x_number:
        print(mem_team[x_input])
    else:
        for mem in sorted(team_mem[x_input]):
            print(mem)

