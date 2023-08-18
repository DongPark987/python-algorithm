#include <cstdio>
#include <cstring>
#pragma warning(disable:4996)

int count = 0;
char* result;
char* data;
int pick;
int repeat = 0;


int Greedy(int loc, int setloc) {
	int i;
	result[loc] = data[setloc];
	int limit = count - pick + loc;
	int checki = setloc;
	int endcheck = pick - 1;

	
	
	while (true) {
		result[loc] = data[checki];
		
		
		for (i = checki; i <= limit; i++) {
			//repeat++;

			if (result[loc] == '9') {
				checki = i;
				break;
			}
			if (data[i] > result[loc]) {
				result[loc] = data[i];
				checki = i;
				if (result[loc] == '9') {
					break;
				}
			}

		}
		if (loc == endcheck) {
			printf("%s", result);
			//printf("\n%d회 수행", repeat);
			break;
		}
		loc++;
		checki++;
		limit++;
	}
	return 0;
}

int  main() {


	int size, erase;
	scanf("%d%d", &size, &pick);
	getchar();
	count = size;
	pick = count - pick;
	data = new char[size];
	result = new char[pick+1];
	result[pick] = '\0';
	scanf("%s", data);

	//printf("\n%d, %d\n", pick, count);

	Greedy(0, 0);

}