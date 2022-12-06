#include<iostream>
using namespace std;
int main() {
	int tcnum, person, price, i, j;
	string name;
	cin >> tcnum;
	for (i = 0; i < tcnum; i++) {		
		cin >> person;
		int p = 0; string n;
		for (j = 0; j < person; j++) {						
			cin >> price >> name;
			if (price > p) {
				p = price;
				n = name;
			}
		}
		cout << n << endl;
	}
}