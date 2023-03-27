# -*- coding: utf-8 -*-
import os
import json
from pathlib import Path

from ais.utils.config import generate_default_config_json


class Config:
    CONFIG_PATH = Path.home().as_posix() + "/.config/ais/config.json"

    def __init__(self) -> None:
        if not os.path.exists(self.CONFIG_PATH):
            os.makedirs(os.path.dirname(self.CONFIG_PATH), exist_ok=True)
            with open(self.CONFIG_PATH, "w") as f:
                f.write(generate_default_config_json())
        with open(self.CONFIG_PATH, "r") as f:
            self._config = json.load(f)

    def get_config(self, key: str) -> str:
        return self._config[key]

    def set_config(self, key: str, val: str) -> None:
        self._config[key] = val
        with open(self.CONFIG_PATH, "w") as f:
            f.write(json.dumps(self._config, indent=4))
