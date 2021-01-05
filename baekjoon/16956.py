import sys
# sys.stdin = open('input.txt', 'r')
r, c = map(int, input().split())
data = []
sheep_data = []
wolf_data = []
M = [list(input()) for i in range(r)]

# for i in range(r):
#     d = input()
#     data.append(d)
#     for j, le in enumerate(d):
#         if le == 'S':
#             sheep_data.append((i, j))
#         elif le == 'W':
#             wolf_data.append((i, j))
dx = [0,1,0,-1]
dy = [1,0,-1,0]
flag = True
for i in range(r):
    for j in range(c):
        if M[i][j] == 'W':
            for w in range(4):
                ii, jj = i + dx[w], j + dy[w]
                if 0<=ii<r and 0<=jj<c and M[ii][jj] == 'S':
                    # print(0)
                    flag = False
# flag = True
# for x, y in wolf_data:
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if (nx, ny) in sheep_data:
#             flag = False
#             break
#     if not flag:
        # break
if not flag:
    print(0)
else:
    print(1)
    for i in range(r):
        tx = ''.join(M[i]).replace(".","D")
        print(tx)
