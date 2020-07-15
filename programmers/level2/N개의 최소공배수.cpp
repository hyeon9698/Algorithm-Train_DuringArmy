#include <string>
#include <vector>
#include <algorithm>


using namespace std;
int gcd(int a, int b){
    while(b!=0){
        int r = a%b;
        a = b;
        b = r;
    }
    return a;
}
int solution(vector<int> arr) {
    int answer = 1;
    int a = 1;
    int tmp = 1;
    for(int i=0;i<arr.size();i++){
        if(i==0){
            tmp = arr[i];
            continue;
        }
        a = gcd(tmp,arr[i]);
        tmp = tmp*arr[i]/a;
    }
    
    return tmp;
}



/* 다른사람 
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int gcd(int x, int y) { return x % y == 0 ? y : gcd(y, x % y); }
int lcm(int x, int y) { return x * y / gcd(x, y); }
int solution(vector<int> arr) {
    int answer = arr[0];
    for (int i = 1; i < arr.size(); i++)
        answer = lcm(answer, arr[i]);
    return answer;
}
*/
