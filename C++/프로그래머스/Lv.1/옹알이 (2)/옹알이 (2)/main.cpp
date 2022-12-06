#include <string>
#include <vector>

using namespace std;

int translate(string babbling) {
    string anaunce[4] = {"aya", "ye", "woo", "ma"};
    string tmpSTR;
    char CB = NULL;
    int wordIndex = 0;
    while (babbling != "") {
        tmpSTR = babbling;
        for (size_t j = 0; j < 4; j++) {
            if (babbling.find(anaunce[j]) == 0) {
                if (CB == anaunce[j][0])
                    return 0;
                babbling.erase(0, anaunce[j].size());
                CB = (anaunce[j][0]);
            }
        }
        if (tmpSTR == babbling) return 0;;
    }
    return 1;
}

int solution(vector<string> babbling) {
    int num = 0;
    for (size_t i = 0; i < babbling.size(); i++) {
        num += translate(babbling[i]);
    }
    return num;
}