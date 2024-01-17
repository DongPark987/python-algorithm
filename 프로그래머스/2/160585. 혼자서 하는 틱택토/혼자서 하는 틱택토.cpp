#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(vector<string> board) {
    int answer = -1;
    int o_cnt = 0;
    int x_cnt = 0;
    for (auto i : board) {
        for (auto j : i) {
            if (j == 'X') {
                x_cnt++;
            }
            else if (j == 'O') { 
                o_cnt++;
            }
        }
    }

    int o_win = 0;
    int x_win = 0;

    for (int i = 0; i < 3; i++) {
        int row = 0;
        int col = 0;
        for (int j = 0; j < 3; j++) {
            if (board[i][j] == 'X') {
                row -= 1;
            }
            else if (board[i][j] == 'O') {
                row += 1;
            }

            if (board[j][i] == 'X') {
                col -= 1;
            }
            else if (board[j][i] == 'O') {
                col += 1;
            }
        }
        if (row == 3)
            o_win++;
        else if (row == -3)
            x_win++;
        if (col == 3)
            o_win++;
        else if (col == -3)
            x_win++;
    }

    int row = 0;
    int col = 0;
    for (int i = 0; i < 3; i++) {
        if (board[i][i] == 'X') {
            row -= 1;
        }
        else if (board[i][i] == 'O') {
            row += 1;
        }
        if (board[2 - i][i] == 'X') {
            col -= 1;
        }
        else if (board[2 - i][i] == 'O') {
            col += 1;
        }

    }
    if (row == 3)
        o_win++;
    else if (row == -3)
        x_win++;
    if (col == 3)
        o_win++;
    else if (col == -3)
        x_win++;

    if (o_cnt - x_cnt < 0 || abs(o_cnt - x_cnt)> 1)
        return 0;



    if (o_win > 0 && x_win > 0) {
        return 0;
    }

    if (o_win >= 1 and o_cnt != x_cnt + 1) {
        return 0;
    }

    if (x_win >= 1 and o_cnt != x_cnt) {
        return 0;
    }

    return 1;
}