def ft_water_reminder() -> None:  # noqa: INP001
    min_water_days = 2
    days = int(input("Days since last watering: "))
    if days > min_water_days:
        print("Water the plants!")
    else:
        print("Plants are fine")
