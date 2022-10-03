def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    An iterable.
    None if the iterable can not be used by the function.
    """
    if callable(function_to_apply) is False :
        raise TypeError("The function is not callable")
        return None

    if hasattr(iterable, '__iter__') :
        ret = iterable.copy()
        for el in ret :
            yield function_to_apply(el)
        return ret
    else :
        raise TypeError("The data is not iterable")


if __name__ == '__main__':

    chars = "aBcDeFghiJk"
    print(ft_map(str.upper, chars))
    print(list(map(str.upper, chars)))
    print(ft_map(lambda n: 2 * n, range(5)))
    print(list(map(lambda n: n * n, range(5))))

    print(list(ft_map(lambda x: x + 2, [])))
    print(list(ft_map(lambda x: x + 2, [1])))
    print(list(ft_map(lambda x: x ** 2, [1, 2, 3, 4, 5])))
    