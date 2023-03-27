# -*- coding: utf-8 -*-
import sys
from pathlib import Path

current_path = Path(__file__).parent.parent.resolve()
sys.path.append(str(current_path))


from ais.console.parser import InputParser  # noqa: E402


def test_ask():
    assert InputParser("ais ask How are you?").is_ask()


def test_cmd():
    assert InputParser("!ls?").is_cmd()


def test_set():
    assert InputParser("ais set ACCESS_KEY abcdgla1231").is_set()


def test_set_key_value():
    assert InputParser("ais set ACCESS_KEY abcdgla1231").get_set() == ("ACCESS_KEY", "abcdgla1231")


def test_cmd_value():
    assert InputParser("!cd a/random/file").get_cmd() == "cd a/random/file"


def test_ask_value():
    assert InputParser("ais ask How are you?").get_ask().strip() == "How are you?"
