# Multilevel Inrheritance

class Father:

    def grandpa_met(self):
        return "this is a grandpa method"

class Parent(Father):

    def parent_met(self):
        return "this is a parent method"

class Child(Parent):

    def child_met(self):
        return "this is a child method"

c=Child()
print(c.child_met())
print(c.grandpa_met())
print(c.parent_met())