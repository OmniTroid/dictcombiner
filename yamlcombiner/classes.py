from pathlib import Path

class YamlCombiner:
	def __init__(self, base_yml, sub_yml_dir):
		self.base_yml = Path(base_yml)
		self.sub_yml_dir = Path(sub_yml_dir)

		if not self.base_yml.exists():
			raise FileNotFoundError(self.base_yml)

		if not self.base_yml.is_file():
			raise NotAFileError(self.base_yml)

		if not self.sub_yml_dir.exists():
			raise FileNotFoundError(self.sub_yml_dir)

		if not self.sub_yml_dir.is_dir():
			raise NotADirectoryError(self.sub_yml_dir)
