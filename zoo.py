'''class Animal:
    sound="sound"
    breath="breathee"
    @classmethod
    def breathe(cls):
        print(cls.sound)
        return
    @classmethod
    def make_sound(cls):
        print(cls.breath)
        return'''
    
class Deer:
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        if required_food_in_kgs<=0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        if age_in_months!=1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        self._age_in_months=age_in_months
        self._breed=breed
        self._required_food_in_kgs=required_food_in_kgs
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def breed(self):
        return self._breed
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    def grow(self):
        self._required_food_in_kgs+=2
        self._age_in_months+=1
    def breathe(self):
        print("Breathe in air")
    def make_sound(self):
        print("Buck Buck")

class Lion:
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        if required_food_in_kgs<=0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        if age_in_months!=1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        self._age_in_months=age_in_months
        self._breed=breed
        self._required_food_in_kgs=required_food_in_kgs
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def breed(self):
        return self._breed
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    
    def grow(self):
        self._required_food_in_kgs+=4
        self._age_in_months+=1
    def breathe(self):
        print("Breathe in air")
    def make_sound(self):
        print("Roar Roar")
class Shark:
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        if required_food_in_kgs<=0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        if age_in_months!=1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        self._age_in_months=age_in_months
        self._breed=breed
        self._required_food_in_kgs=required_food_in_kgs
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def breed(self):
        return self._breed
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    
    def grow(self):
        self._required_food_in_kgs+=8
        self._age_in_months+=1
    def breathe(self):
        print("Breathe oxygen from water")
    def make_sound(self):
        print("Shark Sound")
class GoldFish:
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        if required_food_in_kgs<=0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        if age_in_months!=1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        self._age_in_months=age_in_months
        self._breed=breed
        self._required_food_in_kgs=required_food_in_kgs
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def breed(self):
        return self._breed
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    
    def grow(self):
        self._required_food_in_kgs+=0.2
        self._age_in_months+=1
    def breathe(self):
        print("Breathe oxygen from water")
    def make_sound(self):
        print("Hum Hum")
class Snake:
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        if required_food_in_kgs<=0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        if age_in_months!=1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        self._age_in_months=age_in_months
        self._breed=breed
        self._required_food_in_kgs=required_food_in_kgs
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def breed(self):
        return self._breed
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    def grow(self):
        self._required_food_in_kgs+=0.5
        self._age_in_months+=1
    def breathe(self):
        print("Breathe in air")
    def make_sound(self):
        print("Hiss Hiss")
class Zoo:
    def __init__(self,reserved_food_in_kgs=0):
        self._animals_list=[]
        self._reserved_food_in_kgs=reserved_food_in_kgs
    def add_food_to_reserve(self,food_amount):
        self._reserved_food_in_kgs+=food_amount
    def add_animal(self,animal):
        self._animals_list.append(animal)
    def count_animals(self):
        return len(self._animals_list)
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
    @property
    def animals_list(self):
        return self._animals_list
    def feed(self,animal_object):
        #print(animal_object._required_food_in_kgs)
        self._reserved_food_in_kgs-=animal_object._required_food_in_kgs
        animal_object._age_in_months+=1
