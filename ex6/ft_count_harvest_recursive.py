def ft_count_harvest_recursive(days: int | None = None, current: int = 1):
    if days is None:
        days = int(input("Days until harvest: "))
    if current == days:
        print(f"Day {current} Harvest time!")
    else:
        print(f"Day {current}")
        ft_count_harvest_recursive(days, current + 1)
