#include <bits/stdc++.h>
using namespace std;

const int MAXT = 5000000;
vector<bool> isPrime(MAXT + 1, true);

void sieve() {
    isPrime[0] = isPrime[1] = false;
    for (int i = 2; i * i <= MAXT; ++i) {
        if (isPrime[i]) {
            for (int j = i * i; j <= MAXT; j += i)
                isPrime[j] = false;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);


    freopen("NTMAX.INP", "r", stdin);
    freopen("NTMAX.OUT", "w", stdout);

    sieve();

    string S;
    if (!getline(cin, S)) return 0;   // đọc cả dòng (phòng trường hợp có khoảng trắng)

    long long N_digits = 0;  // số lượng ký tự số trong xâu
    int maxPrime = 0;        // số nguyên tố lớn nhất

    bool inNumber = false;   // đang ở trong một đoạn toàn chữ số
    bool hasNonZero = false; // đã gặp chữ số khác 0 trong đoạn hiện tại chưa
    bool tooBig = false;     // số hiện tại đã vượt quá MAXT hay chưa
    int cur = 0;             // giá trị số hiện tại (bỏ các số 0 vô nghĩa ở đầu)

    for (char ch : S) {
        if (isdigit(static_cast<unsigned char>(ch))) {
            // Đếm chữ số
            N_digits++;

            int d = ch - '0';

            if (!inNumber) {
                // Bắt đầu một đoạn số mới
                inNumber = true;
                hasNonZero = false;
                tooBig = false;
                cur = 0;

                if (d != 0) {
                    hasNonZero = true;
                    cur = d;
                    if (cur > MAXT) tooBig = true;
                }
            } else {
                if (!hasNonZero) {
                    if (d != 0) {
                        hasNonZero = true;
                        cur = d;
                        if (cur > MAXT) tooBig = true;
                    }
                } else {
                    if (!tooBig) {
                        cur = cur * 10 + d;
                        if (cur > MAXT) {
                            tooBig = true;
                        }
                    }
                }
            }
        } else {
            if (inNumber) {
                if (hasNonZero && !tooBig && cur <= MAXT) {
                    if (isPrime[cur]) {
                        if (cur > maxPrime) maxPrime = cur;
                    }
                }
            }
            inNumber = false;
            hasNonZero = false;
            tooBig = false;
            cur = 0;
        }
    }
    if (inNumber) {
        if (hasNonZero && !tooBig && cur <= MAXT) {
            if (isPrime[cur]) {
                if (cur > maxPrime) maxPrime = cur;
            }
        }
    }

    cout << N_digits << "\n";
    cout << maxPrime << "\n"; // nếu không có số nguyên tố, maxPrime sẽ là 0

    return 0;
}
