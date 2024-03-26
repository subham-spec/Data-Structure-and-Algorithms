'''
There is no such function overloading and overriding in python

But we can achieve polymorphism in these ways.
'''

# A simple Python function to demonstrate 
# Polymorphism
def add(x, y, z = 0): 
	return x + y+z

# Polymorphism with Inheritence
class Bird:
    def intro(self):
        print("There are many types of birds.")
        
    def flight(self):
        print("Most of the birds can fly but some cannot.")

class sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")
	
class ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")


if __name__ == "__main__":
    print(add(2, 3))
    print(add(2, 3, 4))
    
    obj_bird = Bird()
    obj_spr = sparrow()
    obj_ost = ostrich()

    obj_bird.intro()
    obj_bird.flight()

    obj_spr.intro()
    obj_spr.flight()

    obj_ost.intro()
    obj_ost.flight()

