import pytest
import os
from pathlib import Path

import dictcombiner as dc

def test_trivial():
	script_dir = Path(__file__).parent.resolve()
	base_yml = Path(script_dir, 'testdata', 'base.yml')
	sub_yml_dir = Path(script_dir, 'testdata', 'sub')
	combiner = yc.YamlCombiner(base_yml, sub_yml_dir)

def test_combine_dicts():
	base_dict = {
		'config': 15,
		'settings': {
			'a': 1,
			'b': 2,
			'c': 3
		}
	}

	sub_dicts = [
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

	result_dict = yc.utils.combine_dicts(base_dict, sub_dicts)

	assert result_dict == expected_result_dict
