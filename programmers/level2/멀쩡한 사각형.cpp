using namespace std;

long long solution(int w, int h)
{
	int gcd;
	long long sum = (long long)w * (long long)h;
	int a = w;
    int b = h;
	while(b!=0){
		int r = a%b;
		a= b;
		b= r;
	}
    gcd = a;
	return sum - gcd * ((w / gcd) + (h / gcd) - 1);
}
