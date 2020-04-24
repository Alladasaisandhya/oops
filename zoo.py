class Animal:
    sound="sound"
    breath="breathe"
    grow_food=0
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        if required_food_in_kgs<=0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        if age_in_months!=1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        self._age_in_months=age_in_months
        self._breed=breed
        self._required_food_in_kgs=required_food_in_kgs
    def grow(self):
        self._age_in_months+=1
        self._required_food_in_kgs+=self.grow_food
    @classmethod
    def breathe(cls):
        print(cls.breath)
    @classmethod
    def make_sound(cls):
        print(cls.sound)
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    @property
    def breed(self):
        return self._breed
def hunting(park,hunting_animal):
    c=0
    c1=0
    for animal in park.animals_list:
        if animal.__class__==Deer:
            c+=1
            park.animals_list.remove(animal)
        if animal.__class__==GoldFish:
            c1+=1
            park.animals_list.remove(animal)
    if c==0 and hunting_animal=="Deer":
        print("No deers to hunt")
    if c1==0 and hunting_animal=="GoldFish":
        print("No GoldFish to hunt")
    
class Landanimals(Animal):
    breath="Breathe in air"
    
class Wateranimals(Animal):
    breath="Breathe oxygen from water"
    
class Deer(Landanimals,Animal):
    sound="Buck Buck"
    grow_food=2
    
class Lion(Landanimals,Animal):
    sound="Roar Roar"
    grow_food=4
    def hunt(self,animal_object):
        hunting_animal="Deer"
        hunting(animal_object,hunting_animal)
    
    
class Shark(Wateranimals,Animal):
    sound="Shark Sound"
    grow_food=8
    def hunt(self,animal_object):
        hunting_animal="GoldFish"
        hunting(animal_object,hunting_animal)
    
    
class GoldFish(Wateranimals,Animal):
    sound="Hum Hum"
    grow_food=0.2
    
    
    
class Snake(Landanimals,Animal):
    sound="Hiss Hiss"
    grow_food=0.5
    def hunt(self,animal_object):
        hunting_animal="Deer"
        hunting(animal_object,hunting_animal)
    
class Zoo(Animal):
    all_number_of_animals=[]
    def __init__(self,reserved_food_in_kgs=0):
        self.animals_list=[]
        self._reserved_food_in_kgs=reserved_food_in_kgs
    def add_food_to_reserve(self,food_amount):
        self._reserved_food_in_kgs+=food_amount
    def count_animals(self):
        return len(self.animals_list)
    def add_animal(self,animal):
        self.animals_list.append(animal)
        self.all_number_of_animals.append(animal)
    def feed(self,animal_1):
        if self._reserved_food_in_kgs>0:
            self._reserved_food_in_kgs-=animal_1._required_food_in_kgs
            animal_1.grow()
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
    @classmethod
    def count_animals_in_all_zoos(cls):
        return len(cls.all_number_of_animals)
    @staticmethod
    def count_animals_in_given_zoos(list_object):
        total_number_of_animals_in_all_zoos=0
        for animal in list_object:
            total_number_of_animals_in_all_zoos+=len(list_object)
        return total_number_of_animals_in_all_zoos
