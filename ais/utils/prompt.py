# -*- coding: utf-8 -*-
# flake8: noqa
from enum import Enum


class PromptType(Enum):
    SHELL = 1
    CHAT = 2
    EXPLAIN = 3


SHELL_PROMT = """
You will convert everything i send message to you to bash code.
I have important rules and you must follow my rules.
Rules:
1. Don't explain anything.
2. Just explain if you find "explain" word in the message.
3. Don't sorry and don't explain anything never!
4. Don't use style, html, or anything. Just answer me plaintext.

Keep in your mind my rules!

Message:
"""

CHAT_PROMT = """Give short and concise answers to the question I will ask. """
EXPLAIN_PROMT = """Briefly and concisely describe the code I will give you and enclose keywords in quotation marks.
command: """


def get_prompt(prompt_type: PromptType, message: str) -> str:
    if prompt_type.value == PromptType.SHELL.value:
        return SHELL_PROMT + message
    elif prompt_type.value == PromptType.CHAT.value:
        return CHAT_PROMT + message
    elif prompt_type.value ==  PromptType.EXPLAIN.value:
        return EXPLAIN_PROMT + message
    else:
        return SHELL_PROMT + message
