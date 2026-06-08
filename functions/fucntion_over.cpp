//function overloading
#include <iostream>
using namespace std;

int add(int a, int b) {
    return a + b;
}

double add(double a, double b) {
    return a + b;
}

int main() {
    cout << add(5, 10) << endl;
    cout << add(5.5, 10.5) << endl;
    return 0;
}   