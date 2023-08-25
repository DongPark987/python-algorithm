#include <cstdio>
#include <cstring>
#pragma warning (disable:4996)

int main() {
	int i, count = 0, coin_count,coin_n = 0, pay = 0;
	int coin[10];
	scanf("%d%d", &coin_n, &pay);
	for (i = 0; i < coin_n; i++) {
		scanf("%d", &coin[i]);
	}
	for (i = coin_n - 1; pay != 0; i--) {
		coin_count = pay / coin[i];
		if (coin_count != 0) {
			count += coin_count;
			pay -= (coin[i] * coin_count);
		}
	}
	printf("%d", count);
}