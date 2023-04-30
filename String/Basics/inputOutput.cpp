#include <bits/stdc++.h>
using namespace std;

int main(){
    string s;
    cout<<"Enter the sentence";
    //getline is used to input the sentences in s.
    getline(cin, s);
    cout<<"'"<<s<<"'";

    // To print the sentence word by word
    string t;
    stringstream X(s);

    cout<<"\nPrinting the sentence word by word"<<endl;
    string ans = "";
    while(getline(X, t, ' ')){
        ans += t;
    }

    cout<<"'"<<ans<<"'"<<endl;
}