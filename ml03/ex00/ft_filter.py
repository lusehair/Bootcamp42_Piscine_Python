def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    An iterable.
    None if the iterable can not be used by the function.
    """

    if not callable(function_to_apply)  :
        raise TypeError("The function is not callable")

    if hasattr(iterable, '__iter__') :
        ret = [] 
        for el in iterable : 
            if function_to_apply(el):
               yield el
    else :
        raise TypeError("The data is not iterable")

if __name__ == '__main__' :

    x = [1, 2, 3, 4, 5]

    print(ft_filter(lambda dum: not (dum % 2), 9))
    # Output:
    # < generator object ft_filter at 0x7f709c777d00 >  # The address will be different

    print(list(ft_filter(lambda dum: not (dum % 2), x)))
    # Output:
    # [2, 4]

    print(list(ft_filter(lambda x: x <= 1, [])))