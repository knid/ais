# -*- coding: utf-8 -*-
import requests

from typing import List, Union

from ais.client.abstract import AbstractClient
from ais.history import History
from ais.request import Request
from ais.response import Response


class ChatGPTClient(AbstractClient):
    BASE_URL = "https://api.openai.com/v1"

    def __init__(self, ACCESS_KEY: Union[str, None] = None) -> None:
        super().__init__(ACCESS_KEY)

    @property
    def token(self) -> str:
        return self._ACCESS_KEY

    @token.setter
    def token(self, val: str) -> None:
        self._ACCESS_KEY = val

    def make_req(self, req: Request) -> Response:
        if self._ACCESS_KEY is None:
            raise Exception("Access key not found!\nPlease set openai api key with 'ais set ACCESS_KEY <KEY>'")
        res = requests.post(
            f"{self.BASE_URL}/chat/completions",
            headers={
                "Authorization": f"Bearer {self._ACCESS_KEY}",
                "Content-Type": "application/json",
            },
            data=req.as_json(),

        )
        try:
            if res.json()["error"]["code"] == "invalid_api_key":
                raise Exception("Access key is not valid!\
                \nPlease provide a valid openai api key with 'ais set ACCESS_KEY <KEY>'")
        except KeyError:
            pass
        res = Response.from_res(res)
        self.insert_history(History(req, res))
        return res

    def insert_history(self, history: History) -> None:
        self._history.append(history)

    def history(self) -> List[History]:
        return self._history

    def get_last(self) -> History:
        return self._history[-1]
