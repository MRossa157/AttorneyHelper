from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from docxtpl import DocxTemplate

import constants


class WordWorkerMode(Enum):
    Postanovlenie = {"id": 1, "name": "Постановление"}
    Predpisanie = {"id": 2, "name": "Предписание"}


@dataclass
class WordWorker:
    mode: WordWorkerMode
    faction: dict[str, str]
    case_number: str

    def fill_template(self, output_path):
        replacements = {
            "faction_name": self.faction["name"],
            "small_faction_name": self.faction["name"].lower(),
            "leaders_name": self.faction["leader_name_surname"],
            "lead_dis": self.faction["leader_discord"],
            "my_fio": constants.MY_FIO,
            "my_dis": constants.MY_DISCORD,
            "my_rank": constants.MY_RANK,
            "date": datetime.now().strftime("%d.%m.%Y"),
            "number": self.case_number,
        }

        doc = DocxTemplate(self.__get_template_path())
        doc.render(replacements)
        doc.save(output_path)

    def __get_template_path(self):
        if self.mode == WordWorkerMode.Predpisanie:
            return constants.PREDPISANIE_TEMPLATE_PATH
        elif self.mode == WordWorkerMode.Postanovlenie:
            return constants.POSTANOVLENIE_TEMPLATE_PATH
