class TeaLeaf:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age + 2
    
    @age.setter
    def age(self, age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Tea leaf age must be between 1 and 5 years")

leaf = TeaLeaf(2)
print(leaf._age)
print(leaf.age)    # direct access (2)
leaf.age = 4       # uses setter (valid, sets _age=4)
print(leaf.age)    # uses getter (returns 4+2 = 6)
