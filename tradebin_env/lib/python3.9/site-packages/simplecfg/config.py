import os
import json


class Config:
	"""A config file
	"""

	def __init__(self, path: str):
		"""
		Arguments:
			path -- Full path to the configuration file
		"""

		if type(path) is not str:
			path = str(path)

		self.__path = path
		self.__data = {}


	def get(self, key: str):
		"""Get an item from the config

		Arguments:
			key -- The key of the item you wish to recall

		Returns:
			Returns the item if key is found. Otherwise returns None
		"""

		if type(key) is not str:
			key = str(key)

		if key in self.__data:
			return self.__data[key]
		else:
			return None


	def set(self, key: str, value):
		"""Set a value in the config

		Arguments:
			key -- The key for the item you wish to store
			value -- The item to be stored at 'key', any type
		"""

		self.__data[key] = value


	def delete(self, key: str) -> bool:
		"""Remove an item from the config

		Arguments:
			key -- The key of the item you wish to remove

		Returns:
			The item that was deleted from the config, None if object not found
		"""

		if key in self.__data:
			item = self.__data[key]
			del self.__data[key]
			return item
		else:
			return None


	def get_keys(self) -> list:
		"""Get a list of all keys in the config

		Returns:
			An iterable containing all keys in the config
		"""

		return self.__data.keys()


	def dump(self) -> str:
		"""Get a string representation of the config

		Returns:
			A string containing the JSON
		"""

		return json.dumps(self.__data, indent=4, sort_keys=True)


	def wipe(self):
		"""Delete all keys in the config
		"""

		self.__data = {}


	def __len__(self) -> int:
		"""Get length of the config

		Returns:
			Number of keys in the config
		"""

		return len(self.__data)


	def __contains__(self, key: str) -> bool:
		"""Determines if a key exists in the config

		Arguments:
			key -- Key to check for

		Returns:
			True if the key exists, otherwise False
		"""

		return key in self.__data


	def __getitem__(self, key: str):
		"""Alias for get()
		"""
		
		return self.get(key)


	def __setitem__(self, key: str, value):
		"""Alias for set()
		"""

		self.set(key, value)


	def __delitem__(self, key: str):
		"""Alias for delete
		"""

		self.delete(key)


	def read_file(self, load_if_corrupt = False):
		"""Load the config from disk

		Keyword Arguments:
			load_if_corrupt -- If True, loading a corrupt file will produce an empty config, as opposed to a ValueError (default: {False})

		Raises:
			ValueError: Raised if 'load_if_corrupt' == False and the config file is corrupted
		"""

		f = self.__get_config_file()

		file_data = f.read()

		if len(file_data) <= 0:
			file_data = "{}"
		
		try:
			self.__data = json.loads(file_data)
		except ValueError as e:
			if not load_if_corrupt:
				raise ValueError("Configuration file " + self.__path + " appears to be corrupt!")
			else:
				self.__data = {}

		f.close()


	def write_file(self):
		"""Commit config to disk
		"""

		f = self.__get_config_file("w")

		f.write(self.dump())

		f.close()


	def __get_config_file(self, mode: str = "r"):
		if len(self.__path) <= 0 or self.__path.endswith(os.path.sep) or os.path.isdir(self.__path):
			raise OSError("Invalid configuration file path: " + self.__path)

		if not os.path.exists(self.__path):
			file_dir = os.path.dirname(self.__path)
			if not os.path.exists(file_dir):
				os.makedirs(file_dir)
			open(self.__path, "w").close()
			
		return open(self.__path, mode)
