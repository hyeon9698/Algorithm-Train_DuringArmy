#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    vector<int> A(n+1,1);
    for(auto a: lost){
        A[a]--;
    }
    for(auto a: reserve){
        A[a]++;
    }
    for(int i=1;i<A.size();i++){
        if(A[i]==0){
            if(A[i-1]==2){
                A[i-1]--;
                A[i]++;
            }
            else if(i!=A.size()&&A[i+1]==2){
                A[i+1]--;
                A[i]++;
            }
        }
    }
    for(int i=1;i<A.size();i++){
        if(A[i]!=0){
            answer++;
        }
    }
    return answer;
}
