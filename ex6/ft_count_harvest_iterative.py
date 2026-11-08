# ruff: ignore[implicit-namespace-package]
def ft_count_harvest_iterative() -> None:
    days = int(input("Days until harvest: "))
    i = 0
    while i < days + 1:
        if i == days:
            print("Harvest time!")
        else:
            print(f"Day {i + 1}")
        i += 1
