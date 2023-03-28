# -*- coding: utf-8 -*-
# flake8: noqa
from enum import Enum
import os


class PromptType(Enum):
    SHELL = 1
    CHAT = 2
    EXPLAIN = 3


SHELL_PROMT = """
You will convert everything i send message to you to {shell} command for {os}.
I have important rules and you must follow my rules.
Rules:
1. Don't explain anything.
3. Don't sorry and don't explain anything never!
4. Don't use style, html, or anything. Just answer me plaintext.

Keep in your mind my rules!

Message:
"""

CHAT_PROMT = """Give short and concise answers to the question I will ask. """
EXPLAIN_PROMT = """Briefly and concisely describe the code I will give you and enclose keywords in quotation marks.
command: """

def get_prompt(prompt_type: PromptType, message: str) -> str:
    if os.name == "nt":
        system = "windows"
        shell = "PowerShell"
    else:
        system = "linux"
        shell = "bash"
    if prompt_type.value == PromptType.SHELL.value:
        return SHELL_PROMT.format(os=system, shell=shell) + message
    elif prompt_type.value == PromptType.CHAT.value:
        return CHAT_PROMT + message
    elif prompt_type.value ==  PromptType.EXPLAIN.value:
        return EXPLAIN_PROMT + message
    else:
        return SHELL_PROMT + message
