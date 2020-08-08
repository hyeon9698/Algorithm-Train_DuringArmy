#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    priority_queue<int,vector<int>, greater<int>> pq;
    for(int i=0;i<scoville.size();i++){
        pq.push(scoville[i]);
    }
    while(pq.size()>=2){
        if(pq.top()>=K) break;
        int a = pq.top();pq.pop();
        int b = pq.top();pq.pop();
        int c = a + b*2;
        pq.push(c);
        answer++;
    }
    if(pq.top()<K) answer = -1;
    
    return answer;
}
