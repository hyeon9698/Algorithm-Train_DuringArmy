#include <string>
#include <vector>

using namespace std;

string solution(int n) {
    string answer = "";
    int result;
    while(n>0){
        if(n%3==0){
            result = 4;
            n = n/3-1;
        }
        else{
            result = n%3;
            n = n/3;
        }
        answer = to_string(result) + answer;
    }
    return answer;
}
