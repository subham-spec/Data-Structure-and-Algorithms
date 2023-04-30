#include <bits/stdc++.h>
using namespace std;
char highestOccurringChar(char input[]) {
    
    int size = strlen(input);
    char ans;
    if(size == 0)
        return ans;
    ans = input[0];
    vector<int> arr(26, 0);
    int maxi = 0;
    
    for(int i=0; i<size; i++){
        char ch = input[i];
        arr[ch-97]++;
    }

    for(int i=0; i<size; i++){
        if(arr[input[i]-97] > maxi){
            maxi = arr[input[i]-97];
            ans = input[i];
        }
    }

    return ans;
}


/*
Sample Input 1:
abdefgbabfba
Sample Output 1:
b


Sample Input 2:
xy
Sample Output 2:
x
*/