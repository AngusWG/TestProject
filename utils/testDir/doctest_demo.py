# wss3.py
def start_by_thread(func):
    def __decorator(*arg):
        func(arg)

    return __decorator


def plist(tes):
    """
    >>> plist(6)
    18
    >>> plist(8)
    24
    """
    return tes * 3


if __name__ == '__main__':
    plist(2)
    import doctest,wss3

    doctest.testmod(wss3)
