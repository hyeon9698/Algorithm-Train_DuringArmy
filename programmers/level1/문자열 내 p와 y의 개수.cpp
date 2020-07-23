#include <string>
#include <iostream>
using namespace std;

bool solution(string s)
{
    bool answer = true;
    int countpp = 0;
    int countyy = 0;
    for(int i=0;i<s.size();i++){
        if(s[i] == 'p'||s[i]=='P'){
            countpp++;
        }
        if(s[i] == 'y'||s[i]=='Y'){
            countyy++;
        }        
    }
    if(countpp != countyy){
        answer = false;
    }
    if(countpp==0 && countyy==0){
        answer = false;
    }
    return answer;
}
