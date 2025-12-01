#include <iostream>
#include <fstream>
#include <string>
using namespace std;


int main() {
    ifstream f("input", ifstream::in);
    string line;

    int position = 50;
    int total = 0;
    while (f >> line) {
        if (line.at(0) == 'L') {
            position -= stoi(line.substr(1));
        } else if(line.at(0) == 'R') {
            position += stoi(line.substr(1));
        }
        position = position % 100;
        if (position == 0)
            total += 1;
    }
    cout << total << endl;
    return 0;
}