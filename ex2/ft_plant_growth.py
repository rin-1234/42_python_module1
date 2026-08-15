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
    flower = Plant("rose", 25.0, 30)
    init = flower.height
    print("=== Garden Plant Growth ===")
    flower.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        flower.grow()
        flower.age()
        flower.show()
    growth = round((flower.height - init), 1)
    print(f"Growth this week: {growth}cm")
