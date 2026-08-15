class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name.capitalize()
        if height < 0.0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height set to default value")
            height = 0.0
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age set to default value")
            age = 0
        self._height = height
        self._age = age

    def show(self) -> None:
        cap_name = self.name.capitalize()
        print(f"{cap_name}: {self._height}cm, {self._age} days old")

    def grow(self) -> None:
        self._height = round((self._height + 0.8), 1)

    def age(self) -> None:
        self._age += 1

    def set_height(self, height: float) -> None:
        if height < 0.0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = height
        print(f"Height updated: {round((self._height), 0)}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
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
    rose = Plant("rose", 15.0, 30)
    print(
        f"Plant created: Rose: {rose.get_height()}cm, "
        f"{rose.get_age()} days old"
    )

    rose.set_height(25.0)
    rose.set_age(30)

    rose.set_height(-1.0)
    rose.set_age(-1)

    print(f"Current state: {rose.name}: ", end="")
    print(f"{rose.get_height()}cm, {rose.get_age()} days old")
