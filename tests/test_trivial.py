import pytest
import os
from pathlib import Path

import yamlcombiner

def test_trivial():
	script_dir = Path(__file__).parent.resolve()
	base_yml = Path(script_dir, 'testdata', 'base.yml')
	sub_yml_dir = Path(script_dir, 'testdata', 'sub')
	yc = yamlcombiner.YamlCombiner(base_yml, sub_yml_dir)

