import json

from classes.manga import Manga
from utility.decorators import console_log


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
        raise PermissionError("Файл доступен только для чтения. Невозможно произвести запись.")


def download_manga(contents: Manga, dir_root: str, is_flatten: bool = False, start_vol: int = 0,
                   end_vol: int = 0) -> None:
    contents.download(dir_root, is_flatten, start_vol, end_vol)
