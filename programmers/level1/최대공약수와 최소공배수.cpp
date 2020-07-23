#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n, int m) {
    vector<int> answer;
    int a,b;
    int maxa=0;
    if(n>m){
        int temp=n;
        n = m;
        m = temp;
    }
    for(int i=1;i<=m;i++){
        if(m%i==0){
            a=i;
        }
        for(int j=1;j<=n;j++){
            if(n%j==0){
                b=j;
            }
            if(a==b){
                if(maxa<a){
                    maxa = a;
                }
            }
        }
    }   
    answer.push_back(maxa);
    if(m%n==0){
        answer.push_back(m);
    }
    else{
        answer.push_back((n/maxa)*(m/maxa)*maxa);
    }
    return answer;
}
