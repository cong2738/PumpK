#include<iostream>
#include <string>
#include <vector>
#include<deque>
using namespace std;

deque<char> eraseSrDot(deque<char> idline) {
    deque<char> rtdq;
    while (!idline.empty()) {
        char c = idline.front();
        idline.pop_front();
        if (c == '.') {
            while (c == idline.front()) {
                idline.pop_front();
            }
        }
        rtdq.push_back(c);
    }
    return rtdq;
}
string solution(string new_id) {
    string answer = "";
    deque<char> idline;
    for (char c : new_id) {
        if (isalpha(c) || (c >= '0' && c <= '9') || c == '_' || c == '-' || c == '.') {
            if (c >= 'A' && c <= 'Z')
                c = c - 'A' + 'a';
            idline.push_back(c);
        }
    }
    idline = eraseSrDot(idline); cout << ':';
    if (idline.front() == '.') idline.pop_front();
    while (!idline.empty() && answer.size() < 15)
    {
        char c = idline.front();
        idline.pop_front();
        answer += c;
    }
    if (answer.back() == '.') {
        answer.pop_back();
        if (!idline.empty()) answer += idline.front();
    }
    if (answer.size() == 0) answer = "aaa";
    else if (answer.size() < 3) {
        while (answer.size() < 3) {
            answer += answer.back();
        }
    }
    return answer;
}