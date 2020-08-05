#include <vector>
#include <algorithm>
#include <vector>

using namespace std;

int solution(vector<int> nums)
{
    int answer = 0;
    int tmp=0;
    sort(nums.begin(),nums.end());
    for(int i=0;i<nums.size();i++){
        if(tmp!=nums[i]){
            tmp = nums[i];
            answer++;
        }
        if(answer==nums.size()/2) break;
    }
    return answer;
}
