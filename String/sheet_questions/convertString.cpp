#include <bits/stdc++.h> 
using namespace std;

string convertString(string str) {
	// WRITE YOUR CODE HERE
	int size = str.length();
	bool flag = true;
	
	for(int i=0; i<size; i++){
		if(flag && isalpha(str[i])){
			str[i] = toupper(str[i]);
			flag = false;
		}
		else if(isspace(str[i]))
			flag = true;				
	}
	
	return str;
}

/*
Sample Input1:

I love programming
they are playing cricket
good to see you


Sample Output 1 :

I Love Programming
They Are Playing Cricket
Good To See You
*/