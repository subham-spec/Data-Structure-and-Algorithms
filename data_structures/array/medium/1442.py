# 1442. Count Triplets That Can Form Two Arrays of Equal XOR

from typing import List
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        
        l = len(arr)
        # performing xor over the arr
        new_arr = arr[:]
        for i in range(1, l):
            new_arr[i] ^= new_arr[i-1]

        count = 0
        prev = 0
        for i in range(0, l-1):
            prev = i-1
            for j in range(i+1, l):
                for k in range(j, l):
                    lhs = new_arr[i]
                    if prev != -1:
                        lhs ^= new_arr[prev]
                    rhs = new_arr[k]^new_arr[i]

                    if lhs == rhs:
                        count += 1

        return count

'''
Given an array of integers arr.

We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

Let's define a and b as follows:

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.

Return the number of triplets (i, j and k) Where a == b.

 

Example 1:

Input: arr = [2,3,1,6,7]
Output: 4
Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)
Example 2:

Input: arr = [1,1,1,1,1]
Output: 10
 

Constraints:

1 <= arr.length <= 300
1 <= arr[i] <= 108
'''