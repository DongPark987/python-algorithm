#include <iostream>
#include <string>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n;
	string str;
	cin >> n;
	cin >> str;

	long long ans = 0;
	string tmp_num;
	for (char c : str) {
		if (isalpha(c)) {
			if (tmp_num.length() > 0)
				ans += stoi(tmp_num);
			tmp_num.clear();
		}
		else {
			tmp_num.push_back(c);
		}
	}
	if (tmp_num.length() > 0)
		ans += stoi(tmp_num);
	cout << ans;
}