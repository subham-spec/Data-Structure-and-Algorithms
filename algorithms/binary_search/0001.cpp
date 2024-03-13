#include <bits/stdc++.h>
using namespace std;

int main() {

}



/*
Binary Search Algorithm.

Set High, Set Low.

Loop until low<=high:
        mid = (low+high)/2 or low+(high-low)/2
        if mid == target
            returns;
        if mid < target
            low = mid+1
        else
            high = mid-1
*/