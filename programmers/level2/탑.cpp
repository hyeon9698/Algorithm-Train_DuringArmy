#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;


vector<int> solution(vector<int> heights) {
    vector<int> answer;
    vector<pair<int,int>> v;
    int count=0;
    for(int i=0;i<heights.size();i++){
        v.push_back(make_pair(i+1,heights[i]));
    }
    for(int i=0;i<heights.size();i++){
        count=0;
        for(int j=i;j>=0;j--){
            if(heights[i]<heights[j]){
                answer.push_back(v[j].first);
                count=1;
                break;
            }
        }
        if(count==0)answer.push_back(0);

    }
    return answer;
}
