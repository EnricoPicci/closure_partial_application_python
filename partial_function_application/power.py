def power(x: int, y: int):
    return x**y


def power_partial(y: int):
    def inner(x: int):
        return power(x, y)

    return inner


def power_partial_lambda(x: int):
    return lambda y: power(x, y)


if __name__ == "__main__":
    print(power(1, 3))
    print(power(2, 3))
    print(power(3, 3))
    print(power(1, 5))
    print(power(2, 5))
    print(power(3, 5))

    power_partial_application = power_partial(3)
    print(power_partial_application(1))
    print(power_partial_application(2))
    print(power_partial_application(3))
    power_partial_application = power_partial(5)
    print(power_partial_application(1))
    print(power_partial_application(2))
    print(power_partial_application(3))


# python -m partial_function_application.power
