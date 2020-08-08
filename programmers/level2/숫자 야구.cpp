#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> baseball) {
    int answer = 0;
    vector<string> a;
    for(int i = 123;i<=987;i++){
        string temp{ to_string(i) };
        if(temp[0]==temp[1]||temp[1]==temp[2]||temp[2]==temp[0]||temp[0]==' '||temp[1]=='0'||temp[2]=='0')
            continue;
        a.push_back(temp);
    }
    for(auto b: baseball){
        string temp = to_string(b[0]);
        for(int i=a.size()-1;i>=0; i--){
            int strike = 0,ball =0;
            for(int j=0;j<3;j++){
                if(temp[j]==a[i][j]) strike++;
                if(temp[j]==a[i][(j+1)%3]||temp[j]==a[i][(j+2)%3]) ball++;
            }
            if(strike!=b[1]||ball!=b[2]) a.erase(a.begin()+i);
        }
    }
    return a.size();
}
