import copy


def merge_two_lists(list_a: list, list_b: list) -> list:
	return list(set(list_a + list_b))


# merge two dicts, where dict b overwrites dict a
# With dictionaries, we apply the same logic recursively
# With lists, we merge them as sets, ensuring no duplicate entries
def merge_two_dicts(dict_a: dict, dict_b: dict) -> dict:
	# Start with dict_a, so if dict_b is empty we return dict_a
	result_dict = copy.deepcopy(dict_a)

	for key, value in dict_b.items():
		if isinstance(value, dict) and key in result_dict:
			result_dict[key] = merge_two_dicts(result_dict[key], value)
		elif isinstance(value, list) and key in result_dict:
			result_dict[key] = merge_two_lists(result_dict[key], value)
		else:
			result_dict[key] = value

	return result_dict


# Combine a list of dicts into a result dict
def merge_dicts(dicts: [dict]) -> dict:
	if len(dicts) == 1:
		return dicts[0]

	last_dict = dicts.pop()
	return merge_two_dicts(merge_dicts(dicts), last_dict)
