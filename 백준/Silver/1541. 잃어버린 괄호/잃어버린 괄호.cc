#include <cstdio>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <string>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	string str;
	cin >> str;

	int cur = 0;
	int ans = 0;
	int trigger = 1;
	string buff;
	for (int cur = 0; cur < str.size(); cur++) {
		if (cur == str.size() - 1) {
			buff.push_back(str[cur]);
			//cout << buff << endl;;
			ans += stoi(buff) * trigger;
		}

		if (isdigit(str[cur])) {
			buff.push_back(str[cur]);
		}
		else {
			if (str[cur] == '+') {
				//cout << buff << endl;;
				ans += stoi(buff) * trigger;
				buff.clear();
			}
			else {
				//cout << buff << endl;;
				ans += stoi(buff) * trigger;
				buff.clear();
				trigger = -1;
			}
		}
	}

	cout << ans;

}