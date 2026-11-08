def ft_count_harvest_iterative() -> None:  # ruff: ignore[implicit-namespace-package]
    days = int(input("Days until harvest: "))
    for i in range(1, days + 1):
        if i == days:
            print("Harvest time!")
        else:
            print(f"Day {i}")
