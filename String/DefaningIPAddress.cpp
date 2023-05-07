#include <iostream>
using namespace std;

string defangIPaddr(string address) {
        string defanged;
        for (char c : address) {
            if (c == '.')
                defanged += "[.]";
            else
                defanged += c;
        }
        return defanged;
    }


/*
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
*/