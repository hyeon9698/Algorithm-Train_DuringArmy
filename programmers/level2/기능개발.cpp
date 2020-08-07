#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>


using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    deque<pair<int,int>> Q;
    stack<int> S;
    for(int i=0;i<progresses.size();i++){
        int total = progresses[i];
        int j=0;
        for(j=0;total<100;j++){
            total = total + speeds[i];
        }
        Q.push_back(make_pair(i,j));
    }

    int max = Q.front().second;
    int POP = 0;
    for(int i=0;i<progresses.size();i++){
        if(max<Q[i].second){
            answer.push_back(POP);
            max = Q[i].second;

            POP=1;
        }
        else{
            POP++;
        }
    }
    if(POP!=0) answer.push_back(POP);
    return answer;
}
