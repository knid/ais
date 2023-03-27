# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod, abstractproperty
from typing import Dict, List, Union

from ais.response import Response
from ais.request import Request
from ais.history import History


class AbstractClient(ABC):
    def __init__(self, ACCESS_KEY: Union[str, None]) -> None:
        self._ACCESS_KEY = ACCESS_KEY
        self._history: List[History] = []

    @abstractproperty
    def token(self) -> str:
        pass

    @token.setter
    def token(self, val: str) -> None:
        pass

    @abstractmethod
    def make_req(self, req: Request) -> Response:
        pass

    @abstractproperty
    def history(self) -> List[History]:
        pass

    @abstractmethod
    def get_last(self) -> History:
        pass

    @abstractmethod
    def insert_history(self, history: History) -> None:
        pass
