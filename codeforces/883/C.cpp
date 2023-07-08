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


pair<ll, ll> optimal(vector<ll>& problems, ll time) {
    sort(problems.begin(), problems.end());
    ll penalty = 0;
    ll solved = 0;
    ll curr_time = 0;
    for(ll p : problems) {
        if(curr_time + p <= time) {
            curr_time += p;
            penalty += curr_time;
            solved++;
        }
    }
    return make_pair(solved, penalty);
}

int main(){
    int t; cin >> t;
    while(t--){
        ll n, m, h; cin >> n >> m >> h;
        vector<pair<ll, ll>> teams(n);
        for(ll i = 0; i < n; i++){
            vector<ll> problems(m);
            for(ll j = 0; j < m; j++){
                cin >> problems[j];
            }
            teams[i] = optimal(problems, h);
        }
        pair<ll, ll> rudolfscore = teams[0];
        sort(teams.begin(), teams.end(), [](pair<ll, ll> a, pair<ll, ll> b) {
            if(a.first == b.first) return a.second < b.second;
            return a.first > b.first;
        });
        for(ll i = 0; i < n; i++){
            if(teams[i].first == rudolfscore.first && teams[i].second == rudolfscore.second){
                cout << i + 1 << endl;
                break;
            }
        }
    }
}