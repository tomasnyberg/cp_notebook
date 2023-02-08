// #include  <bits/stdc++.h>
#include <string>
#include <vector>
#include <iostream>
#include <math.h>
#include <algorithm>

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

ll count_inversions(vector<int> &v){
    int k = 0;
    ll result = 0;
    for(int i = 0; i < v.size(); i++){
        if(v[i] == 1){
            k++;
        } else {
            result += k;
        }
    }
    return result;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> a(n);
        for (int i=0;i<n;++i) cin >> a[i];
        vector<int> b = a;
        vector<int> c = a;
        for(int i = 0; i < n; i++){
            if(b[i] == 0){
                b[i] = 1;
                break;
            }
        }
        for(int i = n-1; i >= 0; i--){
            if(c[i] == 1){
                c[i] = 0;
                break;
            }
        }
        ll ares = count_inversions(a);
        ll bres = count_inversions(b);
        ll cres = count_inversions(c);
        cout << max((ll) ares, max((ll) bres, (ll) cres)) << endl;
    }
}
