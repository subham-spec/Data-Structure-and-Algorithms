#include <bits/stdc++.h>
using namespace std;

int main(){
    string s = "I am Shubham Sharma, and I am a student";

    // printing the main String
    cout<<"Original : "<<s<<endl;

    cout<<"Itetration 1: "<<endl;
    for(auto it = s.begin(); it!=s.end(); it++){
        cout<<*it;
    }
}