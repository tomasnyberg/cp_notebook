// #include  <bits/stdc++.h>
#include <string>
#include <vector>
#include <iostream>
#include <math.h>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

#define ll long long

template <class T>
void print_v(vector<T> &v) { cout << "["; for (auto x : v) cout << x << ","; cout << "\b]\n"; }

ll min(ll a,int b) { if (a<b) return a; return b; }
ll min(int a,ll b) { if (a<b) return a; return b; }
ll max(ll a,int b) { if (a>b) return a; return b; }
ll max(int a,ll b) { if (a>b) return a; return b; }
ll gcd(ll a,ll b) { if (b==0) return a; return gcd(b, a%b); }
ll lcm(ll a,ll b) { return a/gcd(a,b)*b; }
string to_upper(string a) { for (int i=0;i<(int)a.size();++i) if (a[i]>='a' && a[i]<='z') a[i]-='a'-'A'; return a; }
string to_lower(string a) { for (int i=0;i<(int)a.size();++i) if (a[i]>='A' && a[i]<='Z') a[i]+='a'-'A'; return a; }
bool prime(ll a) { if (a==1) return 0; for (int i=2;i<=round(sqrt(a));++i) if (a%i==0) return 0; return 1; }


ll power(ll x, ll y, ll p) {
    ll res = 1;
    x = x % p;

    while (y > 0) {
        if (y & 1)
            res = (res*x) % p;
        y = y >> 1;
        x = (x*x) % p;
    }
    return res;
}

ll modInverse(ll n, ll p) {
    return power(n, p-2, p);
}

constexpr ll multi(ll a, ll b, ll p) {
    ll res = a * b - (ll) (1.L * a * b / p) * p;
    res %= p;
    if (res < 0) {
        res += p;
    }
    return res;
}

const ll MOD = 1e9 + 7;
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t;
    cin >> t;
    while (t--) {
        int n, m;
        cin >> n >> m;
        vector<int> a;
        map<ll, ll> counts;
        for(int i = 0; i < n; i++){
            // Increase the count of by the int from cin by 1
            ll x;
            cin >> x;
            counts[x]++;
        }
        ll mult = 1;
        vector<ll> prefix_mul;
        for(auto &x: counts){
            mult *= x.second;
            mult %= MOD;
            prefix_mul.push_back(mult);
            a.push_back(x.first);
        }
        // Print all elements in counts
        ll left = 0;
        ll right = 0;
        ll mul = 1;
        ll result = 0;
        while(right < a.size()){
            mul = multi(mul, counts[a[right]], MOD);
            if(right - left + 1 == m){
                if(a[right] - a[left] == right - left){
                    result += mul;
                    result %= MOD;
                }
                if (counts[a[left]] == 0){
                    print_v(a);
                    cout << left << endl;
                    cout << a[left] << endl;
                    cout << counts[a[left]] << endl;
                    cout << "\n";
                    break;
                }
                mul *= modInverse(counts[a[left]], MOD);
                mul %= MOD;
                left++;
            }
            right++;
        }
        cout << result << "\n";
    }
}
