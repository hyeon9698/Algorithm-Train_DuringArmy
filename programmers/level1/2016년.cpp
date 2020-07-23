#include <string>
#include <vector>

using namespace std;

string solution(int a, int b) {
    string answer = "";
    int total = 0;
    int day[12]{ 31,29,31,30,31,30,31,31,30,31,30,31 };
    string stringDay[7]{ "FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU" };
    for (int i = 0; i < a - 1; i++)
    {
        total += day[i];
    }
    total += b - 1;
    answer = stringDay[total % 7];
    return answer;
}
