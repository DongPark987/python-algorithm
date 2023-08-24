#include <cstdio>
#include <cstring>
#include <queue>

#pragma warning(disable:4996);
using namespace std;
bool visit[100001] = { false, };
int bfs(int n1, int n2) {
	queue<int> q[2];
	q[0].push(n1);
	q[1].push(0);
	int a, b, c;
	visit[n1] = true;
	int cursor;
	while (q[0].empty() == false) {
		cursor = q[0].front();
		a = cursor + 1;
		b = cursor - 1;
		c = cursor * 2;
		if (a == n2 || b == n2 || c == n2)return q[1].front() + 1;

		if (a < n2 && visit[a] == false) {
			visit[a] = true;
			q[0].push(a);
			q[1].push(q[1].front() + 1);
		}

		if (b > 0 && visit[b] == false) {
			visit[b] = true;
			q[0].push(b);
			q[1].push(q[1].front() + 1);
		}

		if (c < 100001 && visit[c] == false) {
			visit[c] = true;
			q[0].push(c);
			q[1].push(q[1].front() + 1);
		}
		q[0].pop();
		q[1].pop();
	}
}

int main() {
	int n1, n2;
	scanf("%d %d", &n1, &n2);
	if (n1 != n2) {
		printf("%d\n", bfs(n1, n2));
	}
	else {
		printf("0\n");
	}
}