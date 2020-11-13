from sys import stdin

for _ in range(int(stdin.readline())):
    typing = stdin.readline().strip()
    left, right = [], []
    for typ in typing:
        if typ == '<':
            if left:
                right.append(left.pop())
        elif typ == '>':
            if right:
                left.append(right.pop())
        elif typ == '-':
            if left:
                left.pop()
        else:
            left.append(typ)
    left.extend(reversed(right))
    print(''.join(left))



#####################################

test_cases = int(input())

for _ in range(test_cases):
    left = []
    right = []
    pwd = input()

    for x in pwd:
        if x == ">":
            if right:
                left.append(right.pop()) 
        elif x=="<":
            if left:
                right.append(left.pop())
        elif x=="-":
            if left:
                left.pop()
        else:
            left.append(x)

  print("".join(left)+"".join(reversed(right)))



###########

#include <iostream> 
#include <list>
#include <string>
#pragma warning(disable:4996)  
using namespace std; 
 
int main(){
    int T; cin >> T; 
    while (T--) {
        string L; cin >> L;
        list<char> ans;
        list<char>::iterator ans_iter = ans.begin();
        int L_len = L.size(), L_idx = 0;
 
        while (L_idx < L_len) {
            switch (L[L_idx]) {
            case '<':
                if (ans_iter != ans.begin()) ans_iter--;
                break;
            case '>':
                if (ans_iter != ans.end()) ans_iter++;
                break;
            case '-':
                if (ans_iter != ans.begin())  ans.erase((--ans_iter)++);
                break;
            default:
                ans.insert(ans_iter, L[L_idx]);
                break;
            }
            L_idx++;
        }
        for (auto x : ans) printf("%c", x);
        printf("\n");
    }
    return 0;
}


