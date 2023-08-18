#include <cstdio>
#include <cstring>
#include <queue>

#define MAX_SIZE 50
#pragma warning(disable:4996);
using namespace std;

char map[MAX_SIZE + 1][MAX_SIZE + 1];
int visited[MAX_SIZE][MAX_SIZE];
int n1, n2, dest[2];
int dx[4] = { 1,0,-1,0 };
int dy[4] = { 0,1,0,-1 };
queue<pair<int, int>> k;
queue<pair<int, int>> w;

bool valid_check(int x, int y, int type) {
	if (type == 0) {
		return (x >= 0 && x < n2&& y >= 0 && y < n1&& map[y][x] != 'X' && map[y][x] != '*' && map[y][x] != 'D');
	}
	else {
		return (x >= 0 && x < n2&& y >= 0 && y < n1&& visited[y][x] == 0 && (map[y][x] == '.' || map[y][x] == 'D'));
	}
}

void flood() {

}

int bfs() {
	int x, y;
	int nx, ny;
	int tsize;

	while (!k.empty()) {
		
		tsize = w.size();
		for (int i = 0; i < tsize; i++) {
			x = w.front().first;
			y = w.front().second;
			w.pop();
			for (int j = 0; j < 4; j++) {
				nx = x + dx[j];
				ny = y + dy[j];
				if (valid_check(nx, ny, 0)) {
					map[ny][nx] = '*';
					w.push({ nx,ny });
				}
			}
		}

		tsize = k.size();
		for (int t = 0; t < tsize; t++) {
			x = k.front().first;
			y = k.front().second;
			k.pop();
			if (x == dest[0] && y == dest[1])return visited[y][x] - 1;
			for (int i = 0; i < 4; i++) {
				nx = x + dx[i];
				ny = y + dy[i];
				if (valid_check(nx, ny, 1)) {
					visited[ny][nx] = visited[y][x] + 1;
					k.push({ nx,ny });
				}
			}
		}

	}
	return -1;
}


int main(void) {
	int result;
	scanf("%d %d", &n1, &n2);
	for (int i = 0; i < n1; i++) {
		scanf("%s", map[i]);
		for (int j = 0; j < n2; j++) {
			switch(map[i][j]) {
			
			case 'S':
				k.push({ j,i });
				visited[i][j] = 1;
				break;
			case 'D':
				dest[0] = j;
				dest[1] = i;
				break;
			case '*':
				w.push({ j,i });
			}
		}
	}

	result = bfs();
	if (result == -1) {
		printf("KAKTUS");
	}
	else {
		printf("%d", result);
	}
	
}