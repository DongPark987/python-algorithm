#include <stdio.h>
#include <string.h>
#include <queue>
//#include <iostream>

using namespace std;
#pragma warning(disable : 4996)

struct axis
{
	int x, y, z;
};

int M, N, H;
int dx[6] = { 1,-1,0,0,0,0 }, dy[6] = { 0,0,-1,1,0,0 }, dz[6] = { 0,0,0,0,-1,1 };
int f_cnt = 0;
char box[101][101][101];
queue<axis> q;

void mprint() {
	printf("\---------------------\n",f_cnt);
	for (int k = 0; k < H; k++) {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				printf("%d ", box[k][i][j]);

			}
			printf("\n");
		}
	}
	printf("\---------------------\n", f_cnt);
}

int main() {
	/*ios_base::sync_with_stdio(false);
	cin.tie(NULL);cout.tie(NULL);*/
	scanf("%d %d %d", &M, &N, &H);

	for (int k = 0; k < H; k++) {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				scanf("%d", &box[k][i][j]);
				if (box[k][i][j] == 0) {
					f_cnt++;
				}
				else if (box[k][i][j] == 1) {
					q.push({ j,i,k });
				}
			}
		}
	}

	int ans = 0;
	int q_size;
	while (true) {
		q_size = q.size();

		if (f_cnt == 0 || q_size == 0)
			break;
		for (int i = 0; i < q_size; i++) {
			int x = q.front().x, y = q.front().y, z = q.front().z;
			q.pop();
			for (int j = 0; j < 6; j++) {
				int tx = x + dx[j], ty = y + dy[j], tz = z + dz[j];
				if (tx < 0 || tx >= M || ty < 0 || ty >= N || tz < 0 || tz >= H)
					continue;
				if (box[tz][ty][tx] == 0) {
					box[tz][ty][tx] = 1;
					f_cnt--;
					q.push({ tx,ty,tz });
				}
			}
		}

		ans++;
	}

	//mprint();
	if (f_cnt == 0)
		printf("%d", ans);
	else
		printf("-1");
}