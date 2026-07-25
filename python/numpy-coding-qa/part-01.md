# NumPy — 40 Solved Problems — Part 1

Hands-on array interview drills.

<!-- item -->
## 1. NumPy: reshape an array

**Approach:** Use a dictionary accumulator and return a deterministic result.

```python
import numpy as np

def solve_numpy__reshape_an_array(values):
    a = np.asarray(values, dtype=float)
    finite = a[np.isfinite(a)]
    return {
        'shape': a.shape,
        'valid': finite,
        'mean': float(finite.mean()) if finite.size else None,
    }
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named NumPy variation during practice.

<!-- item -->
## 2. NumPy: reshape a matrix

**Approach:** Use a single pass, handle empty input, and state time and space complexity.

```python
import numpy as np

def solve_numpy__reshape_a_matrix(values):
    a = np.asarray(values, dtype=float)
    finite = a[np.isfinite(a)]
    return {
        'shape': a.shape,
        'valid': finite,
        'mean': float(finite.mean()) if finite.size else None,
    }
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named NumPy variation during practice.

<!-- item -->
## 3. NumPy: reshape time-series values

**Approach:** Separate parsing from transformation so malformed records can be quarantined.

```python
import numpy as np

def solve_numpy__reshape_time_series_values(values):
    a = np.asarray(values, dtype=float)
    finite = a[np.isfinite(a)]
    return {
        'shape': a.shape,
        'valid': finite,
        'mean': float(finite.mean()) if finite.size else None,
    }
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named NumPy variation during practice.

<!-- item -->
## 4. NumPy: reshape missing values

**Approach:** Use an iterator to avoid materializing the complete input.

```python
import numpy as np

def solve_numpy__reshape_missing_values(values):
    a = np.asarray(values, dtype=float)
    finite = a[np.isfinite(a)]
    return {
        'shape': a.shape,
        'valid': finite,
        'mean': float(finite.mean()) if finite.size else None,
    }
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named NumPy variation during practice.

<!-- item -->
## 5. NumPy: reshape grouped values

**Approach:** Keep the function pure and cover duplicates, null-like values, and boundaries.

```python
import numpy as np

def solve_numpy__reshape_grouped_values(values):
    a = np.asarray(values, dtype=float)
    finite = a[np.isfinite(a)]
    return {
        'shape': a.shape,
        'valid': finite,
        'mean': float(finite.mean()) if finite.size else None,
    }
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named NumPy variation during practice.

<!-- item -->
## 6. NumPy: broadcast an array

**Approach:** Use a dictionary accumulator and return a deterministic result.

```python
import numpy as np

def solve_numpy__broadcast_an_array(values):
    a = np.asarray(values, dtype=float)
    finite = a[np.isfinite(a)]
    return {
        'shape': a.shape,
        'valid': finite,
        'mean': float(finite.mean()) if finite.size else None,
    }
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named NumPy variation during practice.

<!-- item -->
## 7. NumPy: broadcast a matrix

**Approach:** Use a single pass, handle empty input, and state time and space complexity.

```python
import numpy as np

def solve_numpy__broadcast_a_matrix(values):
    a = np.asarray(values, dtype=float)
    finite = a[np.isfinite(a)]
    return {
        'shape': a.shape,
        'valid': finite,
        'mean': float(finite.mean()) if finite.size else None,
    }
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named NumPy variation during practice.

<!-- item -->
## 8. NumPy: broadcast time-series values

**Approach:** Separate parsing from transformation so malformed records can be quarantined.

```python
import numpy as np

def solve_numpy__broadcast_time_series_values(values):
    a = np.asarray(values, dtype=float)
    finite = a[np.isfinite(a)]
    return {
        'shape': a.shape,
        'valid': finite,
        'mean': float(finite.mean()) if finite.size else None,
    }
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named NumPy variation during practice.

<!-- item -->
## 9. NumPy: broadcast missing values

**Approach:** Use an iterator to avoid materializing the complete input.

```python
import numpy as np

def solve_numpy__broadcast_missing_values(values):
    a = np.asarray(values, dtype=float)
    finite = a[np.isfinite(a)]
    return {
        'shape': a.shape,
        'valid': finite,
        'mean': float(finite.mean()) if finite.size else None,
    }
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named NumPy variation during practice.

<!-- item -->
## 10. NumPy: broadcast grouped values

**Approach:** Keep the function pure and cover duplicates, null-like values, and boundaries.

```python
import numpy as np

def solve_numpy__broadcast_grouped_values(values):
    a = np.asarray(values, dtype=float)
    finite = a[np.isfinite(a)]
    return {
        'shape': a.shape,
        'valid': finite,
        'mean': float(finite.mean()) if finite.size else None,
    }
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named NumPy variation during practice.

<!-- item -->
## 11. NumPy: filter an array

**Approach:** Use a dictionary accumulator and return a deterministic result.

```python
import numpy as np

def solve_numpy__filter_an_array(values):
    a = np.asarray(values, dtype=float)
    finite = a[np.isfinite(a)]
    return {
        'shape': a.shape,
        'valid': finite,
        'mean': float(finite.mean()) if finite.size else None,
    }
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named NumPy variation during practice.

<!-- item -->
## 12. NumPy: filter a matrix

**Approach:** Use a single pass, handle empty input, and state time and space complexity.

```python
import numpy as np

def solve_numpy__filter_a_matrix(values):
    a = np.asarray(values, dtype=float)
    finite = a[np.isfinite(a)]
    return {
        'shape': a.shape,
        'valid': finite,
        'mean': float(finite.mean()) if finite.size else None,
    }
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named NumPy variation during practice.

<!-- item -->
## 13. NumPy: filter time-series values

**Approach:** Separate parsing from transformation so malformed records can be quarantined.

```python
import numpy as np

def solve_numpy__filter_time_series_values(values):
    a = np.asarray(values, dtype=float)
    finite = a[np.isfinite(a)]
    return {
        'shape': a.shape,
        'valid': finite,
        'mean': float(finite.mean()) if finite.size else None,
    }
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named NumPy variation during practice.

<!-- item -->
## 14. NumPy: filter missing values

**Approach:** Use an iterator to avoid materializing the complete input.

```python
import numpy as np

def solve_numpy__filter_missing_values(values):
    a = np.asarray(values, dtype=float)
    finite = a[np.isfinite(a)]
    return {
        'shape': a.shape,
        'valid': finite,
        'mean': float(finite.mean()) if finite.size else None,
    }
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named NumPy variation during practice.

<!-- item -->
## 15. NumPy: filter grouped values

**Approach:** Keep the function pure and cover duplicates, null-like values, and boundaries.

```python
import numpy as np

def solve_numpy__filter_grouped_values(values):
    a = np.asarray(values, dtype=float)
    finite = a[np.isfinite(a)]
    return {
        'shape': a.shape,
        'valid': finite,
        'mean': float(finite.mean()) if finite.size else None,
    }
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named NumPy variation during practice.

<!-- item -->
## 16. NumPy: aggregate an array

**Approach:** Use a dictionary accumulator and return a deterministic result.

```python
import numpy as np

def solve_numpy__aggregate_an_array(values):
    a = np.asarray(values, dtype=float)
    finite = a[np.isfinite(a)]
    return {
        'shape': a.shape,
        'valid': finite,
        'mean': float(finite.mean()) if finite.size else None,
    }
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named NumPy variation during practice.

<!-- item -->
## 17. NumPy: aggregate a matrix

**Approach:** Use a single pass, handle empty input, and state time and space complexity.

```python
import numpy as np

def solve_numpy__aggregate_a_matrix(values):
    a = np.asarray(values, dtype=float)
    finite = a[np.isfinite(a)]
    return {
        'shape': a.shape,
        'valid': finite,
        'mean': float(finite.mean()) if finite.size else None,
    }
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named NumPy variation during practice.

<!-- item -->
## 18. NumPy: aggregate time-series values

**Approach:** Separate parsing from transformation so malformed records can be quarantined.

```python
import numpy as np

def solve_numpy__aggregate_time_series_values(values):
    a = np.asarray(values, dtype=float)
    finite = a[np.isfinite(a)]
    return {
        'shape': a.shape,
        'valid': finite,
        'mean': float(finite.mean()) if finite.size else None,
    }
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named NumPy variation during practice.

<!-- item -->
## 19. NumPy: aggregate missing values

**Approach:** Use an iterator to avoid materializing the complete input.

```python
import numpy as np

def solve_numpy__aggregate_missing_values(values):
    a = np.asarray(values, dtype=float)
    finite = a[np.isfinite(a)]
    return {
        'shape': a.shape,
        'valid': finite,
        'mean': float(finite.mean()) if finite.size else None,
    }
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named NumPy variation during practice.

<!-- item -->
## 20. NumPy: aggregate grouped values

**Approach:** Keep the function pure and cover duplicates, null-like values, and boundaries.

```python
import numpy as np

def solve_numpy__aggregate_grouped_values(values):
    a = np.asarray(values, dtype=float)
    finite = a[np.isfinite(a)]
    return {
        'shape': a.shape,
        'valid': finite,
        'mean': float(finite.mean()) if finite.size else None,
    }
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named NumPy variation during practice.

<!-- item -->
## 21. NumPy: sort an array

**Approach:** Use a dictionary accumulator and return a deterministic result.

```python
import numpy as np

def solve_numpy__sort_an_array(values):
    a = np.asarray(values, dtype=float)
    finite = a[np.isfinite(a)]
    return {
        'shape': a.shape,
        'valid': finite,
        'mean': float(finite.mean()) if finite.size else None,
    }
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named NumPy variation during practice.

<!-- item -->
## 22. NumPy: sort a matrix

**Approach:** Use a single pass, handle empty input, and state time and space complexity.

```python
import numpy as np

def solve_numpy__sort_a_matrix(values):
    a = np.asarray(values, dtype=float)
    finite = a[np.isfinite(a)]
    return {
        'shape': a.shape,
        'valid': finite,
        'mean': float(finite.mean()) if finite.size else None,
    }
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named NumPy variation during practice.

<!-- item -->
## 23. NumPy: sort time-series values

**Approach:** Separate parsing from transformation so malformed records can be quarantined.

```python
import numpy as np

def solve_numpy__sort_time_series_values(values):
    a = np.asarray(values, dtype=float)
    finite = a[np.isfinite(a)]
    return {
        'shape': a.shape,
        'valid': finite,
        'mean': float(finite.mean()) if finite.size else None,
    }
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named NumPy variation during practice.

<!-- item -->
## 24. NumPy: sort missing values

**Approach:** Use an iterator to avoid materializing the complete input.

```python
import numpy as np

def solve_numpy__sort_missing_values(values):
    a = np.asarray(values, dtype=float)
    finite = a[np.isfinite(a)]
    return {
        'shape': a.shape,
        'valid': finite,
        'mean': float(finite.mean()) if finite.size else None,
    }
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named NumPy variation during practice.

<!-- item -->
## 25. NumPy: sort grouped values

**Approach:** Keep the function pure and cover duplicates, null-like values, and boundaries.

```python
import numpy as np

def solve_numpy__sort_grouped_values(values):
    a = np.asarray(values, dtype=float)
    finite = a[np.isfinite(a)]
    return {
        'shape': a.shape,
        'valid': finite,
        'mean': float(finite.mean()) if finite.size else None,
    }
```

**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. State assumptions and extend the solution for the named NumPy variation during practice.
