# Usage of Vector in DSA

Initialization of Vector

    vector<int> vec; 

Adding values to it.

    vec.push_back(_value)

Iterating over the vector

    // In the forward direction
    for (auto i = g1.begin(); i != g1.end(); ++i) 
        cout << *i << " ";

    for (auto it : vec)
        cout<<it<<endl;

    // In reverse order
    for (auto ir = g1.rbegin(); ir != g1.rend(); ++ir) 
		cout << *ir << " "; 

    // Constant iterator, if the values are fixed - TC : O(1)
    for (auto ir = g1.cbegin(); ir != g1.cend(); ++ir) 
		cout << *ir << " "; 

    // Constant iterator in reverse order, if the values are fixed - TC : O(1)
    for (auto ir = g1.crbegin(); ir != g1.crend(); ++ir) 
		cout << *ir << " "; 

Size of the vector

    vec.size();

Changing the size of vector.
According to the value give in it the zeroes are added or extra elements are deleted from

    vec.resize(_value);

Capacity of the vector, currently assigned to it.

    vec.capacity();

Maximum size of the vector

    vec.max_size();



