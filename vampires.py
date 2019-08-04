
class Vampire:

    coven = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.in_coffin = False
        self.blood = False

    def drink_blood(self):
        self.blood = True

    def go_home(self):
        self.in_coffin = True
    
    @classmethod
    def add(cls, name, age):
        vampire = Vampire(name, age)
        cls.coven.append(vampire)
        return vampire

    @classmethod
    def sunrise(cls):
        for vampire in cls.coven:
            if vampire.in_coffin == False or Vampire.blood == False:
                cls.coven.remove(vampire)



    @classmethod 
    def sunset(cls):
        for vampire in clas.coven:
            vampire.in_coffin == True
            vampire.drank_blood == False



in1 = Vampire.add('Eden', '25')
in2 = Vampire.add('Jay', '40')
in3 = Vampire.add('Moz', '120')
in4 = Vampire.add('Abe', '180')

print(in1)
print(in2)
print(in3)
print(in4)




