import json
import os

from utility.decorators import console_log
from classes.manga import Manga

# Название манги и глав может содержать символы, запрещённые в именах папок.
# В этом случае они должны быть удалены.
WINDOWS_PROHIBITED_DIR_NAME_CHARS = ["<", ">", "*", "?", "/", "\\", "|", ":", '"']


def build_contents(link: str, from_file: bool = False) -> Manga:
    """
    Создаёт и возвращает экземпляр класса Manga.
    """
    return Manga(link, from_file)


@console_log(info='Данные сохранены')
def save_contents(manga: Manga, filename: str = "..\\coloredmanga_parser\\data\\contents.json") -> None:
    """
    Сохраняет содержимое, то есть иерархию файлов, класса Manga в файл в формате JSON.
    """
    data_json = str(manga)
    data_json = json.loads(data_json)

    try:
        with open(filename, 'w', encoding='utf-8') as f_out:
            json.dump(data_json, f_out, indent=2)
    except PermissionError:
        raise PermissionError("Файл доступен только для чтения. Измените атрибуты доступа.")


def download_manga(contents: Manga, dir_root: str, is_flatten: bool = False, start_vol: int = 0,
                   end_vol: int = 0) -> None:
    """
    Загружает и сохраняет в корневую директорию dir_root мангу, сохраняя при этом иерархию томов и глав contents.
    Параметр is_flatten позволяет создавать при сохранении упрощённую иерархию файлов (без папок для глав, т.е. 
    все страницы хранятся в самой папке тома):

    Иерархия при is_flatten=False                   Иерархия при is_flatten=True
    Manga_name.                                     Manga_name.
    +---Volume...                                   \---Volume...
    |   \---Chapter...                                  0001.jpg
    |           001.jpg                                 0002.jpg
    |           002.jpg                                 0003.jpg
    |           003.jpg

    Параметры start_vol и end_vol позволяют задать начальный и конечный тома для скачивания. Если значение равно 0, то
    ограничений нет. Если параметр end_vol задан, то производится скачивание томов до него не включительно, т.е. 
    при start_vol=5, end_vol=9 будут скачаны тома 5, 6, 7, 8.
    """
    contents.download(dir_root, is_flatten, start_vol, end_vol)


def create_dir(path: str) -> str:
    """
    Создаёт директорию по пути path, при этом из пути удаляются все неподдерживаемые Windows символы. Возвращает 
    путь, по которому была создана директория.
    """
    split_path = list(filter(None, path.split("\\")))
    name = split_path[-1]
    new_path = split_path[:-1]
    for ch in WINDOWS_PROHIBITED_DIR_NAME_CHARS:
        name = name.replace(ch, "")
    new_path.append(name)
    new_path = "{0}".format('\\'.join(new_path)) + "\\"
    os.makedirs(new_path, exist_ok=True)
    return new_path
