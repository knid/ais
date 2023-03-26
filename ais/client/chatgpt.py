# -*- coding: utf-8 -*-
import requests

from typing import List

from ais.client.abstract import AbstractClient
from ais.history import History
from ais.request import Request
from ais.response import Response


class ChatGPTClient(AbstractClient):
    BASE_URL = "https://api.openai.com/v1"

    def __init__(self, ACCESS_TOKEN: str) -> None:
        super().__init__(ACCESS_TOKEN)

    @property
    def token(self) -> str:
        return self._ACCESS_TOKEN

    @token.setter
    def token(self, val: str) -> None:
        self._ACCESS_TOKEN = val

    def make_req(self, req: Request) -> Response:
        res = requests.post(
            f"{self.BASE_URL}/chat/completions",
            headers={
                "Authorization": f"Bearer {self._ACCESS_TOKEN}",
                "Content-Type": "application/json",
            },
            data=req.as_json(),
        )
        res = Response.from_res(res)
        self.insert_history(History(req, res))
        return res

    def insert_history(self, history: History) -> None:
        self._history.append(history)

    def history(self) -> List[History]:
        return self._history

    def get_last(self) -> History:
        return self._history[-1]
