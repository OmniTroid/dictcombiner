import argparse
import os
from pathlib import Path
import yaml
import pprint as pp

parser = argparse.ArgumentParser('Combine a set of yaml files into one')

parser.add_argument(
	'--confdir',
	dest='confdir',
	metavar='[confdir]',
	help='Directory which contains config files to combine',
	required=True)
parser.add_argument(
	'--target',
	dest='target',
	metavar='[target]',
	help='Target yaml file',
	required=True)

def main():
	args = parser.parse_args()

	confdir = Path(args.confdir).resolve()
	target = Path(args.target).resolve()

	if not confdir.exists():
		raise FileNotFoundError(confdir)

	if not confdir.is_dir():
		raise NotADirectoryError(confdir)

	if not Path.exists(target.parent):
		raise FileNotFoundError(target.parent)

	if Path.exists(target):
		raise FileExistsError(target)

	# List files in confdir and sort alphabetically
	conf_files = sorted(
		[Path(filename) for filename in confdir.iterdir()],
		key=lambda f: f.name)

	for filename in conf_files:
		with open(filename) as file:
			yaml_data = yaml.safe_load(file)
			pp.PrettyPrinter(indent=4).pprint(yaml_data)

if __name__ == '__main__':
	main()