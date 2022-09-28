def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    """

    if not callable(function_to_apply)  :
        raise TypeError("The function is not callable")


    if hasattr(iterable, '__iter__') :
       for ver, el in enumerate(iterable) : 
            if ver:
                ret = function_to_apply(ret, el)
            else :
                ret = el
       return ret
    else :
        raise TypeError("The data is not iterable") 


if __name__ == '__main__':


    print(ft_reduce((lambda x, y: x + y), [1]))
    print(ft_reduce((lambda x, y: x * y), [1, 2, 3, 4]))

    lst = ['H', 'e', 'l', 'l', 'o', ' ' , 'w', 'o', 'r', 'l', 'd']
    print(ft_reduce(lambda u, v: u + v, lst))

        