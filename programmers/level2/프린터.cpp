#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>


using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    queue<pair<int,int>> que;
    priority_queue <int> sequence;
    for(int i=0;i<priorities.size();i++){
        que.push(make_pair(i,priorities[i]));
        sequence.push(priorities[i]);
    }
    while(!que.empty()){
        int where = que.front().first;
        int what = que.front().second;
        que.pop();
        
        if(sequence.top()==what){
            answer++;
            sequence.pop();
            if(where==location){
                return answer;
            }
        }
        else que.push(make_pair(where,what));
    }
    return answer;
}
