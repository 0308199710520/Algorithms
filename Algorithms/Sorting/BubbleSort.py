from Algorithms.OtherCoolStuff.UsefulStuff import timer


def bubblesort(arr: list) -> list:
    """

    :param arr:
    :return:
    """
    # Iterates over the entire dataset
    for i in range(len(arr) - 1):

        # iterates over the dataset -1 per cycle, "locking in" the last position
        for j in range(len(arr) - 1 - i):

            # Compare and swap
            if arr[j] >= arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr




