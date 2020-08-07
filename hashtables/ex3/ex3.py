from collections import Counter


def intersection(arrays):

    count = 0
    lst = []
    # get the inner array from the 2D array passed in
    for i in arrays:
        if isinstance(i, list):
              # if i in ar1 increment
            ar1 = Counter(i)
            count += 1
            lst.append(ar1)

    arr = Counter()

    result = []
    for i in lst:
        arr += i

#for each item
#if equals count in arrays
#append results to array
    for (key, value) in arr.items():
        if value == count:
            result.append(key)

    # if we get here, the array is set,
    # return it
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
