#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 0;
    queue<int> q;
    int total_w = 0;
    int count = 0;
    int CCOUNT = 0;
    int i=0;
    while(i<truck_weights.size()){
        if(q.size() == bridge_length){
            total_w -= q.front();
            q.pop();
        }
        if(total_w+truck_weights[i]<=weight){
            total_w+=truck_weights[i];
            q.push(truck_weights[i]);
            i++;
        }
        else{
            q.push(0);
        }
        count++;
    }
    answer += count;
    answer += bridge_length;
    return answer;
}
