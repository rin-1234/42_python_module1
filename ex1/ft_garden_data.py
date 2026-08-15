class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        cap_name = self.name.capitalize()
        print(f"{cap_name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    plant1 = Plant("rose", 10, 10)
    plant2 = Plant("sunflower", 12, 13333)
    plant3 = Plant("cactus", 11, 11)
    plant1.show()
    plant2.show()
    plant3.show()
