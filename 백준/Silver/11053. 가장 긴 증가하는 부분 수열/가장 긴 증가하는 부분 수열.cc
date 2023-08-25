#include <cstdio>
#include <algorithm>
using namespace std;
#pragma warning(disable:4996)

int main() {

	int data[1001];
	int dy[1001] = { 0, };
	int n;
	int Max = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) scanf("%d", &data[i]);
	for (int i = 1; i < n; i++) {
		for (int j = 0; j < i; j++) {
			if (data[j] < data[i]) dy[i] = max(dy[j] + 1, dy[i]);
			Max = max(Max, dy[i]);
		}
	}
	printf("%d", Max + 1);
}