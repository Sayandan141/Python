from __future__ import annotations
from typing import Callable, TypeVar, Any
from functools import cmp_to_key

T = TypeVar('T')

def merge(left_half: list[T], right_half: list[T], key: Callable[[T, T], int] | None = None) -> list[T]:
    """Merges two sorted lists into a single sorted list.

    Args:
        left_half: A sorted list of comparable elements.
        right_half: A sorted list of comparable elements.
        key: Optional comparison function. If provided, it should return -1, 0, or 1
             for less than, equal to, or greater than comparisons, respectively.

    Returns:
        A sorted list containing all elements from both input lists.

    Raises:
        TypeError: If elements are not comparable or if key function is invalid.

    Examples:
        >>> merge([-2], [-1])
        [-2, -1]
        >>> merge([1, 2, 3], [4, 5, 6])
        [1, 2, 3, 4, 5, 6]
        >>> merge([12, 15], [13, 14])
        [12, 13, 14, 15]
        >>> merge([], [])
        []
        >>> merge([3, 1], [2], lambda x, y: -1 if x > y else 1 if x < y else 0)  # Descending order
        [3, 2, 1]
    """
    result = []
    left_idx, right_idx = 0, 0

    # Use custom comparator if provided, otherwise use default comparison
    compare = (lambda x, y: key(x, y)) if key else (lambda x, y: -1 if x < y else 1 if x > y else 0)

    # Merge the two sorted lists
    while left_idx < len(left_half) and right_idx < len(right_half):
        if compare(left_half[left_idx], right_half[right_idx]) <= 0:
            result.append(left_half[left_idx])
            left_idx += 1
        else:
            result.append(right_half[right_idx])
            right_idx += 1

    # Append remaining elements from left_half, if any
    result.extend(left_half[left_idx:])
    # Append remaining elements from right_half, if any
    result.extend(right_half[right_idx:])

    return result

def merge_sort(array: list[T], key: Callable[[T, T], int] | None = None) -> list[T]:
    """Sorts a list using the merge sort algorithm.

    Args:
        array: List of comparable elements to be sorted.
        key: Optional comparison function. If provided, it should return -1, 0, or 1
             for less than, equal to, or greater than comparisons, respectively.

    Returns:
        A new sorted list containing all elements from the input list.

    Raises:
        TypeError: If elements are not comparable or if key function is invalid.

    Time Complexity:
        O(n log n) for both average and worst cases.
    Space Complexity:
        O(n) for the auxiliary space used during merging.

    Examples:
        >>> from random import shuffle
        >>> array = [-2, 3, -10, 11, 99, 100000, 100, -200]
        >>> shuffle(array)
        >>> merge_sort(array)
        [-200, -10, -2, 3, 11, 99, 100, 100000]
        >>> merge_sort([-200])
        [-200]
        >>> merge_sort([])
        []
        >>> merge_sort([1, 1, 1, 1])
        [1, 1, 1, 1]
        >>> merge_sort([3, 1, 4], lambda x, y: -1 if x > y else 1 if x < y else 0)  # Descending
        [4, 3, 1]
    """
    # Base case: return if list has 1 or fewer elements
    if len(array) <= 1:
        return array.copy()  # Return a copy to avoid modifying the input

    # Validate input types if no key function is provided
    if not key and len(array) > 1:
        try:
            array[0] < array[0]  # Test comparability
        except TypeError as e:
            raise TypeError("Elements must be comparable") from e

    # Calculate middle index to split the array
    middle = len(array) // 2

    # Recursively sort left and right halves
    left_half = merge_sort(array[:middle], key)
    right_half = merge_sort(array[middle:], key)

    # Merge the sorted halves
    return merge(left_half, right_half, key)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
