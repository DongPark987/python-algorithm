#include <iostream>
#include <vector>
#include <queue>

#pragma warning(disable:4996)
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	int N, M, t1, t2;
	vector<int> v[32001];
	int link[32001] = {0, };
	cin >> N >> M;
	for (int i = 1; i <= M; i++) {
		cin >> t1 >> t2;
		link[t2]++;
		v[t1].push_back(t2);
	}
	queue <int>q;
	for (int i = 1; i <= N; i++)
		if (link[i] == 0)
			q.push(i);

	while (!q.empty()) {
		int t = q.front();
		q.pop();
		cout << t << " ";
		for (int i : v[t]) {
			link[i]--;
			if (!link[i])
				q.push(i);
		}
	}
}