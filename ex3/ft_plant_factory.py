class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age_day = age

    def show(self) -> None:
        cap_name = self.name.capitalize()
        print(f"{cap_name}: {self.height}cm, {self.age_day} days old")

    def grow(self) -> None:
        self.height = round((self.height + 0.8), 1)

    def age(self) -> None:
        self.age_day += 1


if __name__ == "__main__":
    rose = Plant("rose", 25.0, 30)
    oak = Plant("oak", 200.0, 365)
    cactus = Plant("cactus", 5.0, 90)
    sunflower = Plant("sunflower", 80.0, 45)
    fern = Plant("fern", 15.0, 120)
    print("=== Plant Factory Output ===")
    print("Created: ", end="")
    rose.show()
    print("Created: ", end="")
    oak.show()
    print("Created: ", end="")
    cactus.show()
    print("Created: ", end="")
    sunflower.show()
    print("Created: ", end="")
    fern.show()
