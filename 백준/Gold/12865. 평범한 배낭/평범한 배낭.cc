#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int dp[100001] = { 0, };
	int n, k, w, v;
	cin >> n >> k;
	for (int i = 1; i <= n; i++) {
		cin >> w >> v;
		for (int j = k; j >= w; j--) {
			if (dp[j] < dp[j - w] + v)
				dp[j] = dp[j - w] + v;
		}
	}
	cout << dp[k];
}