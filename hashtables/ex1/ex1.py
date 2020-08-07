
def get_indices_of_item_weights(weights, length, limit):
    # set up empty cache
    cache = {}

    # iterate over length of weights array
    for index in range(length):

        # calculate needed value by subtracting the value at index
        needed = limit - weights[index]

        # check the cache
        if needed in cache:
            # if the needed value is in the cache
            subtract = cache[needed]
            # create a new array from the results
            new_list = [index, subtract]
            # sort the list so that the greatest number is at position 0
            new_list.sort(reverse = True)
            # return the list
            return new_list
        else:
            # if the value is not present in the cache
            cache[weights[index]] = index

    # there are no possibilities return None
    return None