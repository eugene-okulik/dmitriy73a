import argparse
import os
import re
from collections import defaultdict
from colorama import Fore, Style, init

init(autoreset=True)
parser = argparse.ArgumentParser(description="Анализ логов")

parser.add_argument("path", help="Путь к файлу")
parser.add_argument("--text", help="Текст для поиска, обязательный аргумент, "
                                   "регистрозависим", required=True)

ar = parser.parse_args()

path = ar.path
text = ar.text


def parse_logs(path):
    """разбиваем по дате/времени и возвращаем все логи файла без JSON"""
    logs_dict = {}
    current_key = None
    current_block = []
    pattern = re.compile(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+")
    with open(path, encoding="utf-8", errors="ignore") as file:
        for line in file:
            search = re.search(pattern, line)
            # очищаю строку от JSON
            line = " ".join([e for e in line.split() if len(e) < 1000])
            if search:
                if current_key:
                    logs_dict[current_key] = "\n".join(current_block)
                current_key = search.group()
                current_block = [line.strip()]
            else:
                current_block.append(line.strip())
        if current_key:
            logs_dict[current_key] = "\n".join(current_block)
    return logs_dict, path


def search_text_in_logs(logs_dict, path):
    """поиск текста и сохранение результатов +-5 слов"""
    final_dict = defaultdict(list)
    for k, v in logs_dict.items():
        v = v.split()
        for i in range(len(v)):
            if text in v[i]:
                final_dict[k].append(
                    " ".join(v[max(0, i - 5): i + 6]))
    return final_dict, path


def present_logs(final_dict, path):
    """вывод результатов поиска текста в файле"""
    if final_dict:
        print(Fore.MAGENTA + f"по заданному тексту {Fore.RED + text + Style.RESET_ALL}",
              Fore.MAGENTA + f"в файле {os.path.basename(path)} найдено: ")
        for k, v in final_dict.items():
            print(Fore.GREEN + f"в логе от {k}")
            for i in v:
                print(i.replace(text, Fore.RED + text + Style.RESET_ALL))
    else:
        print(
            f"не найдено совпадений по тексту {Fore.RED + text + Style.RESET_ALL} в "
            f"файле {Fore.MAGENTA + os.path.basename(path) + Style.RESET_ALL}")


if os.path.isfile(path):
    present_logs(*search_text_in_logs(*parse_logs(path)))


elif os.path.isdir(path):
    for file in os.listdir(path):
        filepath = os.path.join(path, file)
        if os.path.isfile(filepath):
            present_logs(*search_text_in_logs(*parse_logs(filepath)))

else:
    print("некорректный путь к файлу/директории")
