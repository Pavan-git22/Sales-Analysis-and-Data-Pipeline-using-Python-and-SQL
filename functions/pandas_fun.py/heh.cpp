#include <iostream>
using namespace std;

class Test
{
    int *p;

public:
    Test()          // Constructor
    {
        p = new int;     // Memory allocation
        *p = 100;
        cout << "Memory allocated and value = " << p << endl;
    }

    ~Test()         // Destructor
    {
        delete p;        // Memory deallocation
        cout << "Memory deallocated" << endl;
    }
};

int main()
{
    Test t;        // Object creation (constructor called)

    return 0;      // Destructor called automatically
}