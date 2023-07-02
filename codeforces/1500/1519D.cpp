// #include  <bits/stdc++.h>
#include <string>
#include <vector>
#include <iostream>
#include <math.h>
#include <algorithm>
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

ll expand(int left, int right, map<pair<int,int>, ll> &dp, vector<ll> &a, vector<ll> &b){
    if(dp.find({left, right}) != dp.end()){
        return dp[{left, right}];
    }
    if(left < 0 || right == a.size()) return 0;
    ll curr = a[right] * b[left] + a[left] * b[right];
    ll prev = a[right] * b[right] + a[left] * b[left];
    ll keep_going = expand(left-1, right + 1, dp, a, b);
    return max(keep_going + curr - prev, curr - prev);
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n; cin >> n;
    vector<ll> a(n);
    for (int i=0;i<n;++i) cin >> a[i];
    vector<ll> b(n);
    for (int i=0;i<n;++i) cin >> b[i];
    map<pair<int,int>, ll> dp;
    ll max_inc = 0;
    for(int i = 0; i < n; i++){
        max_inc = max(max_inc, expand(i, i, dp, a, b));
        max_inc = max(max_inc, expand(i, i+1, dp, a, b));
    }
    ll result = 0;
    for(int i = 0; i < n; i++){
        result += a[i] * b[i];
    }
    cout << result + max_inc << endl;
}
