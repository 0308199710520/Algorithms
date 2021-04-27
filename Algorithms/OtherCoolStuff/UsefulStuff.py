import time


def timer(func):
    """
    DECORATOR: Gets the timing for a function, returns the time it took to run it
    :param func:
    :return:
    """

    def inner(*args):
        a = time.time()
        retur = func(*args)
        b = time.time()
        print(f"{func.__name__} took {b - a} seconds")
        return retur

    return inner


def multiple_times_runner(*args, repeats=1):
    def inner(func):
        results_list = []
        for _ in range(repeats):
            results_list.append(func(*args))

        return results_list

    return inner


