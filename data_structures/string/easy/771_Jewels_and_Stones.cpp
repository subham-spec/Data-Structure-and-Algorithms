#include <bits/stdc++.h>
using namespace std;

int numJewelsInStones(string jewels, string stones) {
        map<char, int> mp;
        for(char ch: stones)
            mp[ch]++;
        int count = 0;
        for(char ch: jewels)
            count += mp[ch];
        return count;       
    }

/*
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

 

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0
 

Constraints:

1 <= jewels.length, stones.length <= 50
*/