#include <bits/stdc++.h>
using namespace std;
string findFirstRepeatWord(string s){
    set<string> of_string;
    string t;
    stringstream X(s);
    while(getline(X, t, ' ')){
        string word = t;
        // cout<<word<<endl;
        if(of_string.find(word) != of_string.end())
            return word;
        of_string.insert(word);
    }
    return "";
}
int main(){
    string s = "subham is a good boy but boy is not good";
    string u="Ravi had been saying that he had been there";
    string v="Ravi had been saying that";
    string w="he had had he";

    cout<<"\nReapeated word is: ";
    cout<<findFirstRepeatWord(s);
    
    cout<<"\nReapeated word is: ";
    cout<<findFirstRepeatWord(u);
    
    cout<<"\nReapeated word is: ";
    cout<<findFirstRepeatWord(v);
    
    cout<<"\nReapeated word is: ";
    cout<<findFirstRepeatWord(w);
}