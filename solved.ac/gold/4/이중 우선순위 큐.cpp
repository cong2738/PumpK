#include<bits/stdc++.h>
using namespace std;
int main(){
    int T,k;
    for (size_t i = 0; i < T; i++)
    {
        map<int,int> box;
        for (size_t j = 0; j < k; j++)
        {
            char cmd;
            int num;
            map<int,int>::iterator it;
            cin>>cmd>>num;
            switch (cmd)
            {
            case 'I':
                box[num]++;
                break;
            case 'D':                
                if(num==1) it = box.begin();
                else it = box.begin();
                box[(*it).first] -= 1;
                if(box[(*it).first] == 0)box.erase(it);
            }
        }
    }
    
}