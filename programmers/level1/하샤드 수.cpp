#include <string>
#include <vector>

using namespace std;

bool solution(int x) {
    bool answer = true;
    int ans=0;
    int A = x;
    while(x){
        ans = ans + x%10;
        x=x/10;
    }
    
    return A%ans==0 ? true: false;
}
