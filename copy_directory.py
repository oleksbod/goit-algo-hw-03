import os
import shutil

def copy_and_sort_files(source_dir, destination_dir):
    try:
        # Отримуємо повні шляхи до директорій
        source_dir = get_full_path(source_dir, True)        
        destination_dir = get_full_path(destination_dir)

        # Створюємо директорію призначення, якщо вона не існує
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        # Рекурсивно копіюємо та сортуємо файли
        recursive_copy_and_sort(source_dir, destination_dir)

        print("Копіювання та сортування завершено.")
    except Exception as e:
        print(f"Помилка: {e}")


def recursive_copy_and_sort(current_dir, destination_dir):
    try:
        for item in os.listdir(current_dir):
            item_path = os.path.join(current_dir, item)

            if os.path.isdir(item_path):
                # Рекурсивно обробляємо піддиректорії
                recursive_copy_and_sort(item_path, destination_dir)
            elif os.path.isfile(item_path):
                # Копіюємо файли
                copy_file(item_path, destination_dir)
    except PermissionError as e:
        print(f"Помилка: Немає доступу до директорії {current_dir}.")
    except Exception as e:
        print(f"Помилка при копіюванні директорії {current_dir}: {e}")

def copy_file(file_path, destination_dir):
    try:
        # Отримуємо розширення файлу
        _, file_extension = os.path.splitext(file_path)
        file_extension = file_extension[1:]  # Видаляємо крапку з початку розширення

        # Створюємо піддиректорію за розширенням, якщо вона не існує
        subdir_path = os.path.join(destination_dir, file_extension)
        if not os.path.exists(subdir_path):
            os.makedirs(subdir_path)

        # Копіюємо файл у відповідну піддиректорію
        shutil.copy2(file_path, os.path.join(subdir_path, os.path.basename(file_path)))
        print(f"Скопійовано: {file_path}")

    except PermissionError as e:
        print(f"Помилка: Немає доступу до файлу {file_path}.")
    except Exception as e:
        print(f"Помилка при копіюванні файлу {file_path}: {e}")

def get_full_path(directory, is_source_dir = False):
    if directory is None or directory == '':
        directory = os.path.join(os.path.dirname(__file__), 'source' if is_source_dir else 'dist')

    # Якщо директорія не починається з назви диску, то шукаємо її в поточній директорії
    elif not os.path.isabs(directory):
        directory = os.path.join(os.path.dirname(__file__), directory)
        
    return os.path.abspath(directory)

if __name__ == "__main__":
    # Отримуємо введення від користувача через консоль
    source_dir = input("Введіть шлях до вихідної директорії (за замовчуванням: 'source' в поточній директорії): ")
    destination_dir = input("Введіть шлях до директорії призначення (за замовчуванням: створюється 'dist' в поточній директорії): ")

    copy_and_sort_files(source_dir, destination_dir)
