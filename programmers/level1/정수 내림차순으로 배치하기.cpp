#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <math.h>

using namespace std;

long long solution(long long n) {
    long long answer = 0;
    string a="";
    vector<int> v;
    while(n){
        v.push_back(n%10);
        n/=10;
    }
    sort(v.begin(),v.end(),greater<long long>());
    for(int i=0;i<v.size();i++){
        a+=v[i]+'0';
    }
    answer = stol(a);
    return answer;
}
