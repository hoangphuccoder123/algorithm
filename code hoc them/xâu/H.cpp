#include<bits/stdc++.h>
using namespace std;

int main() {
    string s;
    if (!getline(cin, s)) return 0;
    s.erase(remove(s.begin(), s.end(), ' '), s.end());
    cout << s;
    return 0;
}