#include <bits/stdc++.h>
using namespace std;

#define ll long long

vector<ll> prefix_sum(vector<int> &a){
    vector<ll> result(a.size());
    ll total = 0;
    for(int i = 0; i < a.size(); i++){
        total += a[i];
        result[i] = total;
    }
    return result;
}

int main() {
    vector<int> a = {1,2,3,4,5};
    vector<ll> ps = prefix_sum(a);
    for (auto x : ps) cout << x << " ";
    cout << endl;
}