#include <cstdio>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <string>
#include <cstring>

using namespace std;

long long runTime[100001] = { 0 };
long long M, N;

bool check(long long mid) {
	long long cnt = 0;
	long long disk = mid;
	for (int i = 0; i < N; i++) {
		disk -= runTime[i];
		if (disk < 0) {
			cnt++;
			if (cnt == M)
				return false;
			disk = mid - runTime[i];
		}
	}

	return true;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> N >> M;
	long long total = 0;
	for (int i = 0; i < N; i++) {
		cin >> runTime[i];
		total += runTime[i];
	}

	long long left = *max_element(runTime, runTime + N);
	long long right = total;
	long long mid = 0;

	long long ans = 0;

	while (left <= right) {
		mid = (left + right) / 2;

		if (check(mid) == true) { 
			ans = mid;
			right = mid - 1;
		}
		else {
			left = mid + 1;
		}

	}
	cout << ans;
}