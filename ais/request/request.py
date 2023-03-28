# -*- coding: utf-8 -*-
from typing import Dict
import json

from ais.utils.prompt import PromptType, get_prompt


class Request:
    def __init__(
        self,
        prompt: str,
        model: str = "gpt-3.5-turbo",
        role: str = "user",
        prompt_type: PromptType = PromptType.SHELL,
    ) -> None:
        self._model = model
        self._prompt = prompt
        self._role = role
        self._prompt_type = prompt_type

    def as_json(self) -> str:
        return json.dumps(
            {
                "model": self._model,
                "temperature": 0.2,
                "messages": [
                    {
                        "role": self._role,
                        "content": get_prompt(self._prompt_type, self._prompt),
                    }
                ],
            }
        )
