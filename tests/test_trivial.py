import pytest
import os
from pathlib import Path

import dictcombiner as dc

def test_simple_combine():
	dicts = [
	{
		'config': 15,
		'settings': {
			'a': 1,
			'b': 2,
			'c': 3
		}
	},
	{
		'settings': {
			'a': 2,
			'b': 3
		}
	},
	{
		'settings': {
			'a': 5
		}
	}
	]

	expected_result_dict = {
		'config': 15,
		'settings': {
			'a': 5,
			'b': 3,
			'c': 3
		}
	}

	result_dict = dc.utils.combine_dicts(dicts)

	assert result_dict == expected_result_dict

def test_deep_nesting():
	dicts = [
	{
		'a':{
			'b':{
				'c':{
					'd': 1
				}
			}
		}
	},
	{
		'a':{
			'b':{
				'c':{
					'd': 2
				}
			},
			'b2':{
				'c2': 3
			}
		}
	},

	]

	result_dict = dc.utils.combine_dicts(dicts)

	assert result_dict['a']['b']['c']['d'] == 2
	assert result_dict['a']['b2']['c2'] == 3
