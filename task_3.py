from task_3_decor import decorator


def advanced_search(integer_lst, searched_value):
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

@decorator
def search(integer_lst, searched_value):
	return searched_value in integer_lst

lst = [-3, 7, -3, 13, -4, 1, 10, 3, 19, 6, 12, 13, 3, 6, 19, 22, 25, 21, 11, 3]

print(advanced_search(lst, 3))
print(search(lst, 3))
