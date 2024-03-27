# Decorators in Pyhton

def bark(text):
    print(text.upper())

if __name__ == '__main__':
    ## passing function as a parameter
    print('1 -- Function passes as an Object')
    obj1 = bark
    obj1('Bhow-Bhow')

    