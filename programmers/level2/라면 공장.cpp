#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <queue>

using namespace std;


int solution(int stock, vector<int> dates, vector<int> supplies, int k) {
    int answer = 0;
    priority_queue<int, vector<int>> pq;
    
    for(int i = 1, j = 0; i < k; i++){
        stock--;
        
        if(j < dates.size() && i == dates[j]){
            pq.push(supplies[j]);
            j++;
        }
        
        if(stock == 0){
            stock += pq.top();
            pq.pop();
            answer++;
        }
    }
    
    return answer;
}
