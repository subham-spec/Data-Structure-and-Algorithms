# Usage of Maps in DSA

Declairation of Map

    map<string, int> mp;

Assignment in Map

    mp["one"] = 1;
    mp["two"] = 2;

Iterating over the map

    for(auto it:mp){
        cout<<it.first<<endl;
        cout<<it.second<<endl;
    }

Size of the map

    mp.size()
    TC : O(1)

Inserting elements in random order

    map<int, int> mp;
    mp.insert({34,67});
            or
    mp.insert(pair<int, int>(1, 40));

Maximum size of the map, no of values it can hold

    mp.max_size()

Checking the map is empty?

    mp.empty()

Erasing a particular key and value

    mp.erase(_key_)
        or
    auto it = mp.find(45)
    mp.erase(it)

    TC : log(N)

Erases all the key value lies in between it1 till it2(excluded)

    auto it1 = mp.find(2);
    auto it2 = mp.find(5);
    mp.erase(it1, it2);

Erasing all the elements from the map. 
It will deletes all the elements from the map
    
    mp.erase() 







