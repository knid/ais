# -*- coding: utf-8 -*-
from typing import Dict, TypeVar, Type

import requests

T = TypeVar("T", bound="Parent")  # noqa


class Response:
    def __init__(
        self,
        id: str,
        created: int,
        model: str,
        usage: Dict,
        message: str,
        finish_reason: str,
    ) -> None:
        self._id = id
        self._created = created
        self._model = model
        self._usage = usage
        self._message = message
        self._finish_reason = finish_reason

    @classmethod
    def from_res(cls: Type[T], res: requests.Response) -> T:
        data = res.json()
        first_choices = data["choices"][0]
        return cls(
            data["id"],
            data["created"],
            data["model"],
            data["usage"],
            first_choices["message"]["content"],
            first_choices["finish_reason"],
        )

    @property
    def id(self) -> str:
        return self._id

    @property
    def created(self) -> int:
        return self._created

    @property
    def model(self) -> str:
        return self._model

    @property
    def message(self) -> str:
        return self._message
