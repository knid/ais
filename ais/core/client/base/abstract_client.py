# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod, abstractproperty
from typing import Dict, List

from ais.core.response.base import AbstractResponse
from ais.core.request.base import AbstractRequest
from ais.history import History


class AbstractClient(ABC):
    def __init__(self, ACCESS_TOKEN: str) -> None:
        self._ACCESS_TOKEN = ACCESS_TOKEN
        self._history: List[History]

    @abstractproperty
    def token(self) -> str:
        return self._ACCESS_TOKEN

    @token.setter
    def token(self, val: str) -> None:
        pass

    @abstractmethod
    def make_req(self, req: AbstractRequest) -> AbstractResponse:
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
