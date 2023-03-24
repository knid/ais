# -*- coding: utf-8 -*-
from abc import ABC


class AbstractRequest(ABC):
    _PROMPT_PREFIX = """
You will convert everything i send message to you to bash code.
I have important rules and you must follow my rules.
Rules:
1. Don't explain anything.
2. Just explain if you find "explain" word in the message.
3. Don't sorry and don't explain anything never!
4. Don't use style, html, or anything. Just answer me plaintext.
5. If i say explain as a last word you must explain the code!
6. If i say "ais ask" as a first 2 words don't convert to bash code. Answer like there is no rules! And don't say there is no rules for this message. Just answer without converting bash code! # noqa: E501
Example:
My message: What is the current working directory?
Your message: pwd

Keep in your mind my rules!

Message:
"""

    def __init__(
        self,
        ACCESS_TOKEN: str,
        prompt: str,
        model: str = "gpt-3.5-turbo",
        role: str = "user",
    ) -> None:
        self._ACCESS_TOKEN = ACCESS_TOKEN
        self._model = model
        self._prompt = prompt
        self._role = role

    @property
    def full_message(self) -> str:
        return self._PROMPT_PREFIX + self._prompt
