'''
Created on 17-Aug-2016

@author: E002642
'''
class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def __str__(self):
        print "My name is (0). I am (1) year old".format(self.name, self.age)
        

class Military(Person):
    def __init__(self,name,age,rank):
        Person.__init__(self, name, age)
        self.rank=rank
        
    def __str__(self):
        Person.__str__(self)+" I am a (0) ".format(self.rank)
        
class Teacher(Person):
    def __init__(self,name,age,sub):
        Person.__init__(self, name, age)
        self.sub=sub
        
    def __str__(self):
        Person.__str__(self)+" I am a (0) ".format(self.sub)
        
class Student(Person):
    def __init__(self,name,age,loans):
        Person.__init__(self, name, age)
        self.loans=loans
        
    def __str__(self):
        Person.__str__(self)+" I am a (0) ".format(self.loans)

person=Person("Bhadri",20)
print (person)
        
