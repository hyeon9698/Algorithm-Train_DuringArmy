#include <iostream>
#include<vector>
using namespace std;

int solution(vector<vector<int>> board)
{
    int answer = 0;
    vector<vector<int>> temp(board.size() +1, vector<int>(board[0].size() + 1, 0));
    for(int i=1;i<=board.size();i++){
        for(int j=1;j<=board[0].size();j++){
            temp[i][j] = (min(min(temp[i-1][j],temp[i][j-1]),temp[i-1][j-1])+1)*board[i-1][j-1];
            answer = max(answer,temp[i][j]);
        }
    }

    return answer*answer;
}
