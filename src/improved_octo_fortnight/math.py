"""Basic math operations."""


def add(a, b):
    """Add two numbers.

    Parameters
    ----------
    a : int or float
        The first number.
    b : int or float
        The second number.

    Returns
    -------
    int or float
        The sum of `a` and `b`.

    Raises
    ------
    TypeError
        If `a` or `b` is not a number.

    Examples
    --------
    >>> add(1, 2)
    3
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers.")
    return a + b


def fibonacci(n):
    """Generate the Fibonacci sequence.

    Parameters
    ----------
    n : int
        The number of terms to generate. Must be non-negative.

    Returns
    -------
    list of int
        The first `n` terms of the Fibonacci sequence.

    Raises
    ------
    ValueError
        If `n` is negative.

    Examples
    --------
    >>> fibonacci(6)
    [0, 1, 1, 2, 3, 5]
    """
    if n < 0:
        raise ValueError("n must be non-negative.")
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq
