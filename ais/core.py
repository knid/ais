# -*- coding: utf-8 -*-
import os
import sys
import cmd

from ais.status import ExitStatus
from ais.console.parser import InputParser
from ais.console.console import App


class CmdParse(cmd.Cmd):
    prompt = "ais • "

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.inputs = []
        self.app = App()

    def do_prompts(self, _: str) -> None:
        self.app.print(self.inputs)

    def do_exit(self, _) -> None:
        sys.exit()

    def default(self, line: str) -> None:
        self.inputs.append(line)
        parser = InputParser(line)
        if parser.is_cmd():
            os.system(parser.get_cmd())
        elif parser.is_ask():
            self.app.ask(parser.get_ask())
        elif parser.is_set():
            key, val = parser.get_set()
            self.app.config.set_config(key, val)
        else:
            self.app.shell_cmd(line)


def main() -> ExitStatus:
    try:
        CmdParse().cmdloop()
        return ExitStatus.SUCCESS
    except KeyboardInterrupt:
        return ExitStatus.KEYBOARD_INTERRUPT
