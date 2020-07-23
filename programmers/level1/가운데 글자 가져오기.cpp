#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    string answer = "";
    int hsize = s.size()/2;
    if(s.size()%2==0){
        answer = s[hsize-1];
        answer+=s[hsize];
    }
    else {
        answer = s[hsize];
    }
    return answer;
}
