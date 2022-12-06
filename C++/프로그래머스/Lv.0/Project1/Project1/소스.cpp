#include<bits/stdc++.h>
using namespace std;

int solution(string A, string B) {
    reverse(A.begin(), A.end());
    reverse(B.begin(), B.end());
    int L = A.size();
    for (int i = 0; i < L; i++) {
        if (A == B) return i;
        rotate(A.begin(), A.begin() + 1, A.end());
    }
    return -1;
}
int main() {
    cout << solution("hello", "ohell");
}