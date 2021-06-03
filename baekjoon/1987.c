#include <stdio.h>
#pragma warning(disable:4996)
int is_prime(int n) {
	if (n == 1) {
		return 0;
	}
	int tmp = 0;
	for (int i = 2; i < n; i++) {
		if (n % i == 0) {
			tmp++;
		}
	}
	if (tmp == 0) {
		return 1;
	}
	else {
		return 0;
	}
}
int main() {
	int n;
	int lst[101];
	int cnt = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &lst[i]);
	}
	for (int i = 0; i < n; i++) {
		if (is_prime(lst[i])) {
			cnt++;
		}
	}
	printf("%d", cnt);
	return 0;
}
