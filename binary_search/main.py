from typing import List


def search(arr: List[int], target: int) -> int:
    """
    Search a target inside of a given array by binary search algorithmn, using
    left and right distances to calculate middle position.
    :param arr List[int]: Array to search target value
    :param target int: Value to be searched
    :returns int: target position if found, -1 otherwise
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        if target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


if __name__ == "__main__":
    arr_1 = [1, 4, 6, 8, 11, 15, 22, 55, 67, 89]
    assert search(arr_1, 8) == 3
    assert search(arr_1, 15) == 5
    assert search(arr_1, 55) == 7
    assert search(arr_1, 89) == 9
    assert search(arr_1, 4) == 1
    assert search(arr_1, 1) == 0
    assert search(arr_1, 8) == 3

    arr_2 = [4]
    assert search(arr_2, 2) == -1
    assert search(arr_2, 3) == -1
    assert search(arr_2, 4) == 0

    print("Successfully find your tests targets!")
