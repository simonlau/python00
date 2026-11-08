def ft_water_reminder() -> None:  # noqa: INP001
    days = int(input("Days since last watering: "))
    if days > 2:  # noqa: PLR2004
        print("Water the plants!")
    else:
        print("Plants are fine")
