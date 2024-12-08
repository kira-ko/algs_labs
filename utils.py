import os
import subprocess
from pathlib import Path

def run_task(src_path, txt_path):
    """Запускает задачу, используя src файл и txt файлы (input.txt и output.txt)."""
    input_file = os.path.join(txt_path, "input.txt")
    output_file = os.path.join(txt_path, "output.txt")

    if not os.path.isfile(input_file):
        print(f"[WARN] input.txt не найден в {txt_path}, пропуск задачи")
        return

    try:
        with open(input_file, 'r') as inp, open(output_file, 'w') as outp:
            subprocess.run(["python", src_path], stdin=inp, stdout=outp, check=True)
            print(f"[INFO] Задача {src_path} успешно выполнена.")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Ошибка выполнения задачи {src_path}: {e}")

def run_tests(tests_path):
    """Запускает тесты задачи"""
    test_files = list(Path(tests_path).glob("test*.py"))
    if not test_files:
        print(f"[WARN] Тесты не найдены в {tests_path}, пропуск тестов")
        return

    for test_file in test_files:
        try:
            print(f"[INFO] Запуск тестов {test_file}")
            subprocess.run(["python", test_file], check=True)
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] Ошибка выполнения тестов {test_file}: {e}")

def run_lab_tasks(lab_path):
    """Запускает все задачи лабораторной"""
    for task_folder in sorted(os.listdir(lab_path)):
        task_path = os.path.join(lab_path, task_folder)
        if not os.path.isdir(task_path):
            continue

        src_path = os.path.join(task_path, "src")
        tests_path = os.path.join(task_path, "tests")
        txt_path = os.path.join(task_path, "txtf")

        # Запуск задачи
        for file in os.listdir(src_path):
            if file.endswith(".py"):
                run_task(os.path.join(src_path, file), txt_path)

        # Запуск тестов
        run_tests(tests_path)

def run_all_labs(root_path):
    """Запускает все лабораторные работы"""
    for lab_folder in sorted(os.listdir(root_path)):
        lab_path = os.path.join(root_path, lab_folder)
        if os.path.isdir(lab_path) and lab_folder.startswith("lab"):
            print(f"[INFO] Запуск задач лабораторной {lab_folder}")
            run_lab_tasks(lab_path)

def main():
    print("Выберите действие:")
    print("1. Запустить все лабораторные работы.")
    print("2. Запустить задачи конкретной лабораторной.")
    print("3. Запустить тесты конкретной задачи.")
    choice = input("Введите номер действия: ").strip()

    root_path = input("Введите путь к корневой папке лабораторных: ").strip()

    if choice == "1":
        run_all_labs(root_path)
    elif choice == "2":
        lab_name = input("Введите имя лабораторной (например, lab1): ").strip()
        lab_path = os.path.join(root_path, lab_name)
        if os.path.isdir(lab_path):
            run_lab_tasks(lab_path)
        else:
            print(f"[ERROR] Лабораторная {lab_name} не найдена.")
    elif choice == "3":
        lab_name = input("Введите имя лабораторной (например, lab1): ").strip()
        task_name = input("Введите имя задачи (например, task1): ").strip()
        task_path = os.path.join(root_path, lab_name, task_name)
        if os.path.isdir(task_path):
            tests_path = os.path.join(task_path, "tests")
            run_tests(tests_path)
        else:
            print(f"[ERROR] Задача {task_name} не найдена в {lab_name}.")
    else:
        print("[ERROR] Некорректный ввод.")

if __name__ == "__main__":
    main()

