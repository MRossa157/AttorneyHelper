import os

from factions import load_factions
from word_worker import WordWorker
from work_mode_factory import WorkModeFactory


def main():
    print("Выберите режим работы:")
    for mode_id, mode in WorkModeFactory.modes.items():
        print(f"{mode_id}. {mode.name}")
    mode_choice = input("Введите номер режима: ")

    try:
        mode = WorkModeFactory.get_mode(int(mode_choice))
    except ValueError:
        print("Неверный выбор режима. Завершение программы.")
        return

    factions = load_factions()
    print("\nДоступные фракции:")
    for faction_name in factions:
        print(f"- {faction_name}")

    faction_choice = input("Введите название фракции: ")
    faction = factions.get(faction_choice)

    if faction is None:
        print("Неверный выбор фракции. Завершение программы.")
        return

    case_number = input(f"Введите номер {mode.name.lower()}: ")

    output_path = os.path.join(
        os.path.dirname(__file__),
        f"{case_number}_{mode.name}_{faction_choice}.docx",
    )

    worker = WordWorker(mode=mode, faction=faction, case_number=case_number)
    worker.fill_template(output_path)
    print(f"Документ успешно создан: {output_path}")


if __name__ == "__main__":
    main()
