#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> citations) {
    int answer = 0;
    int SIZE = citations.size();
    sort(citations.begin(),citations.end(),greater<int>());
    for(int i=1;i<SIZE+1;i++){
        if(i<=citations[i-1]) answer++;
    }
    return answer;
}

