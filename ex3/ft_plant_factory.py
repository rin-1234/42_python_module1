class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age_day = age

    def show(self) -> None:
        cap_name = self.name.capitalize()
        print(f"{cap_name}: {self.height}cm, {self.age_day} days old")

    def grow(self):
       self.height = round((self.height + 0.8), 1) 

    def age(self):
        self.age_day += 1

if __name__ == "__main__":
    rose = Plant("rose", 25.0, 30)
    oak = Plant("oak", 25.0, 30)
    cactus = Plant("cactus", 25.0, 30)
    sunflower = Plant("sunflower", 25.0, 30)
    fern = Plant("fern", 25.0, 30)
    print("=== Plant Factory Output ===")
    print(f"Created: ", end="")
    rose.show()
    print(f"Created: ", end="")
    oak.show()
    print(f"Created: ", end="")
    cactus.show()
    print(f"Created: ", end="")
    sunflower.show()
    print(f"Created: ", end="")
    fern.show()