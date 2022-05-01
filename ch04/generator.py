def range(*args):
    if len(args) == 1:
        start = 0
        stop = args[0]
    else:
        start = args[0]
        stop = args[1]

    current = start

    while current < stop:
        yield current
        current += 1


def squares(items: list[int]):
    for item in items:
        yield item ** 2


[i for i in squares([1, 2, 3, 4, 5])]
