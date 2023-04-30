#include <bits/stdc++.h>
using namespace std;
void print_data(int n){
    if(n==1){
        cout<<n<<' ';
        return;
    }
    print_data(n-1);
    cout<<n<<' ';
}
int main(){
    int n = 15;

    print_data(n);
}