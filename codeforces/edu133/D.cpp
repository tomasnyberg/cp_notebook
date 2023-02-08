// #include  <bits/stdc++.h>
#include <string>
#include <vector>
#include <iostream>
#include <math.h>

using namespace std;

#define ll long long

template <class T>
void print_v(vector<T> &v) { cout << "{"; for (auto x : v) cout << x << ","; cout << "\b}"; }

ll min(ll a,int b) { if (a<b) return a; return b; }
ll min(int a,ll b) { if (a<b) return a; return b; }
ll max(ll a,int b) { if (a>b) return a; return b; }
ll max(int a,ll b) { if (a>b) return a; return b; }
ll gcd(ll a,ll b) { if (b==0) return a; return gcd(b, a%b); }
ll lcm(ll a,ll b) { return a/gcd(a,b)*b; }
string to_upper(string a) { for (int i=0;i<(int)a.size();++i) if (a[i]>='a' && a[i]<='z') a[i]-='a'-'A'; return a; }
string to_lower(string a) { for (int i=0;i<(int)a.size();++i) if (a[i]>='A' && a[i]<='Z') a[i]+='a'-'A'; return a; }
bool prime(ll a) { if (a==1) return 0; for (int i=2;i<=round(sqrt(a));++i) if (a%i==0) return 0; return 1; }

const int MOD = 998244353;

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> dp(n+1), ans(n+1);
    dp[0] = 1;
    for (int mn = 0; mn + k <= n; mn += k++){
        vector<int> sum(k);
        for(int i = mn; i <= n; i++){
            int cur = dp[i];
            dp[i] = sum[i % k];
            (sum[i%k] += cur) %= MOD;
            (ans[i] += dp[i]) %= MOD;
        }
    }
    for (int i = 1; i <= n; i++) cout << ans[i] << " ";
    cout << endl;
}
