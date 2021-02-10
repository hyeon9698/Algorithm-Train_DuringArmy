import sys
sys.stdin = open('input.txt', 'r')
def print_data():
    for i in data:
        print(i)
def candidate_list(i, j):
    cand = []
    for num in range(1, 10):
        flag = True
        if num in data[i]:
            flag = False
        if flag:
            for k in range(9):
                if num == data[k][j]:
                    flag = False
                    break
        if flag:
            ii = i//3
            jj = j//3
            for x in range(ii*3, ii*3+3):
                flag = True
                for y in range(jj*3, jj*3+3):
                    if num == data[x][y]:
                        flag = False
                        break
                if flag == False:
                    break
        if flag:
            cand.append(num)
    return cand
        
data = [list(map(int, input())) for _ in range(9)]
def backtracking(k):
    global state
    if k == len(zero_position):
        for e in data:
            print(''.join(list(map(str, e))))
        state = True
    else:
        for num in candidate_list()
    
            
for i in data:
    print(i)
