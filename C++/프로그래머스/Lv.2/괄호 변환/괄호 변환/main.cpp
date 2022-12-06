#include<bits/stdc++.h>
using namespace std;
bool isBalance(string p) {
    return count(p.begin(), p.end(), '(') == count(p.begin(), p.end(), ')');
}
bool isCorrect(string p) {
    stack<char> op;
    for (char c : p) {
        switch (c)
        {
        case '(':
            op.push(c);
            break;
        case ')':
            if(op.empty()) return 0;
            else op.pop();
            break;
        }
    }
    return 1;
}
string trans(string p) {
    p = p.substr(1);
    p.pop_back();
    for (char& c : p) {
        switch (c)
        {
        case '(':
            c = ')';
            break;
        case ')':
            c = '(';
            break;
        }
    }
    return p;
}

string solution(string w) {
    string ret = "";
    if (w!="") {
        auto it = w.begin();
        string u = "", v = "";
        while (it != w.end()) {
            u += *it++;
            if (isBalance(u)) break;
        }
        v = w.substr(it - w.begin());
        if (isCorrect(u)) ret = u + solution(v);
        else ret = '(' + solution(v) + ')' + trans(u);
    }    
    return ret;
}

int main() {
    cout << solution("()))((()") << endl;
    return 0;
}