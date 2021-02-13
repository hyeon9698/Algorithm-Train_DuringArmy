import sys
sys.stdin = open('input.txt', 'r')
n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            index_R = [i, j]
        elif graph[i][j] == 'B':
            index_B = [i, j]
        elif graph[i][j] == 'O':
            index_O = [i, j]
red_in = False
blue_in = False
move_direction = [1, 2, 3]  # 1오른쪽 2왼쪽 #위쪽
move_count = 0
def dfs(direction, count):
    if count >= 10:
        print(count)
        return
    global red_in
    global blue_in
    red_stop = False
    blue_stop = False
    while red_stop and blue_stop:
        R_x = index_R[0]
        R_y = index_R[1]
        B_x = index_B[0]
        B_y = index_B[1]
        if direction == 1:
            if not red_stop:
                if graph[R_x][R_y+1] == 'O':
                    red_in = True
                    red_stop = True
                elif graph[R_x][R_y+1] == '#':
                    red_stop = True
                else:
                    index_R[1] += 1
            if not blue_stop:
                if graph[B_x][B_y+1] == 'O':
                    blue_in = True
                    blue_stop = True
                elif graph[B_x][B_y+1] == '#':
                    blue_stop = True
                else:
                    index_B[1] += 1
        if red_in and not blue_stop:
            finished = True
    for i in range(3):
        if direction == 1 and move_direction[i] == 2:
            continue
        elif direction == 2 and move_direction[i] == 1:
            continue
        elif direction == 3 and move_direction[i] == 3:
            continue
        else:
            dfs(move_direction[i], count + 1)
dfs(1, move_count)
if blue_in or move_count >= 10:
    move_count = -1
print(move_count)