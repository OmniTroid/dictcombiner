import dictcombiner as dc


def test_simple_merge():
    dicts = [{
        'config': 15,
        'settings': {
            'a': 1,
            'b': 2,
            'c': 3
        }
    }, {
        'settings': {
            'a': 2,
            'b': 3
        }
    }, {
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

    result_dict = dc.utils.merge_many_dicts(dicts)

    assert result_dict == expected_result_dict


def test_deep_nesting():
    dicts = [
        {
            'a': {
                'b': {
                    'c': {
                        'd': 1
                    }
                }
            }
        },
        {
            'a': {
                'b': {
                    'c': {
                        'd': 2
                    }
                },
                'b2': {
                    'c2': 3
                }
            }
        },

    ]

    result_dict = dc.utils.merge_many_dicts(dicts)

    assert result_dict['a']['b']['c']['d'] == 2
    assert result_dict['a']['b2']['c2'] == 3


def test_combine_empty_dicts():
    dict_a = {
        "dicts": {
            "a": {},
            "b": {},
            "c": {}
        }
    }

    dict_b = {}

    expected_result = {
        "dicts": {
            "a": {},
            "b": {},
            "c": {}
        }
    }

    result_dict = dc.utils.merge_many_dicts([dict_a, dict_b])
    assert result_dict['dicts'] == expected_result['dicts']


def test_merge_lists():
    list_a = [1, 1, 2, 3]
    list_b = [4, 5, 6]
    result = dc.utils.merge_two_lists(list_a, list_b)
    expected = [1, 2, 3, 4, 5, 6]

    assert result == expected


def test_merge_lists_in_dict():
    dict_a = {
        "a": [1, 1, 2, 3],
        "b": [4, 5, 6]
    }

    dict_b = {
        "a": [7, 8, 9],
        "b": [10, 11, 12]
    }

    expected = {
        "a": [1, 2, 3, 7, 8, 9],
        "b": [4, 5, 6, 10, 11, 12]
    }

    result = dc.merge_two_dicts(dict_a, dict_b)
    assert result == expected


def test_merge_dicts():
    dict_a = {
        "a": 1,
        "b": 2
    }

    dict_b = {
        "c": 3,
        "d": 4
    }

    expected = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4
    }

    result = dc.merge_two_dicts(dict_a, dict_b)
    assert result == expected
