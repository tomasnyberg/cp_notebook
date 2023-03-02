// #include  <bits/stdc++.h>
#include <string>
#include <vector>
#include <iostream>
#include <math.h>
#include <algorithm>
#include <vector>
#include <string>
#include <bitset>
#include <unordered_map>

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




class TrieNode {
public:
    vector<TrieNode*> children;
    int count;
    TrieNode() {
        children = vector<TrieNode*>(2, nullptr);
        count = 0;
    }
};

void insert(string word, TrieNode* root, int ii) {
    TrieNode* curr = root;
    for (char c : word) {
        int j = 1 - (c - '0');
        if (!curr->children[j]) {
            curr->children[j] = new TrieNode();
        }
        curr = curr->children[j];
    }
    curr->count++;
}

int amount_in_trie(string word, TrieNode* root) {
    TrieNode* curr = root;
    for (char c : word) {
        int j = 1 - (c - '0');
        if (!curr->children[j]) {
            return 0;
        }
        curr = curr->children[j];
    }
    return curr->count;
}

int count_ones(int num) {
    int count = 0;
    while (num != 0) {
        if (num & 1) {
            count++;
        }
        num >>= 1;
    }
    return count;
}


int main() {
    int n;
    cin >> n;
    vector<string> words(n);
    for (int i=0;i<n;++i) {
        cin >> words[i];
    }
    TrieNode* oddroot = new TrieNode();
    TrieNode* evenroot = new TrieNode();
    for (int i=0;i<n;++i) {
        int num = 0;
        int seen =0;
        string s = words[i];
        for (int j=0;j<(int)s.size();++j) {
            num ^= (1 << (s[j] - 'a'));
            seen |= (1 << (s[j] - 'a'));
        }
        if(count_ones(seen) == 26){
            continue;
        }
        string bin = bitset<26>(num).to_string();
        if (s.size() % 2 == 0){
            insert(bin, evenroot, i);
        } else {
            insert(bin, oddroot, i);
        }
    }
    ll ans = 0;
    for(int ii = 0; ii < n; ii++){
        string s = words[ii];
        int seen =0;
        int num = 0;
        for (int j=0;j<(int)s.size();++j) {
            num ^= (1 << (s[j] - 'a'));
            seen |= (1 << (s[j] - 'a'));
        }
        if(count_ones(seen) == 26){
            continue;
        }
        bitset<26> bs = bitset<26>(num);
        for(int i = 0; i < 26; i++){
            if(num & (1 << i)){
                bs[i] = 0;
            } else {
                bs[i] = 1;
            }
        }
        vector<string> possible;
        string bin2 = bs.to_string();
        for (int i=0;i<26;++i) {
            // if bin[i] is 1, change it to 0 and add that to the vector of possibilities
            if (bin2[i] == '1') {
                bin2[i] = '0';
                possible.push_back(bin2);
                bin2[i] = '1';
            }
        }
        int matches = 0;
        if (s.size() % 2 == 0){
            for (string p : possible) {
                matches += amount_in_trie(p, oddroot);
            }
        } else {
            for (string p : possible) {
                matches += amount_in_trie(p, evenroot);
            }
        }
        ans += matches;
    }
    cout << ans/ 2 << endl;
}
