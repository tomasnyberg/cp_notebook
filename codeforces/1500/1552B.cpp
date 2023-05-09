// #include  <bits/stdc++.h>
#include <string>
#include <vector>
#include <iostream>
#include <math.h>
#include <algorithm>
#include <set>

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

bool beats(vector<int> &a, vector<int> &b){
    int result = 0;
    for(int i = 0; i < a.size(); i++){
        if(a[i] < b[i]){
            result++;
        }
    }
    return result >= 3;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        vector<vector<int>> athletes;
        for(int i = 0; i < n; i++){
            vector<int> athlete(5);
            for(int j = 0; j < 5; j++){
                cin >> athlete[j];
            }
            athletes.push_back(athlete);
        }
        // for(int i = 0; i < athletes.size(); i++){
        //     print_v(athletes[i]);
        // }
        set<int> candidates;
        for(int i = 0; i < n; i++){
            candidates.insert(i);
        }
        int result = -1;
        while(candidates.size()){
            int one_candidate = *candidates.begin();
            // cout << "Trying candidate " << one_candidate << endl;
            candidates.erase(one_candidate);
            set<int> to_erase;
            int beatsCount = 0;
            for(int i = 0; i < athletes.size(); i++){
                if(beats(athletes[one_candidate], athletes[i])){
                    to_erase.insert(i);
                    beatsCount++;
                }
            }
            // cout << "He beat " << beatsCount << " athletes" << endl;
            if(beatsCount == n-1){
                result = one_candidate;
                break;
            }
            for(auto x: to_erase){
                candidates.erase(x);
            }
        }
        if(result == -1){
            cout << result << endl;
        } else {
            cout << result + 1 << endl;
        }
    }
}
