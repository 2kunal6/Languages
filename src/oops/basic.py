class par:
    def __init__(self, name):
        self.name = name
    def p(self):
        print(self.name)

class child(par):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    def pr(self):
        print(self.name, self.age)

c = child('a', 10)
c.pr()
