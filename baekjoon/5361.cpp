#include <iostream>
using namespace std;
int main() {
    double a[5], sum;
    int n;
    while (n--) {
        sum = 0;
        for (int i = 0; i < 5; i++)
        {
            double x;
            cin >> x;
            sum += a[i] * x;
        }
        printf("$%.2f\n",sum );
    }
}
