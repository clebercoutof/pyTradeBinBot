from simplecfg.config import Config


class SynchronousConfig(Config):
	"""All usages are identical to simplecfg.Config, except changes are saved to the disk automatically.

	**ALL MUTATORS** will trigger a write_file() operation!
	"""

	def __init__(self, path: str):
		super().__init__(path)


	def set(self, key: str, value):
		super().set(key, value)
		self.write_file()


	def delete(self, key: str) -> bool:
		result = super().delete(key)
		self.write_file()
		return result


	def wipe(self):
		super().wipe()
		self.write_file()
