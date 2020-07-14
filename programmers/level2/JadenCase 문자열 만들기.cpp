#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(string s) {
    string answer = "";
    int sol = 0;
    for(int i = 0;i<s.size();i++){
        if(s[i-1]==' ' && s[i]!=' '){
            if(s[i]>='a'&&s[i]<='z'){
                s[i] = s[i] + ('A'-'a');
            }
        }
        else if(s[i]>='A'&&s[i]<='Z'){
            s[i] = s[i] - ('A'-'a');
        }
        else if(s[0] >='a'&&s[0]<='z'){
            s[0] = s[0] + ('A'-'a');
        }
    }
    return s;
}
