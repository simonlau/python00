def ft_plant_age() -> None:  # noqa: INP001
    min_harvest_age = 60
    age = int(input("Enter plant age in days: "))
    if age > min_harvest_age:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
