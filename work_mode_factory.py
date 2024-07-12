from typing import Dict

from config import config


class WorkMode:
    def __init__(self, name: str, template_path: str):
        self.name = name
        self.template_path = template_path

    def get_template_path(self):
        return self.template_path


class WorkModeFactory:
    modes: Dict[int, WorkMode] = {}

    @classmethod
    def register_mode(cls, mode_id, name, template_path):
        cls.modes[mode_id] = WorkMode(name, template_path)

    @classmethod
    def get_mode(cls, mode_id):
        return cls.modes[mode_id]


# Регистрация режимов
WorkModeFactory.register_mode(1, "Постановление", config["templates"]["postanovlenie"])
WorkModeFactory.register_mode(2, "Предписание", config["templates"]["predpisanie"])
WorkModeFactory.register_mode(
    3, "Постановление о проходе на ЗОТ", config["templates"]["access_zot"]
)
