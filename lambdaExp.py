def filtered(numList, divisor):
    """
    Prints the elements of numList that are multiples of the given divisor.

    Args:
        numList (list): A list of numbers.
        divisor (int or function): The divisor used for filtering.
    """
    if isinstance(divisor, int):
        div_is_num = list(filter(lambda x: x % int(divisor) == 0, numList))
        print(*(int(i) for i in div_is_num), sep=", ", end="")
    else:
        div_is_lam = list(filter(divisor, numList))
        print(*(int(i) for i in div_is_lam), sep=", ")

nList = [i for i in range(101)]

filtered(nList, 11)
