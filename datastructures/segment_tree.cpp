// #include <bits/stdc++.h>
#include <iostream>
#include <vector>

#define ll long long

using namespace std;

const int MAXN = 100000;
int n, t[4*MAXN]; // t = the tree itself
// tl and tr are the boundaries of the current segment
void _build(int a[], int v, int tl, int tr){
    if (tl == tr){
        t[v] = a[tl];
    } else {
        int tm = (tl + tr) / 2;
        _build(a, v*2, tl, tm);
        _build(a, v*2+1, tm+1, tr);
        t[v] = t[v*2] + t[v*2+1];
    }
}

ll sum(int v, int tl, int tr, int l, int r){
    if(l > r) return 0;
    if (l == tl && r == tr) return t[v];
    int tm = (tl + tr) / 2;
    ll a = sum(v*2, tl, tm, l, min(r, tm)); // sum of left node
    ll b = sum(v*2+1, tm+1, tr, max(l, tm+1), r); // sum of right node
    return a + b;
}

void update(int v, int tl, int tr, int pos, int new_val){
    if(tl == tr) {
        t[v] = new_val;
    } else {
        int tm = (tl + tr) / 2;
        if (pos <= tm) update(v*2, tl, tm, pos, new_val);
        else update(v*2+1, tm+1, tr, pos, new_val);
        t[v] = t[v*2] + t[v*2+1];
    }
}

// Wrapper function to make this easy to remember
void build(vector<int> &a){
    // Convert the vector to an array
    int n = a.size();
    int arr[n];
    for(int i = 0; i < n; i++) arr[i] = a[i];
    _build(arr, 1, 0, n-1);
}

int main() {
    cout << "Hello world!" << endl;
    // Integer array of size 5
    vector<int> a = {1,2,3,4,5};
    build(a);
    cout << sum(1, 0, 4, 0, 4) << endl;

}
