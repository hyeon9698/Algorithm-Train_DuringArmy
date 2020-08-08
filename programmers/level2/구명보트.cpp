#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;
    int L = 0; int R = people.size()-1;
    sort(people.begin(),people.end());
    while(L<=R){
        if(people[L]+people[R]>limit){
            R--;
            answer++;
        }
        else{
            L++;
            R--;
            answer++;
        }
    }
    return answer;
}
