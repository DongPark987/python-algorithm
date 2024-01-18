#include <iostream>

#include <string>
#include <vector>
#include <queue>

using namespace std;

int dx[4] = { 0,0,-1,1 }, dy[4] = { 1,-1,0,0 };

int solution(vector<string> maps) {
    int answer = 0;
    const int row = maps.size(), col = maps[0].size();
    pair<int, int> S, E, L;

    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            if (maps[i][j] == 'S') {
                S.first = i;
                S.second = j;
            }
            else if (maps[i][j] == 'E') {
                E.first = i;
                E.second = j;
            }
            else if (maps[i][j] == 'L') {
                L.first = i;
                L.second = j;
            }
        }
    }


    int visit[101][101];

    for (int i = 0; i < row; i++)
        for (int j = 0; j < col; j++)
            visit[i][j] = 999999;

    queue<pair<int, int>> q;
    int ans = 0;


    //레버찾기
    q.push({ S.first, S.second });
    visit[S.first][S.second] = 0;
    while (!q.empty()) {
        int y = q.front().first, x = q.front().second;
        q.pop();
        for (int i = 0; i < 4; i++) {
            int tx = x + dx[i], ty = y + dy[i];

            if (tx<0 || tx >= col || ty < 0 || ty>=row || maps[ty][tx] == 'X') {
                continue;
            }
            if (visit[ty][tx] > visit[y][x] + 1) {
                visit[ty][tx] = visit[y][x] + 1;
                q.push({ ty,tx });
            }
        }
    }

    if (visit[L.first][L.second] == 999999) {
        return -1;
    }
    answer += visit[L.first][L.second];

    for (int i = 0; i < row; i++)
        for (int j = 0; j < col; j++)
            visit[i][j] = 999999;

    //출구 찾기
    q.push({ L.first, L.second });
    visit[L.first][L.second] = 0;

    while (!q.empty()) {
        int y = q.front().first, x = q.front().second;
        q.pop();
        for (int i = 0; i < 4; i++) {
            int tx = x + dx[i], ty = y + dy[i];

            if (tx < 0 || tx >= col || ty < 0 || ty >= row || maps[ty][tx] == 'X') {
                continue;
            }
            if (visit[ty][tx] > visit[y][x] + 1) {
                visit[ty][tx] = visit[y][x] + 1;
                q.push({ ty,tx });
            }
        }
    }

    if (visit[E.first][E.second] == 999999) {
        return -1;
    }
    answer += visit[E.first][E.second];

    return answer;
}