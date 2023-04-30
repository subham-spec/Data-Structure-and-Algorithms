#include <bits/stdc++.h>
using namespace std;
void printpermu(int i, vector<string>& s, string res){
    if(i == s.size()){
        cout<<res<<endl;
        return;
    }
    for(int j=i; j<s.size(); j++){
        swap(s[j], s[i]);
        res.append(s[j]);
        printpermu(i+1, s, res);
        swap(s[j], s[i]);
    }
    return;
}
int main(){
    vector<string> s = {"s","u","b","h"};
    string res = "";
    printpermu(0, s, res);

    return 0;
}