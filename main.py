import os

import factions
from word_worker import WordWorker, WordWorkerMode


def main():
    print("Выберите режим работы:")
    print("1. Постановление")
    print("2. Предписание")
    mode_choice = input("Введите номер режима (1 или 2): ")

    if mode_choice == "1":
        mode = WordWorkerMode.Postanovlenie
    elif mode_choice == "2":
        mode = WordWorkerMode.Predpisanie
    else:
        print("Неверный выбор режима. Завершение программы.")
        return

    print("\nДоступные фракции:")
    for faction_name in factions.__dict__.keys():
        if not faction_name.startswith("__"):
            print(f"- {faction_name}")

    faction_choice = input("Введите название фракции: ")
    faction = getattr(factions, faction_choice, None)

    if faction is None:
        print("Неверный выбор фракции. Завершение программы.")
        return

    case_number = input(
        "Введите номер постановления: "
        if mode == WordWorkerMode.Postanovlenie
        else "Введите номер предписания: "
    )

    output_path = os.path.join(
        os.path.dirname(__file__),
        f"{mode.value['name']}_{faction_choice}_{case_number}.docx",
    )

    worker = WordWorker(mode=mode, faction=faction, case_number=case_number)
    worker.fill_template(output_path)
    print(f"Документ успешно создан: {output_path}")


if __name__ == "__main__":
    main()
