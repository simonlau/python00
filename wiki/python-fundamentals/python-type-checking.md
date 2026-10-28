# Python Type Checking

> Sources: Real Python, 2019-01-07
> Raw: [Python Type Checking (Guide)](../../raw/python-fundamentals/2019-01-07-python-type-checking.md); [What's New In Python 3.10](../../raw/python-fundamentals/python-3.10-whats-new.md)
> Updated: 2026-10-28

## Overview

Python is dynamically typed: the interpreter checks types as code runs and variables may change type over their lifetime. PEP 484 introduced type hints, which make it possible to also perform static type checking of Python code without changing its runtime behavior. This guide covers the Python type system, annotations, composite types, type variables, protocols, and static checkers such as mypy.

## Type Systems

### Dynamic Typing

In a dynamically typed language, type checking happens only as code runs, and the type of a variable is allowed to change over its lifetime. Python's `type()` returns the type of an object, confirming that a variable's type may change and Python infers the type as it changes.

### Static Typing

Static type checks are performed without running the program. In most statically typed languages this is done as the program is compiled. Python remains a dynamically typed language, but PEP 484 introduced type hints, which make static type checking of Python code possible. Unlike most statically typed languages, type hints by themselves do not cause Python to enforce types; they are only suggestions, and other tools perform static type checking using them.

### Duck Typing

Duck typing is related to dynamic typing: the type or class of an object is less important than the methods it defines. Instead of checking types, you check for the presence of a given method or attribute. For example, `len()` can be called on any object defining a `.__len__()` method. Duck typing is somewhat supported in static type checking of Python code using structural subtyping.

## Hello Types

Type hints are added by annotating arguments and the return value of a function. For example, `def headline(text: str, align: bool = True) -> str:` annotates `text` as `str`, `align` as `bool` with default `True`, and the return as `str`. Style recommendations: no space before and one space after a colon; spaces around `=` when combining an annotation with a default value; spaces around the `->` arrow.

Type hints have no runtime effect on their own. A static type checker such as mypy can detect incorrect types. mypy is commonly installed with `pip install mypy` and run as `mypy headlines.py`.

## Pros and Cons

Advantages of type hints: they help catch certain errors, document code, improve IDEs and linters (better completion), and encourage a cleaner architecture by forcing thought about types. Downsides: they take developer time, work best in modern Python (annotations in 3.0, variable annotations in 3.6), and introduce a slight startup-time penalty when importing `typing`. Python supports gradual typing, so types can be introduced incrementally; code without hints is ignored by the checker.

## Annotations

### Function Annotations

For functions, annotate arguments and the return value: `def func(arg: arg_type, optarg: arg_type = default) -> return_type:`. Annotations are stored in the function's `.__annotations__` attribute. mypy provides `reveal_type()` and `reveal_locals()` to inspect inferred types during development.

### Variable Annotations

PEP 526 introduced variable annotations in Python 3.6, using the same syntax as function arguments, for example `pi: float = 3.142`. Annotations of variables are stored in the module-level `__annotations__` dictionary. A variable may be annotated without being assigned a value.

### Type Comments

Type comments are specially formatted comments compatible with older Python versions, for example `# type: (float) -> float` on the line after the function definition. They are handled by the type checker and are not available in `__annotations__`. The recommendation is to use annotations when possible and type comments when necessary, with stub files as a third option.

## Playing With Python Types, Part 1

### Example: A Deck of Cards

A card game example represents each card as a tuple of two strings and the deck as a list of cards. `create_deck()` builds 52 cards and optionally shuffles; `deal_hands()` deals them to four players.

### Sequences and Mappings

Composite types should use special types from the `typing` module rather than bare `list` or `tuple`, so element types are specified: `List[str]`, `Tuple[int, int, int]`, `Dict[str, bool]`. A tuple is an immutable sequence of a fixed number of possibly differently typed elements; a list is a mutable sequence of an unknown number of elements of the same type. For function arguments expecting any sequence, use `typing.Sequence` to express duck typing.

### Type Aliases

Type aliases are created by assigning a type expression to a variable, for example `Card = Tuple[str, str]` and `Deck = List[Card]`. They make nested type hints readable and can be inspected to see what they represent.

### Functions Without Return Values

Functions without an explicit return still return `None`. Annotate such functions with `-> None` to catch bugs where a meaningless return value is used. This differs from omitting the return annotation, where mypy has no information. Functions that never return normally can use `NoReturn`.

### The Any Type

`Any` is a special type that can hold any value. Annotating a parameter as `Sequence[Any]` returning `Any` loses type information, since the specific item type is discarded.

## Type Theory

### Subtypes

A type `T` is a subtype of `U` if every value of `T` is also a value of `U` and every function of `U` is also a function of `T`. This guarantees a variable of type `T` can pretend to be `U`. For example, `bool` is a subtype of `int`. Subtypes relate to but are not identical to subclasses; for instance `int` is a subtype of `float` but not a subclass of it.

### Covariant, Contravariant, and Invariant

Composite types may be covariant (preserving the type hierarchy, as `Tuple`), invariant (no subtype guarantee, as `List`), or contravariant (reversing the hierarchy, as `Callable` arguments). Subtypes and composite types can be non-intuitive.

### Gradual Typing and Consistent Types

Gradual typing is enabled by `Any`, which sits at both top and bottom of the subtype hierarchy in a sense. A type `T` is consistent with `U` if `T` is a subtype of `U` or either is `Any`. The checker only complains about inconsistent types, so `Any` never causes errors but disables checking for that value.

## Playing With Python Types, Part 2

### Type Variables

A type variable, created with `TypeVar`, ranges over possible types and takes the most specific type. It preserves type information through generic functions like `choose()`, whereas `Any` would discard it. Type variables can be constrained to a set of acceptable types.

### Duck Types and Protocols

A nominal system compares types by names and declarations; a structural system compares by structure. Protocols (PEP 544) define structural types: any class implementing the required methods fulfills the protocol. The `typing` module provides protocols such as `Sized`, `Container`, `Iterable`, `Awaitable`, and `ContextManager`. Custom protocols can be defined by inheriting from `Protocol`.

### The Optional Type

`Optional[T]` (equivalent to `Union[None, T]`) annotates values that may be `T` or `None`. When operating on such a value, the code must handle the `None` case to avoid type errors.

### Type Hints for Methods

Method type hints work like function hints; `self` and `cls` need not be annotated. `.__init__()` should return `None`. Classes can be used as types by name. Forward references to not-yet-defined classes use string literals, or `from __future__ import annotations` in Python 3.7+.

### Returning self or cls

When a superclass method returns `self` or `cls`, annotate using a type variable bound to the class (e.g., `TAnimal = TypeVar("TAnimal", bound="Animal")`) so subclasses get their own type rather than the superclass type.

### Annotating *args and **kwargs

For `*args`, annotate the type of each individual argument, not the tuple. For `**kwargs`, annotate the type of each keyword argument value.

### Callables

Functions are first-class objects represented by `typing.Callable`. `Callable[[A1, A2], Rt]` denotes a callable taking arguments of types `A1`, `A2` and returning `Rt`.

## Type Hints in Python 3.10

Python 3.10 introduced several improvements to type hints (see [Python 3.10](python-3.10.md)):
- **PEP 604**: New union type operator `X | Y` as a cleaner alternative to `typing.Union`, also accepted by `isinstance()` and `issubclass()`.
- **PEP 612**: Parameter specification variables (`ParamSpec`) and `Concatenate` operator to forward parameter types in higher-order functions and decorators.
- **PEP 613**: Explicit `TypeAlias` annotation to distinguish type aliases from ordinary assignments.
- **PEP 647**: `TypeGuard` for user-defined type guards to improve type narrowing.

## Static Type Checking

### The Mypy Project

Mypy, started by Jukka Lehtosalo around 2012, is a static type checker for regular Python code. It uses annotations to check types without running the program.

### Running Mypy

Install with `pip install mypy` and run with `mypy my_program.py`. Options include `--ignore-missing-imports` for third-party packages without hints. Configuration can be stored in `mypy.ini` with per-module sections.

### Adding Stubs

Stub files (`.pyi`) add type hints to code that cannot be changed, containing signatures with `...` bodies instead of implementations. Set `MYPYPATH` to a directory of stubs. This is how types are added to third-party packages.

### Typeshed

Typeshed is a repository of type hints for the standard library and third-party packages, included with mypy. Contributing type hints to Typeshed is encouraged where permitted.

### Other Static Type Checkers

Alternatives include PyCharm's built-in checker, Facebook's Pyre, and Google's pytype (which can also add annotations automatically). Type hints may also be used at runtime via `__annotations__`, with packages like Enforce, Pydantic, or Pytypes, or for compilation via Cython and Mypyc.

## Conclusion

Type hinting in Python is useful but optional. It does not change what code can do; it makes reasoning about code, finding bugs, and maintaining architecture easier. Gradual typing makes Python type checking more flexible than in many languages. Key points: annotations and type comments both add hints; many composite and special types are supported; static checkers such as mypy perform the actual checking.

## See Also

- [Growing Code: Python Fundamentals Through Garden Data](growing-code.md)
