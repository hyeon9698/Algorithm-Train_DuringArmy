#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<int> priorities, int location) {
    deque<int> q;
    for(int i=0;i<priorities.size();i++){
        q.push_back(priorities[i]);
    }
    int sol = 0;
    int answer = 0;
    for(int i=0;i<priorities.size();i++){
        sol = 0;
        if(sol==0){
            for(int j=0;j<priorities.size();j++){
                if(q[0]<q[j]){
                    sol = 1;
                }
            }
        }
        if(sol==0)break;
        if(sol==1){
            cout<<q[0]<<'\n';
            q.push_back(q[0]);
            q.pop_front();
            if(location==0) location+=priorities.size()-1;
            else location--;
            }
    }
    answer = location;
    return answer+1;
}