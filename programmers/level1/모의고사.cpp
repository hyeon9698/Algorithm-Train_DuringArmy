#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;
int ai[10001];
int bi[10001];
int ci[10001];

vector<int> solution(vector<int> answers) {
    for(int i=0;i<10000;i++){
        int temp = (i+1)%5;
        if (temp == 0 )temp = 5;
        ai[i] = temp;
}
for(int i=0;i<10000;i+=8){
    bi[i] = 2;
    bi[i+1] = 1;
    bi[i+2] = 2;
    bi[i+3] = 3;
    bi[i+4] = 2;
    bi[i+5] = 4;
    bi[i+6] = 2;
    bi[i+7] = 5;    
}
for(int i=0;i<10000;i+=10){
    ci[i] = 3;
    ci[i+1] = 3;
    ci[i+2] = 1;
    ci[i+3] = 1;
    ci[i+4] = 2;
    ci[i+5] = 2;
    ci[i+6] = 4;
    ci[i+7] = 4;
    ci[i+8] = 5;
    ci[i+9] = 5;
}
    vector<int> answer;
    
    int acount = 0;
    int bcount = 0;
    int ccount = 0;
    int a = 1;
    int b = 2;
    int c = 3;
    for(int i=0;i<answers.size();i++){
        if(answers[i] == ai[i]){acount++;}
        if(answers[i] == bi[i]){bcount++;}
        if(answers[i] == ci[i]){ccount++;}        
    }
    if(acount > bcount && acount > ccount){
        answer.push_back(1);
    }
    else if(bcount>acount && bcount > ccount){
        answer.push_back(2);
    }
    else if(ccount>acount && ccount > bcount){
        answer.push_back(3);
    }
    else if (acount == bcount && acount > ccount){
        answer.push_back(1);
        answer.push_back(2);
    }
    else if (bcount == ccount && bcount > acount){
        answer.push_back(2);
        answer.push_back(3);
    }
    else if(acount == ccount && acount > bcount){
        answer.push_back(1);
        answer.push_back(3);
    }
    else if(acount == bcount && bcount == ccount){
        answer.push_back(1);
        answer.push_back(2);
        answer.push_back(3);
    }
    return answer;
}
