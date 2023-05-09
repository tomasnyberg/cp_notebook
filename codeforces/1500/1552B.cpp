// #include  <bits/stdc++.h>
#include <string>
#include <vector>
#include <iostream>
#include <math.h>
#include <algorithm>
#include <set>
#include <random>

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
        vector<int> candidates;
        for(int i = 0; i < n; i++){
            candidates.push_back(i);
        }
        int result = -1;
        set<int> to_erase;
        while(candidates.size()){
            // Choose a random integer in the range 0 to candidates.size()
            random_device rd;
            mt19937 gen(rd());
            uniform_int_distribution<> dis(0, candidates.size()-1);
            int one_candidate = candidates[dis(gen)];
            to_erase.insert(one_candidate);
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
            vector<int> new_candidates;
            for(int i = 0; i < n; i++){
                if(to_erase.find(i) == to_erase.end()){
                    new_candidates.push_back(i);
                }
            }
            candidates = new_candidates;
        }
        if(result == -1){
            cout << result << endl;
        } else {
            cout << result + 1 << endl;
        }
    }
}
