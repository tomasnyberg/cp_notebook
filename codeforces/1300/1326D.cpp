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

std::string manacher(std::string s) {
    // Transform s into T.
    std::string T = "^#" + std::string(1, s[0]);
    for (int i = 1; i < s.size(); ++i) {
        T += "#";
        T += s[i];
    }
    T += "#$";

    int n = T.size();
    std::vector<int> P(n, 0);
    int C = 0, R = 0;
    for (int i = 1; i < n-1; ++i) {
        if (R > i) {
            int i_mirror = 2*C - i;
            P[i] = std::min(R - i, P[i_mirror]);
        }
        
        // Attempt to expand
        while (T[i + 1 + P[i]] == T[i - 1 - P[i]]) {
            P[i]++;
        }

        // Update C and R if i's palindrome expands past R
        if (i + P[i] > R) {
            C = i;
            R = i + P[i];
        }
    }

    int max_length = -1, center_index = -1;
    for (int i = 1; i < n-1; ++i) {
        if (P[i] > max_length && (i - P[i] == 1 || P[i] + i == n - 2)) {
            max_length = P[i];
            center_index = i;
        }
    }

    // Extract the longest palindromic string
    std::string longest = T.substr(center_index - max_length, 2 * max_length);
    longest.erase(std::remove(longest.begin(), longest.end(), '#'), longest.end());
    return longest;
}


int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t; cin >> t;
    while(t--){
        string s; cin >> s;
        // Check if palindrome
        if(s == string(s.rbegin(), s.rend())){
            cout << s << "\n";
            continue;
        }
        string start;
        string end;
        int i = 0;
        int j = s.size() - 1;
        while (i < j) {
            if (s[i] == s[j]) {
                start.push_back(s[i]);
                end.push_back(s[j]);
                i++;
                j--;
            } else {
                break;
            }
        }
        reverse(end.begin(), end.end());
        string middle = manacher(s.substr(i, j - i + 1));
        cout << start << middle << end << "\n";
    }
}
