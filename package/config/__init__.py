
from pathlib import Path

from package.config.Config import ConfigHandler

config_path = Path('./config/main.json')

handler = ConfigHandler(config_path)
config = handler.load()
