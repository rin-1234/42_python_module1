class Plant:
    class Stats:
        def __init__(self) -> None:
            self.grow_count = 0
            self.age_count = 0
            self.show_count = 0

        def show(self) -> None:
            print(
                f"Stats: {self.get_grow_count()} grow, "
                f"{self.get_age_count()} age, "
                f"{self.get_show_count()} show"
            )

        def get_grow_count(self) -> int:
            return self.grow_count

        def get_age_count(self) -> int:
            return self.age_count

        def get_show_count(self) -> int:
            return self.show_count

        def set_grow_count(self) -> None:
            self.grow_count += 1

        def set_age_count(self) -> None:
            self.age_count += 1

        def set_show_count(self) -> None:
            self.show_count += 1

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
    ) -> None:
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
        self._stats = Plant.Stats()

    def show(self) -> None:
        cap_name = self.name.capitalize()
        print(f"{cap_name}: {self._height}cm, {self._age} days old")
        self._stats.set_show_count()

    def show_stats(self) -> None:
        print(f"[statistics for {self.name}]")
        self._stats.show()

    def grow(self) -> None:
        self._height = round((self._height + 0.8), 1)
        self._stats.set_grow_count()

    def age(self) -> None:
        self._age += 1
        self._stats.set_age_count()

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

    @staticmethod
    def is_more_than_year(num: int) -> bool:
        return num > 365

    @classmethod
    def make_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
    ) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_bloom = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.is_bloom is False:
            print(f"{self.name} has not bloomed yet")
        else:
            print(f"{self.name} is blooming beautifully!")

    def bloom(self) -> None:
        self.is_bloom = True


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
    ) -> None:
        super().__init__(name, height, age, color)
        self.seed_count = 0

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seed_count}")

    def bloom(self) -> None:
        super().bloom()
        self.seed_count += 42


class Tree(Plant):
    class TreeStats:
        def __init__(self) -> None:
            self.shade_count = 0

        def show(self) -> None:
            print(f"{self.shade_count} shade")

        def get_shade_count(self) -> int:
            return self.shade_count

        def set_shade_count(self) -> None:
            self.shade_count += 1

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float,
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._tree_stats = Tree.TreeStats()

    def produce_shade(self) -> None:
        print(
            f"Tree Oak now produces a shade of {self._height}cm long "
            f"and {self.trunk_diameter}cm wide."
        )
        self._tree_stats.set_shade_count()

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def show_stats(self) -> None:
        super().show_stats()
        self._tree_stats.show()


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str,
        nutritional_value: int,
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def age(self) -> None:
        super().age()
        self.nutritional_value += 1


def show_statistic(plant: Plant) -> None:
    plant.show_stats()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_more_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_more_than_year(400)}")
    print()

    print("=== Flower")
    rose = Flower("rose", 15.0, 10, "red")
    rose.show()
    show_statistic(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    show_statistic(rose)

    print("=== Tree")
    oak = Tree("oak", 200.0, 365, 5.0)
    oak.show()
    show_statistic(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    show_statistic(oak)
    print()

    print("=== Seed")
    sunflower = Seed("sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    show_statistic(sunflower)
    print()

    print("=== Anonymous")
    anonymous = Plant.make_anonymous()
    anonymous.show()
    show_statistic(anonymous)
