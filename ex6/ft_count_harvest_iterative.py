def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    for i in range(1, days + 1):
        if i == days:
            print(f"Day {i} Harvest time!")
        else:
            print(f"Day {i}")
