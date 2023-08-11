#include <cstdio>
#include <cstring>
#pragma warning(disable:4996)

int n,limit;
int board[14][14] = { 0, };
int count = 0;

void forbid(int x, int loc, int isforbid) {
	int i, j;
	for (i = loc; i < n; i++) {
		board[x][i] += isforbid;
	}

	if (x >= loc) {
		for (i = x, j = loc; i < n ; i++, j++)board[i][j] += isforbid;
	}
	else {
		for (i = x, j = loc; j < n; i++, j++)board[i][j] += isforbid;
	}

	if (x >= loc) {
		for (i = x, j = loc; i >= 0; i--, j++)board[i][j] += isforbid;
		
	}
	else {
		for (i = x, j = loc; j < n; i--, j++)board[i][j] += isforbid;
		
	}
}

void backtrack(int loc) {

	if (loc == limit) {
		for (int i = 0; i < n; i++) {
			if (board[i][loc]) continue;
			count++;
		}
		return;
	}
	for (int i = 0; i < n; i++) {
		if (board[i][loc]) continue;
		forbid(i, loc, 1);
		backtrack(loc + 1);
		forbid(i, loc, -1);
	}
}

int  main() {

	scanf("%d", &n);
	limit = n - 1;
	backtrack(0);
	printf("%d\n", count);
}