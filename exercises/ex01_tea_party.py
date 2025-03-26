"""This is a program that will help plan a tea party, calculating number of supplies needed."""

__author__: str = "730667424"


def main_planner(guests: int) -> None:
    """The entrypoint of the program"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """Calculates how many tea bags needed for a number of people"""
    return people * 2


def treats(people: int) -> int:
    """Calculates how many treats are needed for a number of people"""
    return int((tea_bags(people=people)) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Computes the cost of purchasing treats and tea"""
    return (treat_count * 0.75) + (tea_count * 0.5)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
