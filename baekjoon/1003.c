#include <stdio.h>
#pragma warning(disable:4996)

void solution(int n, int ans_map[][2]) {
	ans_map[0][0] = 1;
	ans_map[1][1] = 1;
	for (int i = 2; i <= n;i++) {
		ans_map[i][0] = ans_map[i - 1][0] + ans_map[i - 2][0];
		ans_map[i][1] = ans_map[i - 1][1] + ans_map[i - 2][1];
	}
	printf("%d %d\n", ans_map[n][0], ans_map[n][1]);
}
int main() {
	int t;
	int n;
	int ans[41][2] = { 0 };
	scanf("%d", &t);
	for (int i = 0;i < t;i++) {
		scanf("%d", &n);
		solution(n, ans);
	}
	return 0;
}
