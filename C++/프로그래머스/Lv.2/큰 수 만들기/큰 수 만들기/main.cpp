#include<bits/stdc++.h>
using namespace std;
string solution(string number, int k) {
    for (size_t i = 0; i < k; i++) {
        int tmp = 0,
            eraseindex = number.size() - 1;
        for (size_t j = 0; j < number.size(); j++) {
            if (number[tmp] < number[j]) {
                eraseindex = tmp;
                break;
            }
            tmp = j;
        }
        number.erase(eraseindex, 1);
    }
    return number;
}
int main() {
	cout << solution("4321", 2) << endl;
}