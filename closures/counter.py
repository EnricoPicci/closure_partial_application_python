def counter():
    x = 0

    def increment():
        nonlocal x
        x += 1
        return x

    return increment


if __name__ == "__main__":
    counter_1 = counter()
    print(counter_1())  # 1
    print(counter_1())  # 2
    print(counter_1())  # 3

    counter_2 = counter()
    print(counter_2())  # 1

# python closures/counter.py
