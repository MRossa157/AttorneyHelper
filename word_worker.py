from dataclasses import dataclass
from datetime import datetime
from typing import Dict

from docxtpl import DocxTemplate

from config import config
from work_mode_factory import WorkMode


@dataclass
class WordWorker:
    mode: WorkMode
    faction: Dict[str, str]
    case_number: str

    def fill_template(self, output_path):
        replacements = {
            "faction_name": self.faction["name"],
            "small_faction_name": self.faction["name"].lower(),
            "leaders_name": self.faction["leader_name_surname"],
            "lead_dis": self.faction["leader_discord"],
            "my_fio": config["personalInfo"]["fio"],
            "my_dis": config["personalInfo"]["discord"],
            "my_rank": config["personalInfo"]["rank"],
            "date": datetime.now().strftime("%d.%m.%Y"),
            "number": self.case_number,
        }

        doc = DocxTemplate(self.mode.get_template_path())
        doc.render(replacements)
        doc.save(output_path)
