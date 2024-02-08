#include <cstring>
#include <cstdio>
#pragma warning(disable: 4996)

bool isend = false;
int grid[9][9];

class numset {

public:
    int unused[10];
    int blank[9][2];
    int check[10] = { 0, };
    int blank_count = 0;
    int x, y;

    void init(int px, int py) {
        x = px;
        y = py;
        int i, j, count;
        bool check[10] = { false, };
        check[0] = true;
        for (i = 0; i < 3; i++) {
            for (j = 0; j < 3; j++) {
                if (grid[y + i][x + j] == 0) {
                    blank[blank_count][0] = x + j;
                    blank[blank_count][1] = y + i;
                    blank_count++;
                }
                else {
                    check[grid[y + i][x + j]] = true;
                }
            }
        }

        count = 0;
        for (i = 0; i < 10; i++) {
            if (!check[i]) {
                unused[count] = i;
                count++;
            }
        }
    }

};

numset myset[9];

bool isvalid(int x, int y) {
    int i;
    int check[10];
    memset(check, 0, sizeof(int) * 10);

    for (i = 0; i < 9; i++) {
        if (grid[y][i] != 0 && check[grid[y][i]] == 1) {
            return false;
        }

        check[grid[y][i]]++;
    }
    memset(check, 0, sizeof(int) * 10);
    for (i = 0; i < 9; i++) {
        if (grid[i][x] != 0 && check[grid[i][x]] == 1) {
            return false;
        }
        check[grid[i][x]]++;
    }

    return true;
}

void solve(int setnum, int bnum) {
    int i, j;
    int fx = myset[setnum].blank[bnum][0];
    int fy = myset[setnum].blank[bnum][1];
    const int limit = myset[setnum].blank_count;


    if (setnum == 9) {
        isend = true;
        return;
    }
    if (limit == 0) {
        solve(setnum + 1, 0);
        if (isend == true) return;
    }

    for (i = 0; i < limit; i++) {
        if (myset[setnum].check[myset[setnum].unused[i]] == 1) {
            continue;
        }
        grid[fy][fx] = myset[setnum].unused[i];

        myset[setnum].check[myset[setnum].unused[i]] = 1;

        if (isvalid(fx, fy)) {
            if (bnum == limit - 1) {
                solve(setnum + 1, 0);
                if (isend == true) return;
                myset[setnum].check[myset[setnum].unused[i]] = 0;
            }
            else {
                solve(setnum, bnum + 1);
                if (isend == true) return;
                myset[setnum].check[myset[setnum].unused[i]] = 0;
            }
        }
        else {
            myset[setnum].check[myset[setnum].unused[i]] = 0;
        }
    }

    myset[setnum].check[grid[fy][fx]] = 0;
    grid[fy][fx] = 0;
    return;
}

int main() {
    int i, j, count;

    for (i = 0; i < 9; i++) {
        for (j = 0; j < 9; j++) {
            scanf("%d", &grid[i][j]);
        }
        getchar();
    }

    count = 0;
    for (i = 0; i < 9; i = i + 3) {
        for (j = 0; j < 9; j = j + 3) {
            myset[count].init(j, i);
            count++;
        }
    }
    solve(0, 0);

    for (i = 0; i < 9; i++) {
        for (j = 0; j < 9; j++) {
            printf("%d ", grid[i][j]);
        }
        printf("\n");
    }

}