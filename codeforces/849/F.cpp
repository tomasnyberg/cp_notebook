#include  <bits/stdc++.h>

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


int solve(){
    int n;
    int q;
    cin >> n >> q;
    vector<int> a(n);
    for (int i=0;i<n;++i) cin >> a[i];
    // Create a vector queries which holds the queries
    vector<vector<int>> queries;
    while(q--){
        int type;
        cin >> type;
        if(type==1){
            int l,r;
            cin >> l >> r;
            queries.push_back({type,l,r});
        } else {
            int x;
            cin >> x;
            queries.push_back({type,x});
        }
    }
    for (auto v : queries) print_v(v);
    cout << "\n\n";
    return 0;
}

int main() {
    int t;
    cin >> t;
    while(t--){
        solve();
    }
}
