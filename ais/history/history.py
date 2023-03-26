# -*- coding: utf-8 -*-
from ais.request import Request
from ais.response import Response


class History:
    def __init__(self, req: Request, res: Response) -> None:
        self._req = req
        self._res = res

    @property
    def request(self) -> Request:
        return self._req

    @property
    def response(self) -> Response:
        return self._res
