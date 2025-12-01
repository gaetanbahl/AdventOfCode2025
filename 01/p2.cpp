#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    ifstream f("input", ifstream::in);
    string line;

    int position = 50;
    int total = 0;
    int prev_pos;
    while (f >> line) {
        if (line.at(0) == 'L') {
            prev_pos = position;
            position -= stoi(line.substr(1));

            if(position < 0) {
                int floor_q = position / 100;
                if (position % 100 != 0) floor_q -= 1;
                
                total += abs(floor_q);
                if (prev_pos == 0) {
                    total -= 1;
                }
            }
            position = (position % 100 + 100) % 100; // ensure positive modulus
            if (position == 0)
                total += 1;

        } else if(line.at(0) == 'R') {
            position += stoi(line.substr(1));
            total += position / 100;
            position = position % 100;
        }
    }
    cout << total << endl;
    return 0;
}