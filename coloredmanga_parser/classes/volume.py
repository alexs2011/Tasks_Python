import os

from classes.chapter import Chapter


class Volume:
    def __init__(self, name: str, chapters: dict[str, str] | list[dict], from_file: bool = False) -> None:
        """
        Класс, хранящий название тома и список его глав.
        """
        self.name = name
        self.chapters: list[Chapter] = []
        self.from_file = from_file

        self.__build_chapters(chapters)

    def __repr__(self):
        """
        Строковое представление класса в формате JSON.
        """
        return '' \
               f'\n\t{{\n"vol_name": "{self.name}",\n' \
               f'\t"chapters": {self.chapters}\n}}'

    def __len__(self) -> int:
        """
        Возвращает количество глав в томе.
        """
        return len(self.chapters)

    def __build_chapters_from_url(self, chapters: dict[str, str]) -> None:
        """`
        Формирует список глав для данных, полученных из удалённого источника.
        """
        for chapter_name, chapter_url in chapters.items():
            self.chapters.append(Chapter(chapter_name, chapter_url))

    def __build_chapters_from_file(self, chapters: list[dict]) -> None:
        """`
        Формирует список глав для данных, полученных из файла.
        """
        for ch in chapters:
            self.chapters.append(Chapter(ch['name'], ch['url'], raw_pages=ch['pages'], from_file=True))

    def __build_chapters(self, chapters: dict[str, str] | list[dict]) -> None:
        """
        Формирует список глав данного тома с учётом того, откуда поступают данные.
        """
        if self.from_file:
            self.__build_chapters_from_file(chapters)
        else:
            self.__build_chapters_from_url(chapters)

    def download(self, path: str, is_flatten: bool) -> None:
        path = f"{path}{self.name}\\"
        os.makedirs(path, exist_ok=True)


