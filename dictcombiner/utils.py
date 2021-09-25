import deepdiff as dd
import copy

# Modifies the given result dicts value given by tree_path to value
def modify_result_dict(result_dict : dict, tree_path : [str], value):
	key = tree_path[0]

	if key not in result_dict:
		print('Error: ' + str(key) + ' not in result dict:')
		print(result_dict)

	if len(tree_path) == 1:
		result_dict[key] = value
		return

	modify_result_dict(result_dict[key], tree_path[1:], value)

def traverse(result_dict : dict, sub_dict : dict, tree_path : [str]):
	for key, value in sub_dict.items():
		new_tree_path = copy.deepcopy(tree_path)
		new_tree_path.append(key)
		if type(value) is not dict:
			modify_result_dict(result_dict, new_tree_path, value)
		else:
			traverse(result_dict, sub_dict[key], new_tree_path)

# Combine a base and a set of sub dicts into a result dict
def combine_dicts(base_dict : dict, sub_dicts : [dict]):
	result_dict = copy.deepcopy(base_dict)

	for sub_dict in sub_dicts:
		traverse(result_dict, sub_dict, []) 

	return result_dict
