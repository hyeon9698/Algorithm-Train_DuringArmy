#include <string>
#include <vector>
#include <iostream>

using namespace std;
 
int solution(int n) {
    int answer = 0;
    int total = 0;
    for(int i=1;i<=n;i++){
        total = 0;
        for(int j=i;j<=n;j++){
            if(total > n){
                break;
            }            
            total = total + j;
            if(total == n){
                answer++;
            }
        }
    }

    return answer;
}
