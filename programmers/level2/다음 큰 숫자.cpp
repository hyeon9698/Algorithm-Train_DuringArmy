#include <string>
#include <vector>
#include <iostream> 
#include <math.h>

using namespace std;

int Check_Count(int num){ 
    int one_cnt = 0 ;    
    while(num != 0){
        if(num%2 == 1)one_cnt++;
        num/=2; 
    }
    return one_cnt;
}

int solution(int n) {
    int answer = 0;
    int n_cnt = Check_Count(n);

    for(int i=n+1; i<=1000000; i++){ 
        int new_cnt = Check_Count(i);
        if(n_cnt == new_cnt){  
            answer = i ; 
            break; 
        }
    }
    return answer;
}
