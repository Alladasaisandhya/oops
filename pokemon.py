class Pokemon:
    sound="sound"
    def __init__(self,name,level):
        
        if name=="":
            raise ValueError("name cannot be empty")
        if level<=0:
            raise ValueError("level should be > 0")
        self._name=name
        self._level=level
    @property
    def name(self):
        return self._name
    @property
    def level(self):
        return self._level
class Pikachu(Pokemon):
    def __str__(self):
        return "{} {} {} {}".format(self.name,'-',"Level",self.level)
    @classmethod
    def make_sound(cls):
        print("Pika Pika")
    @classmethod
    def run(cls):
        print("Pikachu running...")
    def attack(self):
        print("Electric attack with {} damage".format(10*self.level))
class Squirtle(Pokemon):
    def __str__(self):
        return "{} {} {} {}".format(self.name,'-',"Level",self.level)
    @classmethod
    def make_sound(cls):
        print("Squirtle...Squirtle")
    @classmethod
    def run(cls):
        print("Squirtle running...")
    @classmethod
    def swim(cls):
        print("Squirtle swimming...")
    def attack(self):
        print("Water attack with {} damage".format(9*self.level))
class Pidgey(Pokemon):
    def __str__(self):
        return "{} {} {} {}".format(self.name,'-',"Level",self.level)
    @classmethod
    def make_sound(cls):
        print("Pidgey...Pidgey")
    @classmethod
    def fly(cls):
        print("Pidgey flying...")
    def attack(self):
        print("Air attack with {} damage".format(5*self.level))
class Swanna(Pokemon):
    def __str__(self):
        return "{} {} {} {}".format(self.name,'-',"Level",self.level)
    @classmethod
    def make_sound(cls):
        print("Swanna...Swanna")
    @classmethod
    def fly(cls):
        print("Swanna flying...")
    @classmethod
    def swim(cls):
        print("Swanna swimming...")
    def attack(self):
        print("Water attack with {} damage".format(9*self.level))
        print("Air attack with {} damage".format(5*self.level))
class Zapdos(Pokemon):
    def __str__(self):
        return "{} {} {} {}".format(self.name,'-',"Level",self.level)
    @classmethod
    def make_sound(cls):
        print("Zap...Zap")
    @classmethod
    def fly(cls):
        print("Zapdos flying...")
    def attack(self):
        print("Electric attack with {} damage".format(10*self.level))
        print("Air attack with {} damage".format(5*self.level))
class Island:
    island_list=[]
    def __init__(self,name,max_no_of_pokemon,total_food_available_in_kgs):
        self._name=name
        self._max_no_of_pokemon=max_no_of_pokemon
        self._total_food_available_in_kgs=total_food_available_in_kgs
        self._pokemon_left_to_catch=0
    @property
    def name(self):
        return self._name
    @property
    def max_no_of_pokemon(self):
        return self._max_no_of_pokemon
    @property
    def total_food_available_in_kgs(self):
        return self._total_food_available_in_kgs
    @property
    def pokemon_left_to_catch(self):
        return self._pokemon_left_to_catch
    
    
    
    def __str__(self):
        return "{} {} {} {} {} {} {}".format(self.name,'-',self.pokemon_left_to_catch,"pokemon",'-',self.total_food_available_in_kgs,"food")
    def add_pokemon(self,pokemon):
        self.island_list.append(pokemon)
        if self._pokemon_left_to_catch<self._max_no_of_pokemon:
            self._pokemon_left_to_catch+=1
        else:
            print("Island at its max pokemon capacity")
class Trainer:
    def __init__(self,name):
        #super().__init__()
        self._name=name
        self._experience=100
        self._max_food_in_bag=10*self.experience
        self._food_in_bag=0
    @property
    def name(self):
        return self._name
    @property
    def experience(self):
        return self._experience
    @property
    def max_food_in_bag(self):
        return self._max_food_in_bag
    @property
    def food_in_bag(self):
        return self._food_in_bag
    def collect_food(self):
        pass
        
'''island=Island("sai",10,100)   
island = Island(name="Island1", max_no_of_pokemon=0, total_food_available_in_kgs=10000) 
island.add_pokemon(island)
island = Island(name="Island2", max_no_of_pokemon=0, total_food_available_in_kgs=10000)
island.add_pokemon(island)
island = Island(name="Island3", max_no_of_pokemon=0, total_food_available_in_kgs=10000)
island.add_pokemon(island)
island = Island(name="Island4", max_no_of_pokemon=0, total_food_available_in_kgs=10000)
island.add_pokemon(island)
island = Island(name="Island5", max_no_of_pokemon=0, total_food_available_in_kgs=10000)
island.add_pokemon(island)
trainer=Trainer("sai")
trainer.get_all_islands()'''
 #for i in self.island_list:
            #print(i)
    '''def get_all_islands(self):
        for i in self.island_list:
            self.__str__()'''
    
    
        
        
        
        
        
    
