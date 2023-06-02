// #include  <bits/stdc++.h>
#include <string>
#include <vector>
#include <iostream>
#include <math.h>
#include <algorithm>
#include <cmath>

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

vector<ll> find_numbers(ll l, ll r, ll m, ll a){
    ll n = m / a;
    for(int d = -1; d < 2; d++){
        ll candidate = n + d;
        if(candidate <= 0) continue;
        ll diff = m - a * candidate;
        if(abs(diff) > r - l) continue;
        // Initialize a vector res of size 3
        vector<ll> res(3);
        res[0] = a;
        if(diff < 0){
            res[1] = l;
            res[2] = l - diff;
        } else {
            res[1] = r;
            res[2] = r - diff;
        }
        return res;
    }
    return {-1, -1, -1};
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    ll t; cin >> t;
    while(t--){
        ll l, r, m; cin >> l >> r >> m;
        for(ll n = l; n <= r; n++){
            vector<ll> res = find_numbers(l, r, m, n);
            if(res[1] != -1){
                cout << res[0] << " " << res[1] << " " << res[2] << "\n";
                break;
            }
        }
    }
    
}
