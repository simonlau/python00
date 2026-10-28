# Growing Code: Python Fundamentals Through Garden Data

> Sources: Growing Code, Unknown
> Raw: [Growing Code - Python Fundamentals Through Garden Data](../../raw/python-fundamentals/growing-code-python-fundamentals.md)
> Updated: 2026-10-24

## Overview

The Growing Code curriculum teaches Python fundamentals through community garden data, using garden metaphors to make programming concepts accessible and meaningful. The eight exercises progress from basic printing and input operations to advanced concepts like type hints and recursion, building essential programming skills while contributing to sustainable community initiatives.

## The Growing Code Approach

The curriculum frames Python programming as garden growth — learning should be joyful, accessible, and inclusive. Each exercise introduces a core concept through realistic garden scenarios, from tracking harvest yields to managing seed inventory, helping learners discover that programming, like gardening, is about nurturing growth both in code and in communities.

## General Instructions

All exercises follow uniform rules: write only the requested function (no main programs), place each exercise in its own file, use exact function names, and respect flake8 standards. Functions must be written in Python 3.10+ without input validation for cases with undefined behavior (like negative numbers).

Type hints are optional but recommended for exercises 0-6 and required for exercise 7. For negative numbers or invalid inputs, the behaviour is undefined.

## AI Collaboration Guidelines

This curriculum includes AI collaboration guidance for reducing repetitive tasks, developing prompting skills, understanding AI systems, and building both technical and power skills with peers. It emphasizes critically assessing AI-generated content, systematic checking of generated output, and always seeking peer review to avoid mistakes and blind spots.

## Exercise Structure

The curriculum contains eight exercises covering fundamental programming concepts:

### Exercise 0: Hello Garden
- File: `ft_hello_garden.py`
- Function: `ft_hello_garden()`
- Task: Write a function that simply displays a welcome message to the garden community

### Exercise 1: Garden Name
- File: `ft_garden_name.py`
- Function: `ft_garden_name()`
- Task: Write a function that asks for a garden name, displays it followed by "Status: Growing well!"

### Exercise 2: Garden Plot Area
- File: `ft_plot_area.py`
- Function: `ft_plot_area()`
- Task: Write a function that asks for length and width, calculates and displays the rectangular plot area

### Exercise 3: Harvest Total
- File: `ft_harvest_total.py`
- Function: `ft_harvest_total()`
- Task: Write a function that asks for harvest weights from three days and calculates the total

### Exercise 4: Plant Age Check
- File: `ft_plant_age.py`
- Function: `ft_plant_age()`
- Task: Write a function that asks for a plant's age in days and tells whether it's ready to harvest (more than 60 days)

### Exercise 5: Water Reminder
- File: `ft_water_reminder.py`
- Function: `ft_water_reminder()`
- Task: Write a function that asks for days since last watering and prints "Water the plants!" if more than 2 days, else "Plants are fine"

### Exercise 6: Count to Harvest
- Files: `ft_count_harvest_iterative.py` and `ft_count_harvest_recursive.py`
- Functions: `ft_count_harvest_iterative()` and `ft_count_harvest_recursive()`
- Task: Write both iterative and recursive versions that count from 1 to a given number, printing each day until harvest time

### Exercise 7: Seed Inventory with Type Annotations
- File: `ft_seed_inventory.py`
- Function: `ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None`
- Task: Write a function with type hints that displays seed inventory information for packets, grams, or area units

## Helper Resources

A `main.py` helper file is provided to import and test exercise functions automatically, showing clear error messages and allowing testing of individual exercises or all at once. This helper helps learners understand Python imports while focusing on writing solutions.

## Submission and Evaluation

Submit only the individual Python function files requested by each exercise. The repository structure and file names will be evaluated during defense, where you may be asked to explain your code, trace execution, or modify solutions.

Focus on clean, readable code that demonstrates understanding of Python fundamentals.

## See Also

- [Python Type Checking](python-type-checking.md)
- [Python 3.10](python-3.10.md)
