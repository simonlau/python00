# ruff: ignore[implicit-namespace-package]
def ft_count_harvest_recursive(
    days: int | None = None, current: int = 1
) -> None:
    if days is None:
        days = int(input("Days until harvest: "))
    if current == days + 1:
        print("Harvest time!")
    else:
        print(f"Day {current}")
        ft_count_harvest_recursive(days, current + 1)
