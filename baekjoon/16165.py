import sys
sys.stdin = open('input.txt', 'r')
n, m = map(int, input().split())


class girlgroup:
    def __init__(self, group_name, member_list):
        self.group_name = group_name
        self.member_list = member_list


GirlGroup = []
for i in range(n):
    group_name = input()
    member_number = int(input())
    member_data_list = []
    for _ in range(member_number):
        member_data_list.append(input())
    GirlGroup.append(girlgroup(group_name, member_data_list))

for _ in range(m):
    x_input = input()
    x_number = int(input())
    if x_number:
        for i in range(len(GirlGroup)):
            if x_input in GirlGroup[i].member_list:
                print(GirlGroup[i].group_name)
    else:
        for i in range(len(GirlGroup)):
            if x_input == GirlGroup[i].group_name:
                print('\n'.join(sorted(GirlGroup[i].member_list)))
