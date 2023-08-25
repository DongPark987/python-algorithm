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
int dp[1001][1001] = { 0, };
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	
	

	string str1 = {'0'}, str2 = {'0'}, tmp;
	cin >> tmp;
	str1.append(tmp);
	cin >> tmp;
	str2.append(tmp);
	for (int i = 1; i < str2.size(); i++) {
		for (int j = 1; j < str1.size(); j++) {
			if (str2[i] == str1[j]) {
				dp[i][j] = dp[i - 1][j - 1] + 1;
			}
			else {
				dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
			}
		}
	}

	cout << dp[str2.size()-1][str1.size() - 1];
}