#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_set>

using namespace std;

vector<int> solution(int n, vector<string> words) {
    vector<int> answer;
    unordered_set<string> s;
    int size = words.size();
    int num = 0;
    int turn = 0;
    int i;
    s.insert(words[0]);
    for(i=1;i<size;i++){
        if(s.find(words[i])==s.end()&&words[i-1][words[i-1].length()-1]==words[i][0]){
            s.insert(words[i]);
        }
        else break;
    }
    if(i<size){
        num = (i%n)+1;
        turn = (i/n) +1;
    }
    answer.push_back(num);
    answer.push_back(turn);
    
    return answer;
}
