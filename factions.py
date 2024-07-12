import json
from typing import Dict

from config import config


def load_factions() -> Dict[str, Dict[str, str]]:
    with open(config["factionsPath"], "r") as file:
        return json.load(file)
