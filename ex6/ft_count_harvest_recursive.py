def ft_count_harvest_recursive(days: int | None = None, current: int = 1) -> None:  # noqa: INP001
    if days is None:
        days = int(input("Days until harvest: "))
    if current == days:
        print("Harvest time!")
    else:
        print(f"Day {current}")
        ft_count_harvest_recursive(days, current + 1)
