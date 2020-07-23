#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer;
    int temp;
    for(int i=0;i<arr.size();i++){
        temp = arr[i];
        if(i==0){
            answer.push_back(temp);
            continue;
        }
        if(arr[i-1] == temp){
            continue;
        }
        else {
            answer.push_back(temp);
        }
    }
    return answer;
}
