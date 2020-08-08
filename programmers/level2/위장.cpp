#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    unordered_map<string,int> temp;
    for(int i=0;i<clothes.size();i++){
        temp[clothes[i][1]]++;
    }
    for(auto pair : temp){
        answer *=(pair.second+1);
    }
    return answer-1;
}
