#include <stdio.h>
#pragma warning(disable:4996)
int main() {
	int a;
	int b;
	scanf("%d %d", &a, &b);
	printf("%.9fl", (double)a/(double)b);
	return 0;
}