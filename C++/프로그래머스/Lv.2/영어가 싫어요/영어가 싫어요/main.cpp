#include <string>
#include <vector>
#include<iostream>
using namespace std;

long long solution(string numbers) {
    string alnum[10] = { "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };
    string answer = "";
    while (!numbers.empty()) {
        int index;
        switch (numbers[0]) {            
        case 'z':
            index = 0;
            break;
        case 'o':
            index = 1;
            break;
        case 't':
            switch (numbers[1]) {
            case 'w':
                index = 2;
                break;
            case 'h':
                index = 3;
                break;
            default:
                break;
            }
            break;
        case 'f':
            switch (numbers[1]) {
            case 'o':
                index = 4;
                break;
            case 'i':
                index = 5;
                break;
            }
            break;
        case 's':
            switch (numbers[1]) {
            case 'i':
                index = 6;
                break;
            case 'e':
                index = 7;
                break;
            }
            break;
        case 'e':
            index = 8;
            break;
        case 'n':
            index = 9;
            break;
        default:
            break;
        }        
        numbers.replace(0, alnum[index].size(), "");
        answer += to_string(index);
    }
    return stoll(answer);
}