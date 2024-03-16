// Ugly Number II

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int nthUglyNumber(int n) {
        vector<int> arr(n);
        arr[0] = 1;
        int p2=0, p3=0, p5=0;

        for(int i=1; i<n; i++) {
            int mini = min(arr[p2]*2, min(arr[p3]*3, arr[p5]*5));
            arr[i] = mini;
            if(mini == arr[p2]*2)
                p2++;
            if(mini == arr[p3]*3)
                p3++;
            if(mini == arr[p5]*5)
                p5++;
        }
        return arr[n-1];
    }
};

/*
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.

 

Example 1:

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
Example 2:

Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
 

Constraints:

1 <= n <= 1690
*/