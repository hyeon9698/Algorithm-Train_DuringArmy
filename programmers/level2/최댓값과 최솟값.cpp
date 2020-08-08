#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string s) {
    string answer = "";
    vector<int> a;
    string temp="";
    for(int i=0;i<s.size();i++){
        if(s[i]==' '){
            a.push_back(stoi(temp));
            temp = "";
        }
        else{
            temp+=s[i];
        }
    }
    a.push_back(stoi(temp));
    sort(a.begin(),a.end());
    answer += to_string(a.front());
    answer += " ";
    answer += to_string(a.back());
    return answer;
}
