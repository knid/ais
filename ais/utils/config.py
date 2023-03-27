# -*- coding: utf-8 -*-
import json


def get_default_config():
    return {"ACCESS_KEY": "", "askBeforeRun": True}


def generate_default_config_json():
    return json.dumps(get_default_config(), indent=4)
