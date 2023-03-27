# -*- coding: utf-8 -*-
from pathlib import Path
from typing import Tuple


class InputParser:
    CMD_PREFIX = "!"
    AIS_PREFIX = "ais"
    AIS_ASK_PREFIX = "ais ask"
    AIS_SET_PREFIX = "ais set"

    COMMANDS = {
        "!": "Run raw command.\n\n! <CMD>",
        "ais": "Run ais command.\n\nais {ask, set}",
        "ais ask": "Ask a queston to ai.\n\nais ask <question>",
        "ais set": f"Set config. (see for keys: {Path.home().as_posix()}\
            /.config/ais/config.json)\n\nais set <KEY> <VALUE>",
    }

    def __init__(self, input: str) -> None:
        self.input = input.strip()

    def is_cmd(self) -> bool:
        return self.check_prefix(self.CMD_PREFIX)

    def is_ais_command(self) -> bool:
        return self.check_prefix(self.AIS_PREFIX)

    def is_ask(self) -> bool:
        return self.check_prefix(self.AIS_ASK_PREFIX)

    def is_set(self) -> bool:
        return self.check_prefix(self.AIS_SET_PREFIX)

    def get_cmd(self) -> str:
        if self.is_cmd():
            return self.input[len(self.CMD_PREFIX):]
        return ""

    def get_ask(self) -> str:
        if self.is_ask():
            return self.input[len(self.AIS_ASK_PREFIX):]
        return ""

    def get_set(self) -> Tuple[str, str]:
        if self.is_set():
            input = self.input[len(self.AIS_SET_PREFIX):]
            splitted = input.split()
            return (splitted[0], splitted[1])
        return ("", "")

    def get_help_text(self, key: str) -> str:
        return self.COMMANDS[key]

    def check_prefix(self, val: str) -> bool:
        return True if self.input.startswith(val) else False
