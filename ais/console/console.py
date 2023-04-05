# -*- coding: utf-8 -*-
import os

import questionary
from rich.console import Console as RichConsole

from ais.client.chatgpt import ChatGPTClient
from ais.console.parser import InputParser
from ais.utils.prompt import PromptType
from ais.config.config import Config
from ais.request import Request


class App(RichConsole):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.config = Config()
        self.client = ChatGPTClient(self._get_access_key())

    def shell_cmd(self, input: str = "", explained: bool = False, data: str = "") -> None:
        if explained and not data:
            raise Exception("Data is not valid")
        choices = ["✅ Run this command", "❌ Cancel"]
        if not explained:
            choices.insert(1, "❔ Explain this command")
            try:
                if not input: Exception("Inpus is not valid")
                data = self.get_data(Request(prompt=input, prompt_type=PromptType.SHELL))
            except Exception as e:
                self.print(str(e))
                return

        if not explained:
            self.print_data("Command", data)

        answer = questionary.select(
            "Select action",
            choices=choices,
            style=questionary.Style([("answer", "fg:#ffffff bold")]),
            pointer="◌"
        ).ask()
        if answer == choices[0]:
            os.system(data)
        elif not explained and answer == choices[1]:
            self.explain_of_cmd(data)
        else:
            pass
        print()

    def ask(self, input: str) -> None:
        data = self.get_data(Request(prompt=input, prompt_type=PromptType.CHAT))
        self.print_data("Result", data)

    def explain_of_cmd(self, cmd: str) -> None:
        data = self.get_data(Request(prompt=cmd, prompt_type=PromptType.EXPLAIN))
        self.print_data("Explain", data)
        self.shell_cmd(explained=True, data=cmd)

    def set_config(self, key: str, val: str) -> None:
        self.config.set_config(key, val)
        if key == "ACCESS_KEY":
            self.client = ChatGPTClient(val)

    def print_data(self, rule_name: str, data: str) -> None:
        self.rule(f" {rule_name} ", style="white bold")
        print()
        self.print(data)
        print()

    def get_data(self, req: Request) -> str:
        with self.status(
            "[white]Waiting response", spinner="bouncingBall", spinner_style="white"
        ):
            res = self.client.make_req(req)
            return res.message

    def _get_access_key(self):
        try:
            return self.config.get_config("ACCESS_KEY")
        except KeyError:
            self.print(
                "[bold red]Access key is not setted.\
            \nPlease provide a openai acceess key with ais set ACCESS_KEY <KEY>"
            )

    def run(self, parser: InputParser) -> None:
        if parser.is_ask():
            self.ask(parser.get_ask())
        elif parser.is_set():
            key, val = parser.get_set()
            self.config.set_config(key, val)
        elif parser.is_ais_command():
            self.print("[red bold]Command error[/red bold] Help for ais:")
            self.print(f'{parser.get_help_text("ais")}')
        elif parser.is_cmd():
            os.system(parser.get_cmd())
        else:
            self.shell_cmd(parser.input)
        print()
