#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#pragma warning(disable:4996)
int main() {
	int n;
	char func[7];
	int visited[21] = {0};
	int x;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%s", func);
		if (strcmp(func, "add")==0) {
			scanf("%d", &x);
			visited[x] = 1;
		}
		if (strcmp(func, "remove") == 0) {
			scanf("%d", &x);
			visited[x] = 0;
		}
		if (strcmp(func, "check") == 0) {
			scanf("%d", &x);
			if (visited[x]) printf("1\n");
			else printf("0\n");
		}
		if (strcmp(func, "toggle") == 0) {
			scanf("%d", &x);
			if (visited[x]) visited[x] = 0;
			else visited[x] = 1;
		}
		if (strcmp(func, "all") == 0) {
			for (int i = 0; i < sizeof(visited)/sizeof(int); i++) {
				visited[i] = 1;
			}
		}
		if (strcmp(func, "empty") == 0) {
			for (int i = 0; i < sizeof(visited)/ sizeof(int); i++) {
				visited[i] = 0;
			}
		}
	}
	return 0;
}
