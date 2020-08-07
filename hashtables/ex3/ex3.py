from collections import Counter


def intersection(arrays):

    count = 0
    lst = []
    for i in arrays:
        if isinstance(i, list):
            ar1 = Counter(i)
            count += 1
            lst.append(ar1)

    arr = Counter()

    result = []
    for i in lst:
        arr += i

    for (key, value) in arr.items():
        if value == count:
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
