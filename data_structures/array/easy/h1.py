# Minimum Length

def sortSameArray(arr1, arr2, n):
    i, j = 0, n-1
    while i<j:
        if arr1[i]!=arr2[i] and arr1[j]!=arr2[j]:
            break
        if arr1[i]==arr2[i]:
            i += 1
        if arr1[j]==arr2[j]:
            j -= 1
    return 0 if i>j else j-i+1
    
if __name__ == "__main__":
    test_cases = int(input())
    for i in range(test_cases):
        n = int(input())
        arr1 = list(map(int, input().split()))
        arr2 = list(map(int, input().split()))

        ans = sortSameArray(arr1, arr2, n)
        print(ans)

'''

Arrays, 1-D, Data Structures
Problem
You are given two arrays A and B, of length N. 
You can select any subarray and then sort the elements in ascending order of that subarray for arrays A and B.

Find the minimum length of the subarray you can choose to make A and B same after performing the operation. 
A and B are permutations of each other.

Input Format:

The first line contains an integer T denoting the number of test cases.
The first line of each test case contains an integer N.
The next line of each test case contains N space-separated integers, elements of array A
The next line of each test case contains N space-separated integers, elements of array B
Output Format:

For each test case, print the minimum length of the subarray you can choose to make A and B same after performing the operation.

Constraints:
Sample Input
2
3
2 3 1 
2 1 3
4
1 1 2 1
2 1 1 1
Sample Output
2
3
Time Limit: 1
Memory Limit: 256
Source Limit:

Explanation
First test case:
We can choose a subarray from index to (1-based indexing). Hence, the answer is 

Second test case:
We can choose a subarray from index to (1-based indexing). Hence, the answer is 
'''