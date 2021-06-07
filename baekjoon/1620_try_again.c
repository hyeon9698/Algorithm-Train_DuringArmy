#include <stdio.h>
#include <string.h>
#pragma warning(disable:4996)
int main() {
	int n;
	int m;
	int num;
	char s[21];
	char val[21];
	char dogam[101][21];
	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; i++) {
		scanf("%s", &s);
		strcpy(dogam[i], s);
	}
	for (int i = 0; i < m; i++) {
		scanf("%s", &val);
		if (val[0] >= '0' && val[0] <= '9') {
			num = atoi(val);
			printf("%s", dogam[num]);
		}
		else {

		}
	}
	return 0;
}
