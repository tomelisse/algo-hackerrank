#include <bits/stdc++.h>
#include <vector>
using namespace std;

long aVeryBigSum(int n, vector <long> ar) {
     return std::accumulate(ar.begin(), ar.end(), static_cast<long long int>(0));
}

int main() {
    int n;
    cin >> n;
    vector<long> ar(n);
    for(int ar_i = 0; ar_i < n; ar_i++){
       cin >> ar[ar_i];
    }
    long result = aVeryBigSum(n, ar);
    cout << result << endl;
    return 0;
}
