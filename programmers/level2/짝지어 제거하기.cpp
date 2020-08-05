#include <iostream>
#include<string>
#include <stack>

using namespace std;

int solution(string s)
{
    int answer = 0;
    stack<int> st;
    for(int i=0;i<s.size();i++){
        if(!st.empty()){
            char tmp = st.top();
            if(tmp == s[i]){
                st.pop();
            }
            else st.push(s[i]);
        }
        else st.push(s[i]);
    }
    if(st.empty()){
       answer = 1; 
    }
    return answer;
}
