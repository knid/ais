# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod, abstractproperty, abstractclassmethod

import requests


class AbstractResponse(ABC):
    def __init__(self, id: str, created: int, model: str, result: str) -> None:
        self._id = id
        self._created = created
        self._model = model
        self._result = result

    @abstractclassmethod
    def from_res(cls, res: requests.Response):
        pass

    @abstractproperty
    def id(self) -> str:
        pass

    @abstractproperty
    def created(self) -> int:
        pass

    @abstractproperty
    def model(self) -> str:
        pass

    @abstractproperty
    def content(self) -> str:
        pass

    @abstractmethod
    def get_code(self) -> str:
        pass
