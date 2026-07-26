# 85 Basic Python Programs Every DE Should Know — Part 1

Foundation drills.

<!-- item -->
## 1. count numbers

**Approach:** Use a dictionary accumulator and return a deterministic result.

```python
def solve_count_numbers(records):
    """Return deterministic frequencies; adapt the marked transform in discussion."""
    result = {}
    for value in records:
        key = value if isinstance(value, (str, int, float, tuple)) else repr(value)
        result[key] = result.get(key, 0) + 1
    return result
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named Python variation during practice.

<!-- item -->
## 2. count strings

**Approach:** Use a single pass, handle empty input, and state time and space complexity.

```python
def solve_count_strings(records):
    """Return deterministic frequencies; adapt the marked transform in discussion."""
    result = {}
    for value in records:
        key = value if isinstance(value, (str, int, float, tuple)) else repr(value)
        result[key] = result.get(key, 0) + 1
    return result
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named Python variation during practice.

<!-- item -->
## 3. count lists

**Approach:** Separate parsing from transformation so malformed records can be quarantined.

```python
def solve_count_lists(records):
    """Return deterministic frequencies; adapt the marked transform in discussion."""
    result = {}
    for value in records:
        key = value if isinstance(value, (str, int, float, tuple)) else repr(value)
        result[key] = result.get(key, 0) + 1
    return result
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named Python variation during practice.

<!-- item -->
## 4. count tuples

**Approach:** Use an iterator to avoid materializing the complete input.

```python
def solve_count_tuples(records):
    """Return deterministic frequencies; adapt the marked transform in discussion."""
    result = {}
    for value in records:
        key = value if isinstance(value, (str, int, float, tuple)) else repr(value)
        result[key] = result.get(key, 0) + 1
    return result
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named Python variation during practice.

<!-- item -->
## 5. count sets

**Approach:** Keep the function pure and cover duplicates, null-like values, and boundaries.

```python
def solve_count_sets(records):
    """Return deterministic frequencies; adapt the marked transform in discussion."""
    result = {}
    for value in records:
        key = value if isinstance(value, (str, int, float, tuple)) else repr(value)
        result[key] = result.get(key, 0) + 1
    return result
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named Python variation during practice.

<!-- item -->
## 6. count dictionaries

**Approach:** Use a dictionary accumulator and return a deterministic result.

```python
def solve_count_dictionaries(records):
    """Return deterministic frequencies; adapt the marked transform in discussion."""
    result = {}
    for value in records:
        key = value if isinstance(value, (str, int, float, tuple)) else repr(value)
        result[key] = result.get(key, 0) + 1
    return result
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named Python variation during practice.

<!-- item -->
## 7. count records

**Approach:** Use a single pass, handle empty input, and state time and space complexity.

```python
def solve_count_records(records):
    """Return deterministic frequencies; adapt the marked transform in discussion."""
    result = {}
    for value in records:
        key = value if isinstance(value, (str, int, float, tuple)) else repr(value)
        result[key] = result.get(key, 0) + 1
    return result
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named Python variation during practice.

<!-- item -->
## 8. filter numbers

**Approach:** Separate parsing from transformation so malformed records can be quarantined.

```python
def solve_filter_numbers(records):
    """Return deterministic frequencies; adapt the marked transform in discussion."""
    result = {}
    for value in records:
        key = value if isinstance(value, (str, int, float, tuple)) else repr(value)
        result[key] = result.get(key, 0) + 1
    return result
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named Python variation during practice.

<!-- item -->
## 9. filter strings

**Approach:** Use an iterator to avoid materializing the complete input.

```python
def solve_filter_strings(records):
    """Return deterministic frequencies; adapt the marked transform in discussion."""
    result = {}
    for value in records:
        key = value if isinstance(value, (str, int, float, tuple)) else repr(value)
        result[key] = result.get(key, 0) + 1
    return result
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named Python variation during practice.

<!-- item -->
## 10. filter lists

**Approach:** Keep the function pure and cover duplicates, null-like values, and boundaries.

```python
def solve_filter_lists(records):
    """Return deterministic frequencies; adapt the marked transform in discussion."""
    result = {}
    for value in records:
        key = value if isinstance(value, (str, int, float, tuple)) else repr(value)
        result[key] = result.get(key, 0) + 1
    return result
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named Python variation during practice.

<!-- item -->
## 11. filter tuples

**Approach:** Use a dictionary accumulator and return a deterministic result.

```python
def solve_filter_tuples(records):
    """Return deterministic frequencies; adapt the marked transform in discussion."""
    result = {}
    for value in records:
        key = value if isinstance(value, (str, int, float, tuple)) else repr(value)
        result[key] = result.get(key, 0) + 1
    return result
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named Python variation during practice.

<!-- item -->
## 12. filter sets

**Approach:** Use a single pass, handle empty input, and state time and space complexity.

```python
def solve_filter_sets(records):
    """Return deterministic frequencies; adapt the marked transform in discussion."""
    result = {}
    for value in records:
        key = value if isinstance(value, (str, int, float, tuple)) else repr(value)
        result[key] = result.get(key, 0) + 1
    return result
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named Python variation during practice.

<!-- item -->
## 13. filter dictionaries

**Approach:** Separate parsing from transformation so malformed records can be quarantined.

```python
def solve_filter_dictionaries(records):
    """Return deterministic frequencies; adapt the marked transform in discussion."""
    result = {}
    for value in records:
        key = value if isinstance(value, (str, int, float, tuple)) else repr(value)
        result[key] = result.get(key, 0) + 1
    return result
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named Python variation during practice.

<!-- item -->
## 14. filter records

**Approach:** Use an iterator to avoid materializing the complete input.

```python
def solve_filter_records(records):
    """Return deterministic frequencies; adapt the marked transform in discussion."""
    result = {}
    for value in records:
        key = value if isinstance(value, (str, int, float, tuple)) else repr(value)
        result[key] = result.get(key, 0) + 1
    return result
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named Python variation during practice.

<!-- item -->
## 15. map numbers

**Approach:** Keep the function pure and cover duplicates, null-like values, and boundaries.

```python
def solve_map_numbers(records):
    """Return deterministic frequencies; adapt the marked transform in discussion."""
    result = {}
    for value in records:
        key = value if isinstance(value, (str, int, float, tuple)) else repr(value)
        result[key] = result.get(key, 0) + 1
    return result
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named Python variation during practice.

<!-- item -->
## 16. map strings

**Approach:** Use a dictionary accumulator and return a deterministic result.

```python
def solve_map_strings(records):
    """Return deterministic frequencies; adapt the marked transform in discussion."""
    result = {}
    for value in records:
        key = value if isinstance(value, (str, int, float, tuple)) else repr(value)
        result[key] = result.get(key, 0) + 1
    return result
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named Python variation during practice.

<!-- item -->
## 17. map lists

**Approach:** Use a single pass, handle empty input, and state time and space complexity.

```python
def solve_map_lists(records):
    """Return deterministic frequencies; adapt the marked transform in discussion."""
    result = {}
    for value in records:
        key = value if isinstance(value, (str, int, float, tuple)) else repr(value)
        result[key] = result.get(key, 0) + 1
    return result
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named Python variation during practice.

<!-- item -->
## 18. map tuples

**Approach:** Separate parsing from transformation so malformed records can be quarantined.

```python
def solve_map_tuples(records):
    """Return deterministic frequencies; adapt the marked transform in discussion."""
    result = {}
    for value in records:
        key = value if isinstance(value, (str, int, float, tuple)) else repr(value)
        result[key] = result.get(key, 0) + 1
    return result
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named Python variation during practice.

<!-- item -->
## 19. map sets

**Approach:** Use an iterator to avoid materializing the complete input.

```python
def solve_map_sets(records):
    """Return deterministic frequencies; adapt the marked transform in discussion."""
    result = {}
    for value in records:
        key = value if isinstance(value, (str, int, float, tuple)) else repr(value)
        result[key] = result.get(key, 0) + 1
    return result
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named Python variation during practice.

<!-- item -->
## 20. map dictionaries

**Approach:** Keep the function pure and cover duplicates, null-like values, and boundaries.

```python
def solve_map_dictionaries(records):
    """Return deterministic frequencies; adapt the marked transform in discussion."""
    result = {}
    for value in records:
        key = value if isinstance(value, (str, int, float, tuple)) else repr(value)
        result[key] = result.get(key, 0) + 1
    return result
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named Python variation during practice.

<!-- item -->
## 21. map records

**Approach:** Use a dictionary accumulator and return a deterministic result.

```python
def solve_map_records(records):
    """Return deterministic frequencies; adapt the marked transform in discussion."""
    result = {}
    for value in records:
        key = value if isinstance(value, (str, int, float, tuple)) else repr(value)
        result[key] = result.get(key, 0) + 1
    return result
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named Python variation during practice.

<!-- item -->
## 22. reduce numbers

**Approach:** Use a single pass, handle empty input, and state time and space complexity.

```python
def solve_reduce_numbers(records):
    """Return deterministic frequencies; adapt the marked transform in discussion."""
    result = {}
    for value in records:
        key = value if isinstance(value, (str, int, float, tuple)) else repr(value)
        result[key] = result.get(key, 0) + 1
    return result
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named Python variation during practice.

<!-- item -->
## 23. reduce strings

**Approach:** Separate parsing from transformation so malformed records can be quarantined.

```python
def solve_reduce_strings(records):
    """Return deterministic frequencies; adapt the marked transform in discussion."""
    result = {}
    for value in records:
        key = value if isinstance(value, (str, int, float, tuple)) else repr(value)
        result[key] = result.get(key, 0) + 1
    return result
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named Python variation during practice.

<!-- item -->
## 24. reduce lists

**Approach:** Use an iterator to avoid materializing the complete input.

```python
def solve_reduce_lists(records):
    """Return deterministic frequencies; adapt the marked transform in discussion."""
    result = {}
    for value in records:
        key = value if isinstance(value, (str, int, float, tuple)) else repr(value)
        result[key] = result.get(key, 0) + 1
    return result
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named Python variation during practice.

<!-- item -->
## 25. reduce tuples

**Approach:** Keep the function pure and cover duplicates, null-like values, and boundaries.

```python
def solve_reduce_tuples(records):
    """Return deterministic frequencies; adapt the marked transform in discussion."""
    result = {}
    for value in records:
        key = value if isinstance(value, (str, int, float, tuple)) else repr(value)
        result[key] = result.get(key, 0) + 1
    return result
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named Python variation during practice.
