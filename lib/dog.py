#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed
        pass
    pass
phibe = Dog("phibe", "kig") #Instantiation
print(phibe.name) #output
print(phibe.breed)#output