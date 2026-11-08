def ft_plant_age() -> None:  # noqa: INP001
    age = int(input("Enter plant age in days: "))
    if age > 60:  # noqa: PLR2004
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
