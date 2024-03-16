# STL over SET

## Modifiers

### st.insert(_value): 
    Insert element to the container
    
### st.erase(_val), st.erase(_pointer) ,st.erase(_begin pointer, _end pointer): 
    Erase particular elements
    
### st.swap(st2): 
    Swap content between two sets.
    
### st.clear(): 
    Clear content from the container.

### auto msg = st.emplace(_value) : Returns two things 
    1. msg.first - Pointer to the element.
    2. msg.second - True/False, weather new element is inserted or not.

### auto it = st.emplace_hint(_value)
    Insert element with the pointer to itself.

## Capacity:
### st.empty(): 
    Check whether container contains any value or not.

### st.size(): 
    Return size of container.

### st.max_size(): 
    Return maximum holding capacity.

## Iterators:
### st.begin(): 
    Return iterator to beginning.
### st.end(): 
    Return iterator to end.
### st.rbegin(): 
    Return reverse iterator to reverse beginning.
### st.rend() :	
    Return reverse iterator to reverse end.
### st.cbegin() : 
    Return const_iterator to beginning.
### st.cend() :	
    Return const_iterator to end.
### st.crbegin() : 
    Return const_reverse_iterator to reverse beginning.
### st.crend() : 
    Return const_reverse_iterator to reverse end.

## Observers:
    st.key_comp	Return comparison object (public member function)
    st.value_comp	Return comparison object (public member function)

Operations:
    st.find	Get iterator to element (public member function)
    st.count	Count elements with a specific value (public member function)
    st.lower_bound	Return iterator to lower bound (public member function)
    st.upper_bound	Return iterator to upper bound (public member function)
    st.equal_range	Get range of equal elements (public member function)

Allocator:
    st.get_allocator	Get allocator (public member function)


