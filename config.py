import json


def load_config():
    with open("config.json", "r", encoding="utf-8") as file:
        return json.load(file)


config = load_config()

# POSTANOVLENIE_TEMPLATE_PATH = r"templates/postanovlenie_template.docx"
# PREDPISANIE_TEMPLATE_PATH = r"templates/predpisanie_template.docx"
# ACCESS_ZOT_TEMPLATE_PATH = r"templates/access_zot_template.docx"

# FACTIONS_PATH = r"factions.json"

# MY_FIO = "Divine Fearlessez"
# MY_DISCORD = "mrossa"
# MY_RANK = "Военный прокурор"
