# Python 3.10

> Sources: Python Documentation, 2021-10-04
> Raw: [What's New In Python 3.10](../../raw/python-fundamentals/python-3.10-whats-new.md)
> Updated: 2026-10-28

## Overview

Python 3.10 was released on October 4, 2021, compared to 3.9. It introduces structural pattern matching, parenthesized context managers, significantly improved error messages, precise line numbers for debugging, optional encoding warnings, and several new type hint features (PEP 604, 612, 613, 647).

## Structural Pattern Matching

PEP 634/635/636 added structural pattern matching via the `match` statement and `case` statements. A match statement takes a subject expression and compares it to successive patterns from top to bottom, executing the action of the first matching case. Patterns include literals, sequences, mappings, class instances, and a wildcard `_`.

Key capabilities: matching a subject to a literal (with `|` to combine literals), unpacking patterns that bind variables (e.g., `(0, y)`), class patterns capturing attributes, nested patterns, guards with `if`, sequence patterns with wildcards (`*rest`), mapping patterns (extra keys ignored), `as` keyword for subpattern capture, and named constants (must be dotted names). Sequence patterns do not match strings or iterators. If no case matches and no wildcard exists, the match is a no-op.

## Parenthesized Context Managers

Enclosing parentheses for continuation across multiple lines in context managers is now officially supported, similar to import statements. A trailing comma is allowed at the end of the enclosed group. This uses the non-LL(1) capacities of the new parser (PEP 617).

## Better Error Messages

Python 3.10 provides more informative errors:
- SyntaxErrors now highlight the full error range and point to unclosed brackets/strings; many new specialized messages (missing colon before blocks, unparenthesized comprehension targets, missing commas, multiple exception types without parentheses, dictionary key errors, try blocks without except/finally, `=` instead of `==` in comparisons, starred expressions in f-strings).
- IndentationErrors include context about which block expected indentation.
- AttributeErrors and NameErrors offer suggestions of similar names (for example, suggesting `namedtuple` when `namedtoplo` is typed).

## PEP 626: Precise Line Numbers

More precise and reliable line numbers for debugging, profiling, and coverage tools. Tracing events are generated for all executed lines and only executed lines. `frame.f_lineno` always contains the expected line number. `codeobject.co_lnotab` is deprecated (removed in 3.12); use `co_lines()` instead.

## Optional EncodingWarning

An optional `EncodingWarning` is emitted when a locale-specific default encoding is used (instead of UTF-8), helping detect a common bug when opening text files without specifying encoding. Enabled via `-X warn_default_encoding` or `PYTHONWARNDEFAULTENCODING`.

## New Features Related to Type Hints

Python 3.10 added several type hint improvements:
- **PEP 604**: New union type operator `X | Y` as a cleaner alternative to `typing.Union`, also accepted by `isinstance()` and `issubclass()`.
- **PEP 612**: Parameter specification variables (`ParamSpec`) and `Concatenate` operator to forward parameter types in higher-order functions and decorators.
- **PEP 613**: Explicit `TypeAlias` annotation to distinguish type aliases from ordinary assignments.
- **PEP 647**: `TypeGuard` for user-defined type guards to improve type narrowing in static checkers.

## Other Language Changes

Notable additions: `int.bit_count()` (population count); `dict.keys/values/items` views gained a `.mapping` attribute; `zip()` gained an optional `strict` flag; builtin/extension functions no longer accept `Decimal`/`Fraction` etc. without `__index__`; `aiter()` and `anext()` async builtins; `@staticmethod`/`@classmethod` now inherit attributes and are callable as regular functions; lazy-created empty annotation dicts; `SyntaxError` now has `end_lineno` and `end_offset`.

## New Modules

None added in 3.10.

## Improved Modules

Highlights: `dataclasses` gained `slots` parameter and keyword-only fields (via `kw_only=True` or `KW_ONLY` marker); `enum` gained `StrEnum` and changed `__repr__`/`__str__`; `contextlib` gained `aclosing()` and async `nullcontext()`; `argparse` help wording changed from "optional arguments" to "options"; `bisect` gained a key function; `zipimport`, `pathlib`, `asyncio`, `inspect`, `traceback`, `typing`, `unittest`, and many others received improvements. `distutils` is deprecated (removed in 3.12); `asynchat`, `asyncore`, `smtpd` now emit `DeprecationWarning`.

## Deprecations and Removals

- `distutils` deprecated, to be removed in 3.12.
- `co_lnotab` deprecated.
- `bdist_wininst` command removed.
- Several C API changes (PEP 652 stable ABI maintenance).

## See Also

- [Python Type Checking](python-type-checking.md)
- [Growing Code: Python Fundamentals Through Garden Data](growing-code.md)
