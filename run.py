import argparse
import os
from pathlib import Path

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

if __name__ == '__main__':
	main()