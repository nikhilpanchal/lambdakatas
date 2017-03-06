def sum_iterative(f, a, b):
    if a >= b:
        return 0

    return f(a) + sum_iterative(f, (a+1), b)


def sum_tail_recursive(f, a, b):
    def loop(accumulator, a):
        if a >= b:
            return accumulator

        return loop(f(a) + accumulator, (a+1))

    return loop(0, a)


if __name__ == '__main__':
    print(sum_tail_recursive(lambda x: x*2,  1, 50000))
    print(sum_iterative(lambda x: x*2,  1, 50000))
