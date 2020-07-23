#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer;
    vector<int> test;
    int removee;
    test = arr;
    sort(test.begin(), test.end());
    removee = test[0];
    arr.erase(remove(arr.begin(),arr.end(),removee));
    answer = arr;
    if(answer.size()==0){
        answer.push_back(-1);
    }
    return answer;
}
