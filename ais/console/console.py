# -*- coding: utf-8 -*-
import sys
import os

import questionary
from rich.console import Console as RichConsole

from ais.client.chatgpt import ChatGPTClient
from ais.config.config import Config
from ais.request import Request
from ais.utils.prompt import PromptType
from ais.utils.console import clear


class App(RichConsole):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.config = Config()
        self.client = ChatGPTClient(self._get_access_key())
        clear()

    def shell_cmd(self, input: str) -> None:
        choices = ["✅ Run this command", "❔ Explain this command", "❌ Cancel"]
        try:
            data = self.get_data(Request(prompt=input, prompt_type=PromptType.SHELL))
        except Exception as e:
            self.print(str(e))
            return

        self.print_data("Command", data)

        answer = questionary.select(
            "Select action",
            choices=choices,
            style=questionary.Style([("answer", "fg:#ffffff bold")]),
        ).ask()
        print()
        if answer == choices[0]:
            os.system(data)
        elif answer == choices[1]:
            self.explain_of_cmd(data)
        else:
            pass
        print()

    def ask(self, input: str) -> None:
        data = self.get_data(Request(prompt=input, prompt_type=PromptType.CHAT))
        self.print(data)

    def explain_of_cmd(self, cmd: str) -> None:
        data = self.get_data(Request(prompt=cmd, prompt_type=PromptType.EXPLAIN))
        self.print_data("Explain", data)

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