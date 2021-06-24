def decorator(func):
    def wrapper(integer_lst, searched_value):
        if not isinstance(searched_value, int):
            raise ValueError('Arguments should be integers')

        for i in integer_lst:
            if not isinstance(i, int):
                raise ValueError('Arguments should be integers')

        integer_set = set(integer_lst)
        new_lst = list(integer_set)
        if not searched_value in new_lst:
            result_index = -1
        else:
            result_index = new_lst.index(searched_value)
        return new_lst, result_index
    return wrapper