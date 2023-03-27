# -*- coding: utf-8 -*-
import os
import sys
import cmd
import argparse

import ais
from ais.status import ExitStatus
from ais.console.parser import InputParser
from ais.console.console import App
from ais.utils.console import clear


def parse_args():
    parser = argparse.ArgumentParser(
        prog="ais",
        description="Command line helper tool powered by ChatGPT"
    )
    parser.add_argument("-c", "--command", help="Run code without interactive mode")
    parser.add_argument("-v", "--version", action='version', version="%(prog)s " + ais.__version__)
    args = parser.parse_args()
    return args


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

        self.app.run(parser)


def main() -> ExitStatus:
    args = parse_args()
    if args.command:
        app = App()
        parser = InputParser(args.command)
        try:
            app.run(parser)
            return ExitStatus.SUCCESS
        except KeyboardInterrupt:
            return ExitStatus.KEYBOARD_INTERRUPT
    try:
        clear()
        CmdParse().cmdloop()
        return ExitStatus.SUCCESS
    except KeyboardInterrupt:
        return ExitStatus.KEYBOARD_INTERRUPT
