import json

from classes.manga import Manga


def build_contents(link: str, from_file: bool = False) -> Manga:
    """
    Создаёт и возвращает экземпляр класса Manga.
    """
    return Manga(link, from_file)


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

    print("Данные сохранены.")