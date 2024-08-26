# these are global variables
global_1 = 1


def outer_outer_func():
    # this is a variable defined in the outermost function
    outer_outer_1 = 10
    outer_1 = 10
    print(
        f"Values at the beginning of outer_outer_func: {global_1}, {outer_outer_1}, {outer_1}"
    )

    def outer_func():
        # this is a variable defined in the second outermost function
        outer_1 = 100
        print(
            f"Values at the beginning of outer_func: {global_1}, {outer_outer_1}, {outer_1}"
        )

        def inner_function():
            # this is a variable defined in the innermost function
            inner_1 = 1000

            # here we define that we want to use the global and nonlocal variables before using them
            # the declaration of variables in this inner function scope using global and nonlocal
            # must be done before using them in any way, even before reading them, not only before assigning them
            # a new value
            global global_1
            nonlocal outer_outer_1, outer_1

            print(
                f"Values at the beginning of inner_function: {global_1}, {outer_outer_1}, {outer_1}, {inner_1}"
            )

            global_1 = global_1 * 10
            outer_outer_1 = outer_outer_1 * 10
            outer_1 = outer_1 * 10
            inner_1 = inner_1 * 10

            print(
                f"Values at the end of inner_function: {global_1}, {outer_outer_1}, {outer_1}, {inner_1}"
            )

        inner_function()

    outer_func()


if __name__ == "__main__":
    outer_outer_func()

# python -m scope_of_variables.scope_of_variables
