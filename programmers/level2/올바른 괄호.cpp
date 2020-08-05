#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>

using namespace std;

bool solution(string s)
{
    bool answer = true;
    stack<char> st;
    for(int i=0;i<s.size();i++){
        if(!st.empty()){
            char tmp = st.top();
            if(tmp == '('&&s[i]==')'){
                st.pop();
            }
            else st.push(s[i]);
        }
        else st.push(s[i]);
    }
    if(!st.empty()){
        answer = false;
    }
    return answer;
}
