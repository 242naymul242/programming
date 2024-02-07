#include <iostream>

using namespace std;

int fibonacci(int n) {
    if (n == 0 || n == 1) {
        return n;
    }

    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main(int argc, char const *argv[])
{
    cout << "Hello world" << endl;
    int n = 5;
    // cin >> n;
    cout << "Fibonacchi " << n << " = " << fibonacci(n) << endl;
    system("pause");
    return 0;
}
