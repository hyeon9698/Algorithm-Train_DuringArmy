#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

bool compare(string a, string b) {
	int len;
	len = a.size() > b.size() ? a.size() : b.size();
	char x, y;
	for (int i = 0; i <= len; i++) {
		x = a[i % a.size()];
		y = b[i % b.size()];
		if (x > y)return true;
		else if (x == y)continue;
		else return false;
	}
	return false;
}

string solution(vector<int> numbers) {
	vector<string> number_str;
	string answer = "";
	int zero = 0;
	for (int i : numbers)number_str.push_back(to_string(i));
	sort(number_str.begin(), number_str.end(), compare);
	for (string i : number_str) {
		if (i == "0")zero++;
		answer+=i;
	}
	if (answer.size() == zero)return "0";
	return answer;
}
