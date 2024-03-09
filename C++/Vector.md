# Usage of Vector in DSA

Initialization of Vector

    vector<int> vec; 

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

Other Functions are:

    vec.size(); --> Returns the size of the vector.
    vec.empty(); --> Returns vector is empty or not.
    vec.max_size(); --> Returns maximum size of the vector
    vec.push_back(_value) --> Add value at the end of the vector.
    vec.at(_index) --> Return the element at index.
    vec1.swap(vec2) --> Changes the values of vec1 and vec2.
    vec.front() --> Returns the first value from front.
    vec.back() --> Returns the last value from back.
    int *pos = vec.data() --> Memory pointer for the vector.

Changing the size of vector.
According to the value give in it the zeroes are added or extra elements are deleted from

    vec.resize(new_size);
        or
    vec.resize(new_size, value)

To delete the extra elements from the vector, after resize some elements are there in it, to make them garbage value

    vec.shrink_to_fit();

Capacity of the vector, currently assigned to it.

    vec.capacity();



