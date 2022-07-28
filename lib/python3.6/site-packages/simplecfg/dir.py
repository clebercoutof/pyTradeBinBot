import os
import platform

__os = platform.system()

HOME = os.path.expanduser("~")
APP_DATA = HOME
CONFIG = HOME
TEMP = os.path.join("/", "tmp")

if __os == "Linux":
	APP_DATA = os.path.join(HOME, ".local", "share")
	CONFIG = os.path.join(HOME, ".config")
elif __os == "Windows":
	APP_DATA = os.path.join(HOME, "AppData", "Roaming")
	CONFIG = os.path.join(HOME, "AppData", "Roaming")
	TEMP = os.path.join(HOME, "AppData", "Local", "Temp")
elif __os == "Darwin":
	APP_DATA = os.path.join(HOME, "Library", "Application Support")
	CONFIG = os.path.join(HOME, "Library", "Application Support")
else:
	APP_DATA = os.path.join(HOME, ".local", "share")
	CONFIG = os.path.join(HOME, ".config")
