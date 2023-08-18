#include <stdio.h>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

typedef struct _order {
	int time;
	short d;
}order;

typedef struct _snake {
	int y, x;
	int d;
}snake;

int main() {
	char map[102][102] = { 0, };
	int N, K, L, x, y;
	int dx[4] = { 1,0,-1,0 }, dy[4] = { 0,1,0,-1 };
	int c_d[2][4] = { {1,2,3,0},{3,0,1,2} };
	vector<order> v;
	vector<snake> s;
	scanf("%d %d", &N, &K);
	for (int i = 0; i < K; i++) {
		scanf("%d %d", &y, &x);
		map[y][x] = 1;
	}
	scanf("%d", &L);
	for (int i = 0; i < L; i++) {
		int tn; char tc;
		scanf("%d %c", &tn, &tc);
		if (tc == 'L')
			v.push_back({ tn,1 });
		else
			v.push_back({ tn,0 });
		
	}
	for (int i = 0; i < N + 2; i++) {
		map[i][0] = 3;
		map[i][N + 1] = 3;
		map[0][i] = 3;
		map[N + 1][i] = 3;
	}

	int timer = 0, o_c = 0;
	int tx, ty, td, size;
	s.push_back({ 1, 1, 0 });
	map[1][1] = 3;
	while (true) {
		timer++;
		tx = s[0].x;
		ty = s[0].y;
		td = s[0].d;
		size = s.size();
		if (map[ty + dy[td]][tx + dx[td]] != 3) {
			if (map[ty + dy[td]][tx + dx[td]] == 0)
				map[s[size - 1].y][s[size - 1].x] = 0;
			else
				s.push_back(s[size - 1]);
			for (int i = size - 1; i >= 1; i--) s[i] = s[i - 1];
			s[0].x += dx[td];
			s[0].y += dy[td];
			map[s[0].y][s[0].x] = 3;
		}
		else break;
		if (o_c < L) { //방향 전환
			if (v[o_c].time == timer) {
				s[0].d = c_d[v[o_c].d][td];
				o_c++;
			}
		}
	}
	printf("%d", timer);
}