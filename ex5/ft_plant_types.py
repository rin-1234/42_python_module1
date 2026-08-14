class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name.capitalize()
        self._height = height
        self._age = age

    def show(self) -> None:
        cap_name = self.name.capitalize()
        print(f"{cap_name}: {self._height}cm, {self._age} days old")

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

class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk_diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"Tree Oak now produces a shade of {self._height}cm long and {self.trunk_diameter}cm wide.")
    
    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

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

if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print("")

    print("=== Tree")
    tree = Tree("oak", 200.0, 365, 5.0)
    tree.show()
    print("[asking the oak to produce shade]")
    tree.produce_shade()
    print("")

    print("=== Vegetable")
    tomato = Vegetable("tomato", 5.0, 10, "April", 0)
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(0, 20):
        tomato.grow()
        tomato.age()
    tomato.show()