import json
from pathlib import Path

from pydantic import BaseModel
from pydantic.tools import parse_obj_as


class Config(BaseModel):
    telegram_token: str


class ConfigHandler:
    def __init__(
            self,
            config_path: Path
    ) -> None:
        self.config_path = config_path

        if not self.config_path:
            raise Exception(
                f"Config file at {self.config_path.absolute()} doesn't exist"
            )


    def load(self) -> Config:
        with open(self.config_path, mode='r') as handle:
            contents = handle.read()
            config = parse_obj_as(Config, json.loads(contents))

            return config
