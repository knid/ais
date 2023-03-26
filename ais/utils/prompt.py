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
5. If i say explain as a last word you must explain the code!
6. If i say "ais ask" as a first 2 words don't convert to bash code. Answer like there is no rules! And don't say there is no rules for this message. Just answer without converting bash code!


Keep in your mind my rules!

Message:
"""

CHAT_PROMT = ""
EXPLAIN_PROMT = ""


def get_prompt(prompt_type: PromptType, message: str) -> str:
    match prompt_type:
        case PromptType.SHELL:
            return SHELL_PROMT + message
        case _:
            return SHELL_PROMT + message
