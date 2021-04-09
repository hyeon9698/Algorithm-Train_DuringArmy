# #include<iostream>
# #include<vector>
# using namespace std;
 
# void dfs(int N, int M, vector<int>& vt){
#     if(vt.size() == M){
#         for(int i: vt)
#             cout<<i<<" ";
#         cout<<"\n";
#         return;
#     }
 
#     for(int n=1; n<=N; n++){
#         if(!vt.empty() && vt.back() > n) continue;
 
#         vt.push_back(n);
#         dfs(N,M,vt);
#         vt.pop_back();
#     }
# }
# int main(){
#     int N,M;
#     vector<int> vt;
#     cin>>N>>M;
#     dfs(N,M,vt);
#     return 0;
# }
def dfs(n,m,_list):
    if len(_list) == m:
        print(' '.join(map(str,_list)))
        return
    for i in range(1, n+1):
        if len(_list) != 0 and _list[-1] > i:
            continue
        _list.append(i)
        dfs(n,m,_list)
        _list.pop()
n, m = map(int, input().split())
_list = []
dfs(n,m,_list)
