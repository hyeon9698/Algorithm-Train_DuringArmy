#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(string arrangement) {
    int answer = 0;
    vector<int> v;    
    for(int i=0;i<arrangement.length();i++){
        if(arrangement[i]=='(' && arrangement[i+1]==')'){
            for(int j=0;j<v.size();j++){
                v[j]++;
            }
            i++;
        }
        else if(arrangement[i]==')'){
            answer += v.back() + 1;
            v.pop_back();
        }
        else v.push_back(0);
    }
    return answer;
}
