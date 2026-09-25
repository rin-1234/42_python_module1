class Plant:
    def __init__(self, name: str, height: float, age: int):
        self._name = name.capitalize()
        if height < 0.0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height set to default value")
            height = 0.0
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age set to default value")
            age = 0
        self._height = height
        self._age = age

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")

    def grow(self) -> None:
        self._height = round((self._height + 0.8), 1)

    def age(self) -> None:
        self._age += 1

    def set_height(self, height: float) -> None:
        if height < 0.0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = height
        print(f"Height updated: {self._height}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = age
        print(f"Age updated: {self._age} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    print()

    rose.set_height(25.0)
    rose.set_age(30)
    print()

    rose.set_height(-1.0)
    rose.set_age(-1)
    print()

    print("Current state: ", end="")
    rose.show()
    print()
