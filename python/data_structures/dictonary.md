# Use of Dictonary in Python

### To create a normal dictonary

    dict = {"name":"Subham", "age":22}

### To create empty dictonary

    empty_dict = dict()
#
    fruits_dict = dict(apple="red", banana="yellow")

### Accessing Values in dict

    name = my_dict["name"]

### Chekcing the value exists

    color = my_dict.get("red", -1) 

        Either return the value at red or -1, if not exists.

### Assigning or Modifying the value

    my_dict["favorite_color"] = "blue"

### Removing a key value pair from the dict

    del my_dict["city"]

### Iterating over dict

    for key in my_dict:
        print(key, my_dict[key])
#    
    for key, value in my_dict.items():
        print(key, value)

### Common Dictionary Methods

    keys(): All keys as a dictionary view object.
    values(): All values as a list.
    items(): All key-value pairs as tuples in a list.
    len(dict): Number of key-value pairs.
    in: Check if a key exists in the dictionary.

