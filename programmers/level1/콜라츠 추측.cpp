#include<iostream>
using namespace std;

int collatz(int num)
{
    int answer = 0;
  cout<< num <<"\n";
  while(answer++ <= 500){
    num = num%2 ==0 ? num/2 : num*3+1;
    if(num == 1) break;
  }

    return answer > 500 ? -1 : answer;
}

int main()
{
    int testCase = 6;
    int testAnswer = collatz(testCase);

    cout<<testAnswer;
}
