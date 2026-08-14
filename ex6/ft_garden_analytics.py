

class Plant:
    class Stats:
        def __init__(self):
            self.grow_count = 0
            self.age_count = 0
            self.show_count = 0
        
        def show(self):
            print(f"grow() called: {self._grow_count} times")
            print(f"age() called: {self._age_count} times")
            print(f"show() called: {self._show_count} times")


    def __init__(self, name: str, height: float, age: int):
        self.name = name.capitalize()
        self._height = height
        self._age = age
        self._stats = Plant.Stats()

    def show(self) -> None:
        cap_name = self.name.capitalize()
        print(f"{cap_name}: {self._height}cm, {self._age} days old")

    def show_stats(self) -> None:
        self._stats.show()

    def grow(self):
       self._height = round((self._height + 0.8), 1) 

    def age(self):
        self._age += 1

    def set_height(self, height: float):
        if height < 0.0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = height
        print(f"Height updated: {round((self._height), 0)}cm")

    def set_age(self, age: int):
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = age
        print(f"Age updated: {self._age} days")

    def get_height(self):
        return self._height
    
    def get_age(self):
        return self._age
    
    @staticmethod
    def is_more_year(num : int);
        if num > 365
            return True
        else
            return False
    
    @classmethod
    def make_anonymous(cls):
        return cls("", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self.is_bloom = False

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self.is_bloom is False:
           print(f"{self.name} has not bloomed yet") 
        else:
            print(f"{self.name} is blooming beautifully!")

    def bloom(self):
       self.is_bloom = True 

class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str, seed_count: int = 0):
        super()__init__(name, height, age, color)
        self.seed_count = seed_count

    def show(self)
        super().show()
        print(f"seed_count: {self.seed_count}") 

class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk_diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.produce_shade_count = 0

    def produce_shade(self):
        print(f"Tree Oak now produces a shade of {self._height}cm long and {self.trunk_diameter}cm wide.")
        self.produce_shade_count += 1

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")
        print(f"Produce shade count: {self.produce_shade_count} times")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str, nutritional_value: int):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def age(self):
        super().age()
        self.nutritional_value += 1

def show_statistic(plant: Plant)
    print(f"{plant.name}: grow_count: {plant._stats.grow_count}, age_count: {plant._stats.age_count}, show_count: {plant._stats.show_count}")

