#include<stdio.h>
#pragma warning(disable:4996)
#pragma warning(disable:6031)
int digit[10];
void get_digit(int n) {
    while (n > 0) {
        digit[n % 10] = 1;
        n /= 10;
    }
}
int gcd(int a, int b) {
    return b ? gcd(b, a % b) : a;
}
int main() {
    long long n;
    int lcm = 1, loop = 1;
    scanf("%lld", &n);
    get_digit(n);
    for (int i = 1; i < 10; i++)
        if (digit[i])lcm = lcm * i / gcd(lcm, i);
    for (int i = 0;; i++) {
        for (int j = 0; j < loop; j++) {
            if ((n * loop + j) % lcm == 0) {
                printf("%lld\n", n * loop + j);
                goto exit;
            }
        }
        loop *= 10;
    }
exit:
    return 0;
}
