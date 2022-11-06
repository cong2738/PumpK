using namespace std;
#include <vector>
vector<long long> solution(vector<long long> numbers)
{
    vector<long long> answer;
    for (long long number : numbers)
    {
        long long bit = 1;
        while (number & bit) {
            bit <<= 1;
        }
        answer.push_back(number + bit - (bit >> 1));
    }
    return answer;
}

#include<iostream>
int main() {
    vector<long long> numbers = { 2,7 };
    for (long long i : solution(numbers)) cout << i << ' ';
}