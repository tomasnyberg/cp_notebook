// #include  <bits/stdc++.h>
#include <string>
#include <vector>
#include <iostream>
#include <math.h>
#include <algorithm>
#include <cmath>
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


class SparseTable {
public:
    SparseTable(const std::vector<int>& values) : N(values.size()) {
        // Compute the log base 2 of each index
        int logN = static_cast<int>(std::log2(N)) + 1;
        log2_.resize(N+1);
        for (int i = 2; i <= N; i++) {
            log2_[i] = log2_[i/2] + 1;
        }

        // Compute the sparse table
        table_.resize(logN, std::vector<int>(N));
        for (int i = 0; i < N; i++) {
            table_[0][i] = values[i];
        }
        for (int j = 1; j < logN; j++) {
            for (int i = 0; i + (1 << j) <= N; i++) {
                table_[j][i] = std::max(table_[j-1][i], table_[j-1][i+(1<<(j-1))]);
            }
        }
    }

    // Returns the maximum value in the range [l, r]
    int query(int l, int r) const {
        int j = log2_[r-l+1];
        return std::max(table_[j][l], table_[j][r-(1<<j)+1]);
    }

private:
    int N;
    std::vector<int> log2_;
    std::vector<std::vector<int>> table_;
};

int main() {
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        vector<pair<int,int>> xs(n);
        for(int i = 0; i < n; i++){
            pair<int,int> p;
            cin >> p.first >> p.second;
            xs[i] = p;
        }
        sort(xs.begin(), xs.end(), [](const auto& lhs, const auto& rhs) {
            if(lhs.first == rhs.first) return lhs.second < rhs.second;
            return lhs.first < rhs.first;
        });
        vector<int> a(n);
        vector<int> b(n);
        for(int i = 0; i < n; i++){
            a[i] = xs[i].first;
            b[i] = xs[i].second;
        }
        SparseTable st(b);
        ll result = 1e18;
        set<int> sl;
        for(int i = 0; i < n; i++){
            ll biggest = 1;
            auto lb = sl.lower_bound(a[i]);
            vector<int> candidates;
            if (lb != sl.end()) {
                candidates.push_back(*lb);
            }
            if(lb != sl.begin()){
                auto prev = lb;
                prev--;
                candidates.push_back(*prev);
            }
            if(lb != sl.end()){
                auto next = lb;
                next++;
                if(next != sl.end()) candidates.push_back(*next);
            }
            // Sort the candidates by the absolute diff between them and a[i]
            sort(candidates.begin(), candidates.end(), [a, i](const auto& lhs, const auto& rhs) {
                return abs(lhs - a[i]) < abs(rhs - a[i]);
            });
            // print_v(candidates);
            ll biggestother = i == a.size() -1 ? candidates[0] : st.query(i+1, n-1);
            ll otherbig = max(candidates.empty() ? -100000 : candidates[0], biggestother);
            result = min(result, abs(a[i] - otherbig));
            // cout << "i: " << i << " result " << result << endl;
            sl.insert(b[i]);
        }
        cout << result << endl;
    }
}
