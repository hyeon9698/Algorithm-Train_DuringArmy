#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    int total = brown+yellow;
    for(int i=1;i<=total;i++){
        if(total%i==0){
            int h = i;
            int w = total / i;
            if((w-2)*(h-2)==yellow){
                if(w>=h){
                    answer.push_back(w);
                    answer.push_back(h);
                }
            }
        }
    }
    return answer;
}
