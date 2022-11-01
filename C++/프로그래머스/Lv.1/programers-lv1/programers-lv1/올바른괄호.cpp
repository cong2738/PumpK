#include<bits/stdc++.h>

using namespace std;

bool solution(string s)
{
    queue<char> q;
    for (char c : s) {
        switch (c)
        {
        case '(':q.push(c);
            break;
        case ')':
            if (q.front() == '(') q.pop();
            else return false;
            break;
        default:
            break;
        }
    }
    if (q.empty()) return true;
    return false;
}