#include <bits/stdc++.h>
using namespace std;
void printSubSequence(string input, string output){
    if(input.empty()){
        cout<<output<<' ';
        return;
    }
    printSubSequence(input.substr(1), output+input[0]);
    printSubSequence(input.substr(1), output);
    return;
}
int main(){
    string input = "subh";
    string output = "";
    printSubSequence(input, output);
}