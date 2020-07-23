#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(string s, int n) {
    string answer = "";
    int len = s.length();
    for(int i=0;i<len;i++){
        if(s[i] >= 'A' && s[i] <= 'Z'){
            s[i] = (s[i] + n -'A')%26 + 'A';
        }
        else if (s[i] >= 'a' && s[i] <='z'){
            s[i] = (s[i] +n-'a')%26+'a';
        }
        answer += s[i];
    }
    return answer;
}
